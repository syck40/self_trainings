- iptables, tables - chains - rules
```
To give an example, suppose we have an inbound packet destined for our host. The order of execution would be:

1. PREROUTING

Raw

Mangle

NAT

2. INPUT

Mangle

NAT

Filter
```
- sample
```
# Create incoming-ssh chain.
$ iptables -N incoming-ssh

# Allow packets from specific IPs.
$ iptables -A incoming-ssh -s 10.0.0.1 -j ACCEPT
$ iptables -A incoming-ssh -s 10.0.0.2 -j ACCEPT

# Log the packet.
$ iptables -A incoming-ssh -j LOG --log-level info --log-prefix "ssh-failure"

# Drop packets from all other IPs.
$ iptables -A incoming-ssh -j DROP

# Evaluate the incoming-ssh chain,
# if the packet is an inbound TCP packet addressed to port 22.
$ iptables -A INPUT -p tcp --dport 22 -j incoming-ssh
```
- ip masquerading
```
 In Kubernetes, masquerading can make pods use their node’s IP address, despite the fact that pods have unique IP addresses. This is necessary to communicate outside the cluster in many setups, where pods have internal IP addresses that cannot communicate directly with the internet. The MASQUERADE target is similar to SNAT; however, it does not require a --source-address to be known and specified in advance. Instead, it uses the address of a specified interface. This is slightly less performant than SNAT in cases where the new source address is static, as iptables must continuously fetch the address:

$iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
```
- destination nat loadbalacing
```
$ iptables -t nat -A OUTPUT -p tcp --dport 80 -d $FRONT_IP -m statistic \
--mode random --probability 0.5 -j DNAT --to-destination $BACKEND1_IP:80
$ iptables -t nat -A OUTPUT -p tcp --dport 80 -d $FRONT_IP \
-j DNAT --to-destination $BACKEND2_IP:80

In the previous example, there is a 50% chance of routing to the first backend. Otherwise, the packet proceeds to the next rule, which is guaranteed to route the connection to the second backend. 
```
- DNAT problems
```
Using DNAT fan-out for load balancing has several caveats. It has no feedback for the load of a given backend and will always map application-level queries on the same connection to the same backend. Because the DNAT result lasts the lifetime of the connection, if long-lived connections are common, many downstream clients may stick to the same upstream backend if that backend is longer lived than others. To give a Kubernetes example, suppose a gRPC service has only two replicas and then additional replicas scale up. gRPC reuses the same HTTP/2 connection, so existing downstream clients (using the Kubernetes service and not gRPC load balancing) will stay connected to the initial two replicas, skewing the load profile among gRPC backends. Because of this, many developers use a smarter client (such as making use of gRPC’s client-side load balancing), force periodic reconnects at the server and/or client, or use service meshes to externalize the problem. We’ll discuss load balancing in more detail in Chapters 4 and 5.
```
- ipvs loadbalancing
```
To create a basic load balancer with two equally weighted destinations, run ipvsadm -A -t <address> -s <mode>. -A, -E, and -D are used to add, edit, and delete virtual services, respectively. The lowercase counterparts, -a, -e, and -d, are used to add, edit, and delete host backends, respectively:

# ipvsadm -A -t 1.1.1.1:80 -s lc
# ipvsadm -a -t 1.1.1.1:80 -r 2.2.2.2 -m -w 100
# ipvsadm -a -t 1.1.1.1:80 -r 3.3.3.3 -m -w 100

```
```
ICMP is a layer 4 protocol, like TCP and UDP. Kubernetes services support TCP and UDP, but not ICMP. This means that pings to a Kubernetes service will always fail.
```
- docker -> runC(low lvl) runtime
          -> containerD(high lvl) runtimes, background service that allows for daemonless
          ```
          containerd-shim is the component that allows for daemonless containers. It resides as the parent of the container’s process to facilitate a few things. containerd allows the runtimes, i.e., runC, to exit after it starts the container. This way, we do not need the long-running runtime processes for containers. 
          ```
