- get ami img dynamically
```
terraform {
  required_version = "~> 1.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.6"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

data "aws_ami" "ubuntu" {
  most_recent = true
  owners      = ["099720109477"] # Canonical

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-*-amd64-server-*"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }
}

resource "aws_instance" "ubuntu" {
  ami                         = data.aws_ami.ubuntu.id
  instance_type               = "t2.micro"
  associate_public_ip_address = true
  subnet_id                   = aws_subnet.subnet_public.id
}
resource "aws_vpc" "my_vpc" {
  cidr_block           = var.cidr_vpc
  enable_dns_support   = true
  enable_dns_hostnames = true
}
resource "aws_subnet" "subnet_public" {
  vpc_id     = aws_vpc.my_vpc.id
  cidr_block = var.cidr_subnet
}
variable "cidr_vpc" {
  description = "CIDR block for the VPC"
  type        = string
  default     = "172.16.0.0/16"
}
variable "cidr_subnet" {
  description = "CIDR block for the subnet"
  type        = string
  default     = "172.16.10.0/24"
}
```
- iac address manual problems(mis-configure, manage states, transfer)
- iac allow easy share, is a blueprint
- declarative: wysiwyg, tf, cf, verbose but no chance of misconfigure
- imperative: implicit, CDK/Pulumi
- tf altho it is declarative, but has imperative features
- yaml/json has no imperative-like feature
- hcl has imperative-like feature like loop/complex data type/dynamic blocks
- iac -> idempotent, consistent, repeatable,
- tf cloud -> saas that allows remote state/versioncontrol/flexible workflow/colab on infra in a single web portal
- change management, standard practice to apply change and resolve conflict
- change automation creates execution plans and resources graphs to apply and review changesets
- locals, "something-${local.local_var_name}, store an expression for reuse
- null_resource, placeholder resource used together with trigger and provision to run
- data sources use information defined outside of tf/defined by another config/modified by functions.
  - define what kind of external resource you want to select
- named values: resources, var, local, module, data, path.module, count.index
- meta arguments, which can be used with any resource type to change behaviors
  - depends_on
  - count, creating multiple
  - for_each, create multiple according to a map or set of strings
  - provider, select a non-provider from default
    - alias
  - lifecycle
    - create, when resource in config but not in state
    - destroy
    - update in-place
    - destroy and re-create: argument have changed also can't be updated due to api limitations
    - lifecycle, create_before_destroy = true
    - prevent_destroy
    - ignore_changes( list of attributes )
  - provisioner and connection, for taking extra action after resource creation
- expressions
  - double quotes, $${ literal ${
  - interpolation ${..}
  - directive, conditional logic between %{..}
  ```
  <<EOT
  ${ for ip in aws_instance.*.ip ~}
  server ${ip}
  ${ endfor ~}
  ```
  - if else, ternary, var.a != "" ? var.a : "default-a"
  - "for" expression allow iterative over complex type and apply transformation.
  - "for" can accept as input a list/set/tuple/map/object
  - [for s in var.list : upper(s)]
  - [] tuple, {} object
  - splat operator *, [for o in var.list : o.id] = var.list[*].id
  - dynamic, local sg rules list, dynamic ingress for_each local.sg, content = ingress.value.port
  - version constrait, ~> 1.0.0, only last number can be increment
- state mv allows rename resource or move it to another module, prevent create and destroy
- tf plan, read current state of any already exist remote object to make sure it's uptodate
- compare config to prior state and note differences
- propose action that should make remote object match configuration
- tf plan -out = machine code file
- drift: -replace, import, -refresh-only
- taint, mark resource for replacement
- import, create placeholder for imported resource in configuration file, it will not be autofilled.
- terraform import resource_place_holder resource_id, 1 resource at a time.
- terraform refresh will not modify real remote object, but it will modify the tf state
- tf refresh -> tf apply -refresh-only
- refresh-only flag will modify state file to reflect remote state changes.
- if vm is terminated from console, -refresh-only will modify statefile to keep it in sync
- private module has hostname/namespace/name/provider, needs to terraform login to terraform cloud
- public module name has to be named terraform-provider-name
- tf cloud, remote backend, intergrate vcs, tf cloud runtime will tf apply
- backend, how state snapshots are stored.  Standard backend only store state, 3rd party backend are standard like s3
- Enhanced backend can both store state and perform operations
- data terraform_remote_state resource { config = { path = "${path.module}/networking/terraform.tfstate" }} cross-referencing stacks
- tf enterprise is on-prem tf cloud offering
- remote backend means tf cloud or tf enterprise, need to set up provider creds
- remote backend needs tf workspace via name or prefix for multiple workspaces
- terraform init -backend-config=file allows backend to be specified in seperate file
- terraform_remote_state data source retrieve root module output values from anotehr config
- remote_state can only expose root module outputs, nested output needs to be exposed
- resource timeouts setting for create and delete
- complex type: collection vs structural(object)
- list vs set, list has index and ordering but sets has no index/ordering
- structural type needs a schema as argument
- variable "with_optional_attri" {
    type = object({
        a = string
        b = optional(string)
    })
    default = {
        "a" = "hi",
        "b" = "3"
    }
- }
- object vs tuple, object is a map with explicit keying, tuple collection of values without key
- variable "test_tup" {
    type = tuple([string, number, bool])
    default = ["hi", 3, true]
- }
- parseint("100", 10)
- chomp removes newline at the end, format produce string variable interpolation.
- format("hello %s!", "world")
- formatlist("hello %s", ["l1", "l2"])
- indent add # of spaces to beginning of all but the first line
- join, concat
- regexall
- replace/split/strrev/substr/title(cap first letter)/trim(remove char from startand end)
- trimprefix(remove prefix)/trimsuffix(remove suffix)/trimspace(remove all whitespace from both start and end)
- upper
- collection funcs: chunklist
- coalesce("", "b"), return 1st value that isn't null or empty string
- coalescelist, compact(remove empty string in list of string), concat 2 lists
- contains/distinct
- element/index, flatten takes a list and replaces any elements that are lists with flattened sequence
- filesystem funcs: abspath/dirname/basename/pathexpand
- fileset(path.module, "files/*.txt")
- date/time funcs: formatdate/timeadd/timestamp
- ipfuncs: cidrhost("10.12.121.1/20", 16) -> calculate full host ip for a given host number within a cidr
- cidrnetmask convert ipv4 cidr into subnet mask address
- cidrsubnet calculate subnet address within ip prefix, cidrsubnet("10.1.1.1/24", 4, 15) -> 10.1.1.1/28
- cidrsubnets calculate a consecutive ip address ranges
- type conversion evaluates expression and return bool 
- tobool, tomap({"a"=1,"b"="c"})
- try([tostring(var.example),tolist(var.b)]) return result of the first one without error
- org, workspaces, teams, runs
- 3 types of cloud run workflows: vcs(pr trigger), cli, api(upload config file(bash script packaged in archive))
- tf cloud allow publish private module to private registry
- support for module versioning, searchable filterable list
- user token or team token for auth
- cost estimation only specific resources for aws/azure/gcp
- tf version can be chosen for each workspace
- run env is a single use machine in x86
- tf enterprise, self-hosted distro of tf platform
- tf enterprise, postgres/s3
- tf local workspace vs cloud workspace
- tf run triggers, a way to connect workspaces to other workspaces



