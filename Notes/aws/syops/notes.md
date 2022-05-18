- [misc](#misc)
- [1. Monitoring/Logging/Remediation](#1-monitoringloggingremediation)
  - [logs](#logs)
  - [alarms](#alarms)
  - [notification](#notification)
  - [remediation](#remediation)
  - [eventbridge](#eventbridge)
  - [aws config](#aws-config)
- [2. Reliability (5 - 7)](#2-reliability-5---7)
  - [caching](#caching)
  - [rds](#rds)
  - [loose coupling](#loose-coupling)
    - [r53 routing](#r53-routing)
- [3. Deployment/Automation](#3-deploymentautomation)
- [4. Security](#4-security)
- [5. Networking](#5-networking)
- [6. Cost](#6-cost)

```
55 questions
170 min
20 min per lab
```
# misc
- aws --generate-cli-skeleton > file.json, aws --cli-input-json file.json
- aws --query is clientside --filter is serverside

# 1. Monitoring/Logging/Remediation
## logs
- cloudwatch logs, region scoped replicated through region, fault tolerant, durable
- request service/feature to push, not pulled
- need log groups, log groups -> log streams -> log records
- cloudtrail, region scope audit logs, success/failure, mgmt events
- cw logs insights, sql-like query, set alarm, 
- cloudtrail insights, use existing events, no query
- direct s3 export, cli tail, 
- subscription filter(deliver to another service) lambda function, kinesis stream/data firehose
- data firehost, region scope, streaming pipeline buffer and batch, destination to s3/redshift/elasticsearch, http endpoint, datadog
- log group -> s3 -> iam role trust identify data firehose as principle and write permission
- cwl to firehose, iam trust identify cwl as principle and write permission to firehose
- cwl agent for custom metrics, need iam and connectivity to cw endpoint via interfaace endpoint or internet
- aws ssm send-command --document-name "" --targets [{key:value}] --parameters '{'action': 'install', 'name':'AmazonCloudWatchAgent'}'
## alarms
- period: length of time to evaluate , 1 metric data point
- evaluation period, number of data points to evaluate when determining
- datapoints to alarm: number of data points within evaluation that must be breaching to cause alarm, does not have to be consecutive.
- evaluation range: number of points retrived by cw for alrm evaluation
- missing can be configured as missing/notbreaching/breaching/ignore
- actions: sns/ec2 actions/auto scaling/ssm opsitem
## notification
- sns forward to http/httpsendpoint(jira)
- email
- kinesis data firehose
- sqs
- lambda
- mobile push
- sms
## remediation
- ec2 action, any metric
- statuscheckfailed_system only -> ec2 action recover will attempt to move
- sns topic can trigger custom endpoint, api->lambda, lambda
- ec2 status check: system reachability(host os)/instance reachability(guest os)
- ebs volume status
- rds db instance status
## eventbridge
- used to call cloudwatch events, region scoped, default eventbus or custom eventbus
- src and target, able to replay or DLQ queue for when failed
- src can be  cloudtrail api/guardduty/service health events/scheduled/custom events.
- filter match property -> forward to apigateway/ec2action/lambda/sns
## aws config
- region scope, config streams, partial coverage
- capture config changes, create snapshots
- aws config rules: create lambda custom rule for evaluation or aws-managed rules to remediation
- manual or automated remediation, aws ssm automation document

# 2. Reliability (5 - 7)
- scalability, increase resource, not necessarily automation
- elasticity, increase AND decrease, alway automated
- scaling plan(avail, balanced, cost)
- customer create rules and limits, apply that to scaling strategy
- launch template, template with all param filled out
- predictive scaling mode: forcase only(ml model) or forecase and scale(create action)
- pre-launch instances
- max-cap
## caching
- cloudfront, elb/s3 can use caching with cloudfront
- cf, global scoped, deployed at edge location not region, cache both reads and writes.
- elastic-cache, memcached or redis for traffic spike in same az
- dynamodb, true kv store
- memcached, az scoped, memory, volatile, all endpoint writable
- redis, while az scoped, persistent with replication, 1 write endpoint, sharding option
## rds
- same region read replicas can be promoted, it becomes its own primary
- read replicas have its own endpoint
- xregion read replicas, not for sql server engine
- multi az, primary and standby, both writen to syncronisly.  DNS change for fail-over
- active/passive mode, don't get multiple endpoint for multi az mode
- read replica, seperate from multi-az mode, has unique endpoints, 5 RR per primary
- a read replica can be a primary and muti-az even tho it's being replicated to
- aurora more sophiscated but less engine available.  No read replica only aurora replicas
- aurora fail-over much faster
- aurora server-less, auto launch in new az
- single endpoint, round robin loadbalancing, 15 rr per primary, 5 rds rr per primary
- instead of multi-az mode, it's not a active/passive, more throughput
- promotional tier to rank promotion order
## loose coupling
- 1 ec2, 1 r53(cname), 1 static public ip through elastic ip, ip will change with instance restart due to dhcp, eip is region scoped not az scoped can be reassgined.
- r53(alias record to elb dns) -> alb, multi ec2 in multi az
- multi region, r53(a record) to multiple region's alb dns with 1 as primary, health check against elb 1, fail-over record return 2nd region.  Active/passive, 2ndary does not serve traffic
- latency based routing via r53.  Active/active, both region serve traffic with s3 bucket static fail-over
- r53 health checks, check endpoint before you send traffic.
- r53 endpoint healthcheck: choose endpoint(ip/host/domain), protocol(http/https/ping), port(single)
- r53 other healthcheck: 
- r53 cloudwatch alarm healthcheck
- elb healthcheck: check ec2(clb/nlb/alb/glb), check ip(nlb/alb/glb), check lambda(alb)
- elb/asg/fsx/rds single vs multi az
- efs is region scoped, can only access through mount point which is az scopped(elastic network interfaces within subnet of your az), ecs/eks/lambda can mount efs 
### r53 routing
- r53 simple round robin, equal weights, multivalue answer routing = choose 8 healthy at random
- weighted routing to backend alb endpoint
- latency-based routing
- failover(active/passive) routing
- alias record, apex record has to be a record(ip), aws allows alias record(pointer for resource) for alb/s3/cloudfront/apigateway/vpcendpoint
# 3. Deployment/Automation

# 4. Security

# 5. Networking

# 6. Cost