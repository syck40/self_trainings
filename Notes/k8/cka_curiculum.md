- [1. Cluster Architecture, Installation & Configuration	25 %](#1-cluster-architecture-installation--configuration25-)
  - [1.1. Manage role-based Access Control (RBAC)](#11-manage-role-based-access-control-rbac)
  - [1.2. Use Kubeadm to Install a Basic Cluster](#12-use-kubeadm-to-install-a-basic-cluster)
- [2. Workloads & Scheduling	15 %](#2-workloads--scheduling15-)
  - [2.1. Workloads](#21-workloads)
  - [2.2. Scheduling](#22-scheduling)
- [3. Services & Networking	20 %](#3-services--networking20-)
- [4. Storage	10 %](#4-storage10-)
- [5. Troubleshooting	30 %](#5-troubleshooting30-)

https://github.com/bmuschko/cka-study-guide

# 1. Cluster Architecture, Installation & Configuration	25 %
## 1.1. Manage role-based Access Control (RBAC)
```
Create the ServiceAccount named api-access in a new namespace called apps.

Create a ClusterRole with the name api-clusterrole, and the ClusterRoleBinding named api-clusterrolebinding. Map the ServiceAccount from the previous step to the API resources Pods with the operations watch, list, get.

Create a Pod named operator with the image nginx:1.21.1 in the namespace apps. Expose the container port 80. Assign the ServiceAccount api-access to the Pod. Create another Pod named disposable with the image nginx:1.21.1 in the namespace rm. Do not assign the ServiceAccount to the Pod.

Open an interactive shell to the Pod named operator. Use the command line tool curl to make an API call to list the Pods in the namespace rm. What response do you expect? Use the command line tool curl to make an API call to delete the Pod disposable in the namespace rm. Does the response differ from the first call? You can find information about how to interact with Pods using the API via HTTP in the reference guide.
```
## 1.2. Use Kubeadm to Install a Basic Cluster
```
Navigate to the directory app-a/ch02/upgrade-version of the checked-out GitHub repository bmuschko/cka-study-guide. Start up the VMs running the cluster using the command vagrant up. Upgrade all nodes of the cluster from Kubernetes 1.20.4 to 1.21.2. The cluster consists of a single control plane node named k8s-control-plane, and three worker nodes named worker-1, worker-2, and worker-3. Once done, shut down the cluster using vagrant destroy -f.

Prerequisite: This exercise requires the installation of the tools Vagrant and VirtualBox.

Navigate to the directory app-a/ch02/backup-restore-etcd of the checked-out GitHub repository bmuschko/cka-study-guide. Start up the VMs running the cluster using the command vagrant up. The cluster consists of a single control plane node named k8s-control-plane, and two worker nodes named worker-1, and worker-2. The etcdctl tool has been preinstalled on the node k8s-control-plane. Back up etcd to the snapshot file /opt/etcd.bak. Restore etcd from the snapshot file. Use the data directory /var/bak. Once done, shut down the cluster using vagrant destroy -f.
```
# 2. Workloads & Scheduling	15 %
## 2.1. Workloads
```
Create a Deployment named nginx that uses the image nginx:1.17.0. Set 2 replicas to begin with.

Scale the Deployment to 7 replicas using the scale command. Ensure that the correct number of Pod exists.

Create a Horizontal Pod Autoscaler named nginx-hpa for the Deployment with an average utilization of CPU to 65% and an average utilization of memory to 1Gi. Set the minimum number of replicas to 3 and the maximum number of replicas to 20.

Update the Pod template of the Deployment to use the image nginx:1.21.1. Make sure that the changes are recorded. Inspect the revision history. How many revisions should be rendered? Roll back to the first revision.

Create a new Secret named basic-auth of type kubernetes.io/basic-auth. Assign the key-value pairs username=super and password=my-s8cr3t. Mount the Secret as a Volume with the path /etc/secret and read-only permissions to the Pods controlled by the Deployment.
```
## 2.2. Scheduling
```
Write a manifest for a new Pod named ingress-controller with a single container that uses the image bitnami/nginx-ingress-controller:1.0.0. For the container, set the resource request to 256Mi for memory and 1 CPU. Set the resource limits to 1024Mi for memory and 2.5 CPU.

Using the manifest, schedule the Pod on a cluster with 3 nodes. Once created, identify the node that runs the Pod. Write the node name to the file node.txt.

Create the directory named manifests. Within the directory, create two files: pod.yaml and configmap.yaml. The pod.yaml should define a Pod named nginx with the image nginx:1.21.1. The configmap.yaml defines a ConfigMap named logs-config with the key-value pair dir=/etc/logs/traffic.log. Create both objects with a single, declarative command.

Modify the ConfigMap manifest by changing the value of the key dir to /etc/logs/traffic-log.txt. Apply the changes. Delete both objects with a single declarative command.

Use Kustomize to set a common namespace t012 for the resource file pod.yaml. The file pod.yaml defines the Pod named nginx with the image nginx:1.21.1 without a namespace. Run the Kustomize command that renders the transformed manifest on the console.
```
# 3. Services & Networking	20 %
```
In the namespace external, create a Deployment named nginx with the image nginx for 3 replicas. The container should expose the port 80. Within the same namespace, create a Service of type LoadBalancer. The Service should route traffic to the Pods managed by the Deployment.

From your local machine (outside of the cluster), make a call to the LoadBalancer using wget or curl. Identify which of the Pods received the traffic by looking at the logs.

Change the Service type to ClusterIP. Make a call to the Service using wget or curl so that the Pods receive the traffic.

Create an Ingress named incoming in the namespace external. Define the path type Prefix to the path / to the Service from the previous step. The Ingress should be able to handle any incoming HTTP traffic.

Make a call to the Ingress using wget or curl from your local machine. Verify that the Pods receive traffic.

Create a new Service of type ClusterIP named echoserver in the namespace external. The selected and to be created Pod should use the image k8s.gcr.io/echoserver:1.10 on port 8080. Add a new rule to the existing Ingress to route traffic to the echoserver Service with the path /echo and type Exact.

Make a call to the Service using wget or curl from your local machine so that the echoserver can be reached.

Create a rewrite rule for the CoreDNS configuration that allows referencing a Service using the cluster domain cka.example.com. Ensure that the custom CoreDNS configuration takes effect.

Make a call to the nginx Service using wget or curl from a temporary Pod in a new namespace called hello with the appropriate hostname.
```
# 4. Storage	10 %
```
Create a PersistentVolume named logs-pv that maps to the hostPath /tmp/logs. The access mode should be ReadWriteOnce and ReadOnlyMany. Provision a storage capacity of 2Gi. Assign the reclaim policy Delete and an empty string as the storage class. Ensure that the status of the PersistentVolume shows Available.

Create a PersistentVolumeClaim named logs-pvc. The access it uses is ReadWriteOnce. Request a capacity of 1Gi. Ensure that the status of the PersistentVolume shows Bound.

Mount the PersistentVolumeClaim in a Pod running the image nginx at the mount path /var/log/nginx.

Open an interactive shell to the container and create a new file named my-nginx.log in /var/log/nginx. Exit out of the Pod.

Delete the Pod and PersistentVolumeClaim. What happens to the PersistentVolume?

List the available storage classes and identify the default storage class. Note down the provisioner.

Create a new storage class named custom using the provisioner of the default storage class.

Create a PersistentVolumeClaim named custom-pvc. Request a capacity of 500Mi and declare the access mode ReadWriteOnce. Assign the storage class name custom.

The PersistentVolume should have been provisioned dynamically. Find out the name and write it to the file named pv-name.txt.

Delete the PersistentVolumeClaim. What happens to the PersistentVolume?
```
# 5. Troubleshooting	30 %
```
You are supposed to implement cluster-level logging with a sidecar container. Create a multi-container Pod named multi. The main application container named nginx should use the image nginx:1.21.6. The sidecar container named streaming uses the image busybox:1.35.0 and the arguments /bin/sh, -c, 'tail -n+1 -f /var/log/nginx/access.log'.

Define a Volume of type emptyDir for the Pod and mount it to the path /var/log/nginx for both containers.

Access the endpoint of the nginx service a couple of times using a wget or curl command. Inspect the logs of the sidecar container.

Create two Pods named stress-1 and stress-2. Define a container that uses the image polinux/stress:1.0.4 with the command stress and the arguments /bin/sh, -c, 'stress --vm 1 --vm-bytes $(shuf -i 20-200 -n 1)M --vm-hang 1'. Set the container memory resource limits and requests to 250Mi.

Use the data available through the metrics server to identify which of the Pods, stress-1 or stress-2, consumes the most memory. Write the name of the Pod to the file max-memory.txt.

Navigate to the directory app-a/ch07/troubleshooting-pod of the checked-out GitHub repository bmuschko/cka-study-guide. Follow the instructions in the file instructions.md for troubleshooting a faulty Pod setup.

Navigate to the directory app-a/ch07/troubleshooting-deployment of the checked-out GitHub repository bmuschko/cka-study-guide. Follow the instructions in the file instructions.md for troubleshooting a faulty Deployment setup.

Navigate to the directory app-a/ch07/troubleshooting-service of the checked-out GitHub repository bmuschko/cka-study-guide. Follow the instructions in the file instructions.md for troubleshooting a faulty Service setup.

Navigate to the directory app-a/ch07/troubleshooting-control-plane-node of the checked-out GitHub repository bmuschko/cka-study-guide. Follow the instructions in the file instructions.md for troubleshooting a faulty control plane node setup.

Prerequisite: This exercise requires the installation of the tools Vagrant and VirtualBox.

Navigate to the directory app-a/ch07/troubleshooting-worker-node of the checked-out GitHub repository bmuschko/cka-study-guide. Follow the instructions in the file instructions.md for troubleshooting a faulty worker node setup.

Prerequisite: This exercise requires the installation of the tools Vagrant and VirtualBox.
```
