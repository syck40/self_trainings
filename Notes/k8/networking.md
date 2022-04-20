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