- docker cli -> docker engine api -> containerd-shim -> runC start container then exit
- cgroups control access to resources in the kernel for our containers, and namespaces are individual slices of resources to manage separately from the root namespaces, i.e., the host.
- In short, a cgroup is a Linux kernel feature that limits, accounts for, and isolates resource usage. 
- A cgroup controls how much of a resource a container can use, while namespaces control what processes inside the container can see.
- 
```
Create a host with a root network namespace.

Create a new network namespace.

Create a veth pair.

Move one side of the veth pair into a new network namespace.

Address side of the veth pair inside the new network namespace.

Create a bridge interface.

Address the bridge interface.

Attach the bridge to the host interface.

Attach one side of the veth pair to the bridge interface.

Profit.
```
```
$ echo 1 > /proc/sys/net/ipv4/ip_forward
$ sudo ip netns add net1
$ sudo ip link add veth0 type veth peer name veth1
$ sudo ip link set veth1 netns net1
$ sudo ip link add veth0 type veth peer name veth1
$ sudo ip netns exec net1 ip addr add 192.168.1.101/24 dev veth1
$ sudo ip netns exec net1 ip link set dev veth1 up
$ sudo ip link add br0 type bridge
$ sudo ip link set dev br0 up
$ sudo ip link set enp0s3 master br0
$ sudo ip link set veth0 master br0
$ sudo ip netns exec net1  ip route add default via 192.168.1.100
```
- CNI is the software interface between the container runtime and the network implementation.
- A CNI plugin is responsible for associating a network interface to the container network namespace and making any necessary changes to the host. It then assigns the IP to the interface and sets up the routes for it.
- The container runtime uses a configuration file for the host’s network information; in Kubernetes, the Kubelet also uses this configuration file. The CNI and container runtime communicate with each other and apply commands to the configured CNI plugin.
- Nodes and pods must have L3 connectivity in this IP address space. Recall from Chapter 1 that in L3, the Internet layer, connectivity means packets with an IP address can route to a host with that IP address. It is important to note that the ability to deliver packets is more fundamental than creating connections (an L4 concept). In L4, firewalls may choose to allow connections from host A to B but reject connections initiating from host B to A
- In an island cluster setup, as shown in Figure 4-4, nodes have L3 connectivity with the broader network, but pods do not. Traffic to and from pods must pass through some form of proxy, through nodes. Most often, this is achieved by iptables source NAT on a pod’s packets leaving the node. This setup, called masquerading, uses SNAT to rewrite packet sources from the pod’s IP address to the node’s IP address (refer to Chapter 2 for a refresher on SNAT). In other words, packets appear to be “from” the node, rather than the pod.
- The kube-controller-manager runs most individual Kubernetes controllers in one binary and one process, where most Kubernetes logic lives. 
- At a high level, the Kubelet is responsible for managing any pods scheduled to the node and providing status updates for the node and pods on it. However, the Kubelet primarily acts as a coordinator for other software on the node. The Kubelet manages a container networking implementation (via the CNI) and a container runtime (via the CRI).
- Once the container exists, the Kubelet makes an ADD call to the CNI, which tells the CNI plugin to create the pod network. We will cover the interface and plugins in our next section.
- The Kubelet performs several types of health checks for individual containers in a pod: liveness probes (livenessProbe), readiness probes (readinessProbe), and startup probes (startupProbe). The Kubelet (and, by extension, the node itself) must be able to connect to all containers running on that node in order to perform any HTTP health checks.
- The Endpoints/EndpointsSlice controllers also react to failing readiness probes. If a pod’s readiness probe fails, the pod’s IP address will not be in the endpoint object, and the service will not route traffic to it. 
- In Figure 4-6, we can see how Kubernetes (or the runtime, as the CNI project refers to container orchestrators) invokes CNI plugin operations by executing binaries. Kubernetes supplies any configuration for the command in JSON to stdin and receives the command’s output in JSON through stdout. CNI plugins frequently have very simple binaries, which act as a wrapper for Kubernetes to call, while the binary makes an HTTP or RPC API call to a persistent backend. 
- The CNI plugin has two primary responsibilities: allocate and assign unique IP addresses for pods and ensure that routes exist within Kubernetes to each pod IP address. 
- There are two broad categories of CNI network models: flat networks and overlay networks. In a flat network, the CNI driver uses IP addresses from the cluster’s network, which typically requires many IP addresses to be available to the cluster. In an overlay network, the CNI driver creates a secondary network within Kubernetes, which uses the cluster’s network (called the underlay network) to send packets. Overlay networks create a virtual network within the cluster. In an overlay network, the CNI plugin encapsulates packets. 
- Overlay networks add substantial complexity and do not allow hosts on the cluster network to connect directly to pods. However, overlay networks allow the cluster network to be much smaller, as only the nodes must be assigned IP addresses on that network.
- kube-proxy is another per-node daemon in Kubernetes, like Kubelet. kube-proxy provides basic load balancing functionality within the cluster. It implements services and relies on Endpoints/EndpointSlices
- Most types of services have an IP address for the service, called the cluster IP address, which is not routable outside the cluster. kube-proxy is responsible for routing requests to a service’s cluster IP address to healthy pods. kube-proxy is by far the most common implementation for Kubernetes services, but there are alternatives to kube-proxy, such as a replacement mode Cilium.
- labelSelector vs labelExpression
```
matchExpressions:
  - key: colour
    operator: In
    values:
      - purple
  - key: shape
    operator: In
    values:
      - square
matchExpressions:
  - key: colour
    operator: NotIn
    values:
      - red
      - orange
      - yellow
  - key: shape
    operator: Exists
```
- NetworkPolicy rules act as exceptions, or an “allow list,” to the default block caused by selecting pods in a policy. Rules cannot block access; they can only add access. If multiple NetworkPolicy objects select a pod, all rules in each of those NetworkPolicy objects apply.
- A NetworkPolicyPeer has four ways for rules to refer to networked entities: ipBlock, namespaceSelector, podSelector, and a combination.
- ipBlock is useful for allowing traffic to and from external systems. It can be used only on its own in a rule, without a namespaceSelector or podSelector. ipBlock contains a CIDR and an optional except CIDR. The except CIDR will exclude a sub-CIDR (it must be within the CIDR range).
- KubeDNS was used in earlier versions of Kubernetes. KubeDNS had several containers within a single pod: kube-dns, dnsmasq, and sidecar. The kube-dns container watches the Kubernetes API and serves DNS records based on the Kubernetes DNS specification, dnsmasq provides caching and stub domain support, and sidecar provides metrics and health checks. Versions of Kubernetes after 1.13 now use the separate component CoreDNS.
- There are several differences between CoreDNS and KubeDNS:
For simplicity, CoreDNS runs as a single container.
CoreDNS is a Go process that replicates and enhances the functionality of Kube-DNS.
CoreDNS is designed to be a general-purpose DNS server that is backward compatible with Kubernetes, and its extendable plugins can do more than is provided in the Kubernetes DNS specification.
```
There are four options for dnsPolicy that significantly affect how DNS resolutions work inside a pod:

Default
The pod inherits the name resolution configuration from the node that the pods run on.

ClusterFirst
Any DNS query that does not match the cluster domain suffix, such as www.kubernetes.io, is sent to the upstream name server inherited from the node.

ClusterFirstWithHostNet
For pods running with hostNetwork, admins should set the DNS policy to ClusterFirstWithHostNet.

None
All DNS settings use the dnsConfig field in the pod spec.
```
- Sts
```
StatefulSets are a workload abstraction in Kubernetes to manage pods like you would a deployment. Unlike a deployment, StatefulSets add the following features for applications that require them:

Stable, unique network identifiers

Stable, persistent storage

Ordered, graceful deployment and scaling

Ordered, automated rolling updates
```
- Endpoints help identify what pods are running for the service it powers. Endpoints are created and managed by services. We will discuss services on their own later, to avoid covering too many new things at once. For now, let’s just say that a service contains a standard label selector (introduced in Chapter 4), which defines which pods are in the endpoints.
- Each endpoint contains a list of ports (which apply to all pods) and two lists of addresses: ready and unready.
- In a typical cluster, Kubernetes runs kube-proxy on every node. kube-proxy is responsible for the per-node portions of making services work, by handling routing and outbound load balancing to all the pods in a service. To do that, kube-proxy watches all endpoints in the cluster so it knows all applicable pods that all services should route to.
- Now, imagine we have a big cluster, with thousands of nodes, and tens of thousands of pods. That means thousands of kube-proxies are watching endpoints. When an address changes in an Endpoints object (say, from a rolling update, scale up, eviction, health-check failure, or any number of reasons), the updated Endpoints object is pushed to all listening kube-proxies. It is made worse by the number of pods, since more pods means larger Endpoints objects, and more frequent changes. This eventually becomes a strain on etcd, the Kubernetes API server, and the network itself. 
- With “regular” endpoints, a Kubernetes service creates one endpoint for all pods in the service. A service creates multiple endpoint slices, each containing a subset of pods; Figure 5-2 depicts this subset. The union of all endpoint slices for a service contains all pods in the service. This way, an IP address change (due to a new pod, a deleted pod, or a pod’s health changing) will result in a much smaller data transfer to watchers. 
- The endpoint slice controller mirrors endpoints to endpoint slice, to allow systems to continue writing endpoints while treating endpoint slice as the source of truth. 
- Endpoints and endpoint slices are important to understand because they identify the pods responsible for the services, no matter the type deployed.
- ExternalTrafficPolicy indicates how a service will route external traffic to either node-local or cluster-wide endpoints. Local preserves the client source IP and avoids a second hop for LoadBalancer and NodePort type services but risks potentially imbalanced traffic spreading. Cluster obscures the client source IP and may cause a second hop to another node but should have good overall load-spreading. A Cluster value means that for each worker node, the kube-proxy iptable rules are set up to route the traffic to the pods backing the service anywhere in the cluster,
- A Local value means the kube-proxy iptable rules are set up only on the worker nodes with relevant pods running to route the traffic local to the worker node. Using Local also allows application developers to preserve the source IP of the user request. If you set externalTrafficPolicy to the value Local, kube-proxy will proxy requests only to node-local endpoints and will not forward traffic to other nodes. 
- kube-proxy is responsible for making the ClusterIP service address route to all applicable pods. In “normal” configurations, kube-proxy performs L4 load balancing, which may not be sufficient. For example, older pods may see more load, due to accumulating more long-lived connections from clients. Or, a few clients making many requests may cause the load to be distributed unevenly.
- 
```
View the VETH pair and match with the pod.

View the network namespace and match with the pod.

Verify the PIDs on the node and match the pods.

Match services with iptables rules.
```
```
1. exec into pod: ip r, ip a -> eth0@if5
2. exec into node: ip a -> veth45d1f3e8@if5, ip netns list
3. exec into node: ip netns pid
 cni-ec37f6e4-a1b5-9bc9-b324-59d612edb4d4 -> pids: 4737, 4738
4. ps aux | grep 4737 -> app and pause container
5. exec into node: iptables -t nat -L | grep svcip
6. sudo iptables -L KUBE-SVC-RILCPVIYRE4LAVGU -t nat -> return list of ep chains and their lb probabilities
7. sudo iptables -L KUBE-SEP-3GD5EGYMCJCG45CY -t nat -> return this endpoint's backing pod ip
```
- When ClusterIP is set to None, the service does not support any load balancing functionality. Instead, it only provisions an Endpoints object and points the service DNS record at all pods that are selected and ready.
- Headless services allow developers to deploy multiple copies of a pod in a deployment. Instead of a single IP address returned, like with the ClusterIP service, all the IP addresses of the endpoint are returned in the query. It then is up to the client to pick which one to use. 
- LoadBalancer service exposes services external to the cluster network. They combine the NodePort service behavior with an external integration, such as a cloud provider’s load balancer. 
- 
```
Exact
Matches the specific path and only the given path (including trailing / or lack thereof).

Prefix
Matches all paths that start with the given path.

ImplementationSpecific
Allows for custom semantics from the current ingress controller.

```
- virtual hosting
```
  rules:
  - host: a.example.com
    http:
      paths:
      - pathType: Prefix
        path: "/"
        backend:
          service:
            name: service-a
            port:
              number: 80
  - host: b.example.com
    http:
      paths:
      - pathType: Prefix
        path: "/"
        backend:
          service:
            name: service-b
            port:
              number: 80
```
- ingress tls
```
The TLS config references a Kubernetes secret by name, in .spec.tls.[*].secretName. Ingress controllers expect the TLS certificate and key to be provided in .data."tls.crt" and .data."tls.key" respectively

apiVersion: v1
kind: Secret
metadata:
  name: demo-tls
type: kubernetes.io/tls
data:
  tls.crt: cert, encoded in base64
  tls.key: key, encoded in base64
```
- We mentioned earlier that ingress is simply a spec, and drastically different implementations exist. It’s possible to use multiple ingress controllers in a single cluster, using IngressClass settings. An ingress class represents an ingress controller, and therefore a specific ingress implementation.
- Ingress only supports HTTP(S) requests, which is insufficient if your service uses a different protocol (e.g., most databases use their own protocols). Some ingress controllers, such as the NGINX ingress controller, do support TCP and UDP, but this is not the norm.
- 
```
The following are rules for the main route table:

The main route table cannot be deleted.

A gateway route table cannot be set as the main.

The main route table can be replaced with a custom route table.

Admins can add, remove, and modify routes in the main route table.

The local route is the most specific.

Subnets can explicitly associate with the main route table.

There are route tables with specific goals in mind; here is a list of them and a description of how they are different:

Main route table
This route table automatically controls routing for all subnets that are not explicitly associated with any other route table.

Custom route table
A route table network engineers create and customize for specific application traffic flow.

Edge association
A routing table to route inbound VPC traffic to an edge appliance.

Subnet route table
A route table that’s associated with a subnet.

Gateway route table
A route table that’s associated with an internet gateway or virtual private gateway.

Each route table has several components that determine its responsibilities:

Route table association
The association between a route table and a subnet, internet gateway, or virtual private gateway.

Rules
A list of routing entries that define the table; each rule has a destination, target, status, and propagated flag.

Destination
The range of IP addresses where you want traffic to go (destination CIDR).

Target
The gateway, network interface, or connection through which to send the destination traffic; for example, an internet gateway.

Status
The state of a route in the route table: active or blackhole. The blackhole state indicates that the route’s target isn’t available.

Propagation
Route propagation allows a virtual private gateway to automatically propagate routes to the route tables. This flag lets you know if it was added via propagation.

Local route
A default route for communication within the VPC.




```
- A common use case for ENIs is the creation of management networks that are accessible only from a corporate network. AWS services like Amazon WorkSpaces use ENIs to allow access to the customer VPC and the AWS-managed VPC. Lambda can reach resources, like databases, inside a VPC by provisioning and attaching to an ENI.
```
ENIs have these properties:

Primary private IPv4 address

Secondary private IPv4 addresses

One elastic IP (EIP) address per private IPv4 address

One public IPv4 address, which can be auto-assigned to the network interface for eth0 when you launch an instance

One or more IPv6 addresses

One or more security groups

MAC address

Source/destination check flag

Description
```
- An EIP address is a property of an ENI and is associated with an instance by updating the ENI attached to the instance. The advantage of associating an EIP with the ENI rather than directly to the instance is that all the network interface attributes move from one instance to another in a single step.
- Security groups operate at the instance or network interface level and act as a firewall for those devices associated with them. 
- Security groups are stateful, so if traffic is allowed on the inbound flow, the outgoing traffic is allowed. 
```
The following is a list of components of security group rules:

Source/destination
Source (inbound rules) or destination (outbound rules) of the traffic inspected:

Individual or range of IPv4 or IPv6 addresses

Another security group

Other ENIs, gateways, or interfaces

Protocol
Which layer 4 protocol being filtered, 6 (TCP), 17 (UDP), and 1 (ICMP)

Port range
Specific ports for the protocol being filtered

Description
User-defined field to inform others of the intent of the security group
```
- each subnet has a default NACL associated with it and is bounded to an AZ, unlike the security group. Filter rules must be defined explicitly in both directions. The default rules are quite permissive, allowing all traffic in both directions. Users can define their own NACLs to use with a subnet for an added security layer if the security group is too open. 
```
Here are the components of an NACL:

Rule number
Rules are evaluated starting with the lowest numbered rule.

Type
The type of traffic, such as SSH or HTTP.

Protocol
Any protocol that has a standard protocol number: TCP/UDP or ALL.

Port range
The listening port or port range for the traffic. For example, 80 for HTTP traffic.

Source
Inbound rules only; the CIDR range source of the traffic.

Destination
Outbound rules only; the destination for the traffic.

Allow/Deny
Whether to allow or deny the specified traffic.
```
- Network address translation (NAT) devices are used when instances inside a VPC require internet connectivity, but network connections should not be made directly to instances. 
- The main route table has two rules, a local route for the inter-VPC and a route for 0.0.0.0/0 with a target of the NAT GW ID. The private subnet’s database servers will route traffic to the internet via that NAT GW rule in their route tables.

Pods and instances in EKS will need to egress the VPC, so a NAT device must be deployed. 
- The internet gateway is an AWS-managed service and device in the VPC network that allows connectivity to the internet for all devices in the VPC. Here are the steps to ensure access to or from the internet in a VPC:

Deploy and attach an IGW to the VPC.

Define a route in the subnet’s route table that directs internet-bound traffic to the IGW.

Verify NACLs and security group rules allow the traffic to flow to and from instances.
```

Chapter 6. Kubernetes and Cloud Networking
The use of the cloud and its service offerings has grown tremendously: 77% of enterprises are using the public cloud in some capacity, and 81% can innovate more quickly with the public cloud than on-premise. With the popularity and innovation available in the cloud, it follows that running Kubernetes in the cloud is a logical step. Each major cloud provider has its own managed service offering for Kubernetes using its cloud network services.

In this chapter, we’ll explore the network services offered by the major cloud providers AWS, Azure, and GCP with a focus on how they affect the networking needed to run a Kubernetes cluster inside that specific cloud. All the providers also have a CNI project that makes running a Kubernetes cluster smoother from an integration perspective with their cloud network APIs, so an exploration of the CNIs is warranted. After reading this chapter, administrators will understand how cloud providers implement their managed Kubernetes on top of their cloud network services.

Amazon Web Services
Amazon Web Services (AWS) has grown its cloud service offerings from Simple Queue Service (SQS) and Simple Storage Service (S3) to well over 200 services. Gartner Research positions AWS in the Leaders quadrant of its 2020 Magic Quadrant for Cloud Infrastructure & Platform Services. Many services are built atop of other foundational services. For example, Lambda uses S3 for code storage and DynamoDB for metadata. AWS CodeCommit uses S3 for code storage. EC2, S3, and CloudWatch are integrated into the Amazon Elastic MapReduce service, creating a managed data platform. The AWS networking services are no different. Advanced services such as peering and endpoints use building blocks from core networking fundamentals. Understanding those fundamentals, which enable AWS to build a comprehensive Kubernetes service, is needed for administrators and developers.

AWS Network Services
AWS has many services that allow users to extend and secure their cloud networks. Amazon Elastic Kubernetes Service (EKS) makes extensive use of those network components available in the AWS cloud. We will discuss the basics of AWS networking components and how they are related to deploying an EKS cluster network. This section will also discuss several other open source tools that make managing a cluster and application deployments simple. The first is eksctl, a CLI tool that deploys and manages EKS clusters. As we have seen from previous chapters, there are many components needed to run a cluster, and that is also true on the AWS network. eksctl will deploy all the components in AWS for cluster and network administrators. Then, we will discuss the AWS VPC CNI, which allows the cluster to use native AWS services to scale pods and manage their IP address space. Finally, we will examine the AWS Application Load Balancer ingress controller, which automates, manages, and simplifies deployments of application load balancers and ingresses for developers running applications on the AWS network.

Virtual private cloud
The basis of the AWS network is the virtual private cloud (VPC). A majority of AWS resources will work inside the VPC. VPC networking is an isolated virtual network defined by administrators for only their account and its resources. In Figure 6-1, we can see a VPC defined with a single CIDR of 192.168.0.0/16. All resources inside the VPC will use that range for private IP addresses. AWS is constantly enhancing its service offerings; now, network administrators can use multiple nonoverlapping CIDRs in a VPC. The pod IP addresses will also come from VPC CIDR and host IP addressing; more on that in “AWS VPC CNI”. A VPC is set up per AWS region; you can have multiple VPCs per region, but a VPC is defined in only one.

neku 0601
Figure 6-1. AWS virtual private cloud
Region and availability zones
Resources are defined by boundaries in AWS, such as global, region, or availability zone. AWS networking comprises multiple regions; each AWS region consists of multiple isolated and physically separate availability zones (AZs) within a geographic area. An AZ can contain multiple data centers, as shown in Figure 6-2. Some regions can contain six AZs, while newer regions could contain only two. Each AZ is directly connected to the others but is isolated from the failures of another AZ. This design is important to understand for multiple reasons: high availability, load balancing, and subnets are all affected. In one region a load balancer will route traffic over multiple AZs, which have separate subnets and thus enable HA for applications.

neku 0602
Figure 6-2. AWS region network layout
NOTE
An up-to-date list of AWS regions and AZs is available in the documentation.

Subnet
A VPC is compromised of multiple subnets from the CIDR range and deployed to a single AZ. Applications that require high availability should run in multiple AZs and be load balanced with any one of the load balancers available, as discussed in “Region and availability zones”.

A subnet is public if the routing table has a route to an internet gateway. In Figure 6-3, there are three public and private subnets. Private subnets have no direct route to the internet. These subnets are for internal network traffic, such as databases. The size of your VPC CIDR range and the number of public and private subnets are a design consideration when deploying your network architecture. Recent improvements to VPC like allowing multiple CIDR ranges help lessen the ramification of poor design choices, since now network engineers can simply add another CIDR range to a provisioned VPC.

Subnet
Figure 6-3. VPC subnets
Let’s discuss those components that help define if a subnet is public or private.

Routing tables
Each subnet has exactly one route table associated with it. If one is not explicitly associated with it, the main route table is the default one. Network connectivity issues can manifest here; developers deploying applications inside a VPC must know to manipulate route tables to ensure traffic flows where it’s intended.

The following are rules for the main route table:

The main route table cannot be deleted.

A gateway route table cannot be set as the main.

The main route table can be replaced with a custom route table.

Admins can add, remove, and modify routes in the main route table.

The local route is the most specific.

Subnets can explicitly associate with the main route table.

There are route tables with specific goals in mind; here is a list of them and a description of how they are different:

Main route table
This route table automatically controls routing for all subnets that are not explicitly associated with any other route table.

Custom route table
A route table network engineers create and customize for specific application traffic flow.

Edge association
A routing table to route inbound VPC traffic to an edge appliance.

Subnet route table
A route table that’s associated with a subnet.

Gateway route table
A route table that’s associated with an internet gateway or virtual private gateway.

Each route table has several components that determine its responsibilities:

Route table association
The association between a route table and a subnet, internet gateway, or virtual private gateway.

Rules
A list of routing entries that define the table; each rule has a destination, target, status, and propagated flag.

Destination
The range of IP addresses where you want traffic to go (destination CIDR).

Target
The gateway, network interface, or connection through which to send the destination traffic; for example, an internet gateway.

Status
The state of a route in the route table: active or blackhole. The blackhole state indicates that the route’s target isn’t available.

Propagation
Route propagation allows a virtual private gateway to automatically propagate routes to the route tables. This flag lets you know if it was added via propagation.

Local route
A default route for communication within the VPC.

In Figure 6-4, there are two routes in the route table. Any traffic destined for 11.0.0.0/16 stays on the local network inside the VPC. All other traffic, 0.0.0.0/0, goes to the internet gateway, igw-f43c4690, making it a public subnet.

Route
Figure 6-4. Route table
Elastic network interface
An elastic network interface (ENI) is a logical networking component in a VPC that is equivalent to a virtual network card. ENIs contain an IP address, for the instance, and they are elastic in the sense that they can be associated and disassociated to an instance while retaining its properties.

ENIs have these properties:

Primary private IPv4 address

Secondary private IPv4 addresses

One elastic IP (EIP) address per private IPv4 address

One public IPv4 address, which can be auto-assigned to the network interface for eth0 when you launch an instance

One or more IPv6 addresses

One or more security groups

MAC address

Source/destination check flag

Description

A common use case for ENIs is the creation of management networks that are accessible only from a corporate network. AWS services like Amazon WorkSpaces use ENIs to allow access to the customer VPC and the AWS-managed VPC. Lambda can reach resources, like databases, inside a VPC by provisioning and attaching to an ENI.

Later in the section we will see how the AWS VPC CNI uses and manages ENIs along with IP addresses for pods.

Elastic IP address
An EIP address is a static public IPv4 address used for dynamic network addressing in the AWS cloud. An EIP is associated with any instance or network interface in any VPC. With an EIP, application developers can mask an instance’s failures by remapping the address to another instance.

An EIP address is a property of an ENI and is associated with an instance by updating the ENI attached to the instance. The advantage of associating an EIP with the ENI rather than directly to the instance is that all the network interface attributes move from one instance to another in a single step.

The following rules apply:

An EIP address can be associated with either a single instance or a network interface at a time.

An EIP address can migrate from one instance or network interface to another.

There is a (soft) limit of five EIP addresses.

IPv6 is not supported.

Services like NAT and internet gateway use EIPs for consistency between the AZ. Other gateway services like a bastion can benefit from using an EIP. Subnets can automatically assign public IP addresses to EC2 instances, but that address could change; using an EIP would prevent that.

Security controls
There are two fundamental security controls within AWS networking: security groups and network access control lists (NACLs). In our experience, lots of issues arise from misconfigured security groups and NACLs. Developers and network engineers need to understand the differences between the two and the impacts of changes on them.

Security groups
Security groups operate at the instance or network interface level and act as a firewall for those devices associated with them. A security group is a group of network devices that require common network access to each other and other devices on the network. In Figure 6-5 ,we can see that security works across AZs. Security groups have two tables, for inbound and outbound traffic flow. Security groups are stateful, so if traffic is allowed on the inbound flow, the outgoing traffic is allowed. Each security group has a list of rules that define the filter for traffic. Each rule is evaluated before a forwarding decision is made.

Security Group
Figure 6-5. Security group
The following is a list of components of security group rules:

Source/destination
Source (inbound rules) or destination (outbound rules) of the traffic inspected:

Individual or range of IPv4 or IPv6 addresses

Another security group

Other ENIs, gateways, or interfaces

Protocol
Which layer 4 protocol being filtered, 6 (TCP), 17 (UDP), and 1 (ICMP)

Port range
Specific ports for the protocol being filtered

Description
User-defined field to inform others of the intent of the security group

Security groups are similar to the Kubernetes network policies we discussed in earlier chapters. They are a fundamental network technology and should always be used to secure your instances in the AWS VPC. EKS deploys several security groups for communication between the AWS-managed data plane and your worker nodes.

Network access control lists
Network access control lists operate similarly to how they do in other firewalls so that network engineers will be familiar with them. In Figure 6-6, you can see each subnet has a default NACL associated with it and is bounded to an AZ, unlike the security group. Filter rules must be defined explicitly in both directions. The default rules are quite permissive, allowing all traffic in both directions. Users can define their own NACLs to use with a subnet for an added security layer if the security group is too open. By default, custom NACLs deny all traffic, and therefore add rules when deployed; otherwise, instances will lose connectivity.

Here are the components of an NACL:

Rule number
Rules are evaluated starting with the lowest numbered rule.

Type
The type of traffic, such as SSH or HTTP.

Protocol
Any protocol that has a standard protocol number: TCP/UDP or ALL.

Port range
The listening port or port range for the traffic. For example, 80 for HTTP traffic.

Source
Inbound rules only; the CIDR range source of the traffic.

Destination
Outbound rules only; the destination for the traffic.

Allow/Deny
Whether to allow or deny the specified traffic.

NACL
Figure 6-6. NACL
NACLs add an extra layer of security for subnets that may protect from lack or misconfiguration of security groups.

Table 6-1 summarizes the fundamental differences between security groups and network ACLs.

Table 6-1. Security and NACL comparison table
Security group	Network ACL
Operates at the instance level.

Operates at the subnet level.

Supports allow rules only.

Supports allow rules and deny rules.

Stateful: Return traffic is automatically allowed, regardless of any rules.

Stateless: Return traffic must be explicitly allowed by rules.

All rules are evaluated before a forwarding decision is made.

Rules are processed in order, starting with the lowest numbered rule.

Applies to an instance or network interface.

All rules apply to all instances in the subnets that it’s associated with.

It is crucial to understand the differences between NACL and security groups. Network connectivity issues often arise due to a security group not allowing traffic on a specific port or someone not adding an outbound rule on an NACL. When troubleshooting issues with AWS networking, developers and network engineers alike should add checking these components to their troubleshooting list.

All the components we have discussed thus far manage traffic flow inside the VPC. The following services manage traffic into the VPC from client requests and ultimately to applications running inside a Kubernetes cluster: network address translation devices, internet gateway, and load balancers. Let’s dig into those a little more.

Network address translation devices
Network address translation (NAT) devices are used when instances inside a VPC require internet connectivity, but network connections should not be made directly to instances. Examples of instances that should run behind a NAT device are database instances or other middleware needed to run applications.

In AWS, network engineers have several options for running NAT devices. They can manage their own NAT devices deployed as EC2 instances or use the AWS Managed Service NAT gateway (NAT GW). Both require public subnets deployed in multiple AZs for high availability and EIP. A restriction of a NAT GW is that the IP address of it cannot change after you deploy it. Also, that IP address will be the source IP address used to communicate with the internet gateway.

In the VPC route table in Figure 6-7, we can see how the two route tables exist to establish a connection to the internet. The main route table has two rules, a local route for the inter-VPC and a route for 0.0.0.0/0 with a target of the NAT GW ID. The private subnet’s database servers will route traffic to the internet via that NAT GW rule in their route tables.

Pods and instances in EKS will need to egress the VPC, so a NAT device must be deployed. Your choice of NAT device will depend on the operational overhead, cost, or availability requirements for your network design.

net-int
Figure 6-7. VPC routing diagram
Internet gateway
The internet gateway is an AWS-managed service and device in the VPC network that allows connectivity to the internet for all devices in the VPC. Here are the steps to ensure access to or from the internet in a VPC:

Deploy and attach an IGW to the VPC.

Define a route in the subnet’s route table that directs internet-bound traffic to the IGW.

Verify NACLs and security group rules allow the traffic to flow to and from instances.

All of this is shown in the VPC routing from Figure 6-7. We see the IGW deploy for the VPC, a custom route table setup that routes all traffic, 0.0.0.0/0, to the IGW. The web instances have an IPv4 internet routable address, 198.51.100.1-3.

Elastic load balancers
Now that traffic flows from the internet and clients can request access to applications running inside a VPC, we will need to scale and distribute the load for requests. AWS has several options for developers, depending on the type of application load and network traffic requirements needed.

The elastic load balancer has four options:

Classic
A classic load balancer provides fundamental load balancing of EC2 instances. It operates at the request and the connection level. Classic load balancers are limited in functionality and are not to be used with containers.

Application
Application load balancers are layer 7 aware. Traffic routing is made with request-specific information like HTTP headers or HTTP paths. The application load balancer is used with the application load balancer controller. The ALB controller allows devs to automate the deployment and ALB without using the console or API, instead just a few YAML lines.

Network
The network load balancer operates at layer 4. Traffic can be routed based on incoming TCP/UDP ports to individual hosts running services on that port. The network load balancer also allows admins to deploy then with an EIP, a feature unique to the network load balancer.

Gateway
The gateway load balancer manages traffic for appliances at the VPC level. Such network devices like deep packet inspection or proxies can be used with a gateway load balancer. The gateway load balancer is added here to complete the AWS service offering but is not used within the EKS ecosystem.
```
```
Rule
(ALB only) The rules that you define for your listener determine how the load balancer routes all requests to the targets in the target groups.

Listener
Checks for requests from clients. They support HTTP and HTTPS on ports 1–65535.

Target
An EC2 instance, IP address, pods, or lambda running application code.

Target Group
Used to route requests to a registered target.

Health Check
Test to ensure targets are still able to accept client requests.
```
```
The rule will have an action type to determine how to handle the request:

authenticate-cognito
(HTTPS listeners) Use Amazon Cognito to authenticate users.

authenticate-oidc
(HTTPS listeners) Use an identity provider that is compliant with OpenID Connect to authenticate users.

fixed-response
Returns a custom HTTP response.

forward
Forward requests to the specified target groups.

redirect
Redirect requests from one URL to another.
```
- Workers nodes in EKS come in three flavors: EKS-managed node groups, self-managed nodes, and AWS Fargate. 
- The Amazon EKS control plane creates up to four cross-account elastic network interfaces in your VPC for each cluster. EKS uses two VPCs, one for the Kubernetes control plane, including the Kubernetes API masters, API loadbalancer, and etcd depending on the networking model; the other is the customer VPC where the EKS worker nodes run your pods. As part of the boot process for the EC2 instance, the Kubelet is started. The node’s Kubelet reaches out to the Kubernetes cluster endpoint to register the node. It connects either to the public endpoint outside the VPC or to the private endpoint within the VPC. kubectl commands reach out to the API endpoint in the EKS VPC. End users reach applications running in the customer VPC.
- The public endpoint is the default option; it is public because the load balancer for the API endpoint is on a public subnet, as shown in Figure 6-10. Kubernetes API requests that originate from within the cluster’s VPC, like when the worker node reaches out to the control plane, leave the customer VPC, but not the Amazon network. One security concern to consider when using a public endpoint is that the API endpoints are on a public subnet and reachable on the internet.
- eksctl defaults to creating a cluster with the following default parameters:
```
An autogenerated cluster name

Two m5.large worker nodes

Use of the official AWS EKS AMI

Us-west-2 default AWS region

A dedicated VPC

A dedicated VPC with 192.168.0.0/16 CIDR range, eksctl will create by default 8 /19 subnets: three private, three public, and two reserved subnets. eksctl will also deploy a NAT GW that allows for communication of nodes placed in private subnets and an internet gateway to enable access for needed container images and communication to the Amazon S3 and Amazon ECR APIs.

Two security groups are set up for the EKS cluster:

Ingress inter node group SG
Allows nodes to communicate with each other on all ports

Control plane security group
Allows communication between the control plane and worker node groups
```
```
One node group containing two m5.large nodes is the default for eksctl. But how many pods can that node run? AWS has a formula based on the node type and the number of interfaces and IP addresses it can support. That formula is as follows:

(Number of network interfaces for the instance type ×
(the number of IP addresses per network interface - 1)) + 2
Using the preceding formula and the default instance size on eksctl, an m5.large can support a maximum of 29 pods.
```
- aws cni/ipamd run as daemonset, kubelet setting to cni, talks to node daemon for network setup.  kubelet invoke cni api(add/del) -> gRPC -> cni -> ipamd
```
A customer VPC with a subnet 10.200.1.0/24 in AWS gives us 250 usable addresses in this subnet. There are two nodes in our cluster. In EKS, the managed nodes run with the AWS CNI as a daemon set. In our example, each node has only one pod running, with a secondary IP address on the ENI, 10.200.1.6 and 10.200.1.8, for each pod. When a worker node first joins the cluster, there is only one ENI and all its addresses in the ENI. When pod three gets scheduled to node 1, ipamd assigns the IP address to the ENI for that pod. In this case, 10.200.1.7 is the same thing on node 2 with pod 4.
```
- https://github.com/aws/amazon-vpc-cni-k8s/blob/master/docs/cni-proposal.md
```
For each Kubernetes node (ec2 instance), create multiple elastic network interfaces (ENIs) and allocate their secondary IP addresses.
For each pod, pick a free secondary IP address, assign it to the pod, wire host and pod networking stack to allow:
Pod to Pod on a single host communication
Pod to Pod on different hosts communication
Pod to other AWS service communication
Pod to on-premises data center communication
Pod to internet communication
```
- An elastic network interface is a virtual network interface that you can attach to an instance in a VPC. When the ENI is attached to an instance, a corresponding interface is created. The primary ENI IP address is automatically assigned to the interface. All secondary addresses remain unassigned and it's up to the host owner as to how to configure them.
- How traffic reaches nodes and pods is affected by one of two modes the ALB can run:
```
Instance mode
Ingress traffic starts at the ALB and reaches the Kubernetes nodes through each service’s NodePort. This means that services referenced from ingress resources must be exposed by type:NodePort to be reached by the ALB.

IP mode
Ingress traffic starts at the ALB and reaches directly to the Kubernetes pods. CNIs must support a directly accessible pod IP address via secondary IP addresses on ENI.
```
```
The AWS Load Balancer Controller manages AWS Elastic Load Balancers for a Kubernetes cluster. The controller provisions the following resources.

An AWS Application Load Balancer (ALB) when you create a Kubernetes Ingress.

An AWS Network Load Balancer (NLB) when you create a Kubernetes service of type LoadBalancer. In the past, the Kubernetes network load balancer was used for instance targets, but the AWS Load balancer Controller was used for IP targets. With the AWS Load Balancer Controller version 2.3.0 or later, you can create NLBs using either target type. 
```
- The AWS Load Balancer Controller controller was formerly named the AWS ALB Ingress Controller. https://github.com/kubernetes-sigs/aws-load-balancer-controller
