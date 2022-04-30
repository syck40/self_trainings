- all nodes
```
cat <<EOF | sudo tee /etc/modules-load.d/containerd.conf
overlay
br_netfilter
EOF

sudo modprobe overlay
sudo modprobe br_netfilter

cat <<EOF | sudo tee /etc/sysctl.d/99-kubernetes-cri.conf
net.bridge.bridge-nf-call-iptables = 1
net.ipv4.ip_forward = 1
net.bridge.bridge-nf-call-ip6tables = 1
EOF

sudo sysctl --system

sudo apt-get update && sudo apt-get install -y containerd

sudo mkdir -p /etc/containerd
sudo containerd config default | sudo tee /etc/containerd/config.toml

sudo systemctl restart containerd

sudo systemctl status containerd

sudo swapoff -a

sudo sed -i '/ swap / s/^\(.*\)$/#\1/g' /etc/fstab

sudo apt-get update && sudo apt-get install -y apt-transport-https curl

curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -

cat <<EOF | sudo tee /etc/apt/sources.list.d/kubernetes.list
deb https://apt.kubernetes.io/ kubernetes-xenial main
EOF

sudo apt-get update

sudo apt-get install -y kubelet=1.23.0-00 kubeadm=1.23.0-00 kubectl=1.23.0-00

sudo apt-mark hold kubelet kubeadm kubectl
```
- master
```
Initialize the Cluster

Initialize the Kubernetes cluster on the control plane node using kubeadm (Note: This is only performed on the Control Plane Node):
sudo kubeadm init --pod-network-cidr 192.168.0.0/16 --kubernetes-version 1.23.0
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config

Test access to cluster:
kubectl get nodes
Install the Calico Network Add-On

On the Control Plane Node, install Calico Networking:
kubectl apply -f https://docs.projectcalico.org/manifests/calico.yaml
Check status of the control plane node:
kubectl get nodes
Join the Worker Nodes to the Cluster

In the Control Plane Node, create the token and copy the kubeadm join command (NOTE:The join command can also be found in the output from kubeadm init command):
kubeadm token create --print-join-command
In both Worker Nodes, paste the kubeadm join command to join the cluster. Use sudo to run it as root:
sudo kubeadm join ...
In the Control Plane Node, view cluster status (Note: You may have to wait a few moments to allow all nodes to become ready):
kubectl get nodes
```
- `kubectl get pv --sort-by=.spec.capacity.storage`
- `kubectl get pods -n beebox-mobile --kubeconfig dev-k8s-config`
-  
```
kubectl apply -f https://raw.githubusercontent.com/ACloudGuru-Resources/content-cka-resources/master/metrics-server-components.yaml
```
- `kubectl get --raw /apis/metrics.k8s.io/`
- `kubectl -n beebox-mobile top po --sort-by=cpu`

- 
```
cat <<EOF | kubectl apply -f - 
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
  - name: nginx
    image: nginx:1.19.1
    ports:
    - containerPort: 80
    volumeMounts:
    - name: config-volume
      mountPath: /etc/nginx
    - name: htpasswd-volume
      mountPath: /etc/nginx/conf
  volumes:
  - name: config-volume
    configMap:
      name: nginx-config
  - name: htpasswd-volume
    secret:
      secretName: nginx-htpasswd
EOF
```
- vim, :set shiftwidth=1, Ctrl V, jjj to mark lines, 5>
- `kubectl set image deployment web-proj nginx=nginx:1.17 --record`
- `kubectl rollout history deployment web-proj`
- kube-controller-manager are static pods with yaml in /etc/kubernetes/manifests/etcd.yaml|kube-apiserver.yaml|kube-controller-manager.yaml|kube-scheduler.yaml
- user and group are not api resources, unlike service accounts which are used by processes.
- 3 ways of authentication -> x509/basic/bearer openID
- openssl x509 -req -in johndoe.csr -CA /etc/kubernetes/pki/ca.crt -CAkey \
/etc/kubernetes/pki/ca.key -CAcreateserial -out johndoe.crt -days 364
- clusterRole aggregationRule
- `kubectl set img deploy ng *=nginx:1.17` will trigger new deployment rollout history
- `kubectl rollout history deploy ng --revision=5` will show what changed
- `kubectl set env deploy ng --all env=prod` will also trigger new deployemnt rollout
- The option --from-env-file expects a file that contains environment variables in the format KEY=value separated by a new line. The key-value pairs follow typical naming conventions for environment variables e.g. the key is upper-cased, and individual words are separated by an underscore character.
- svc with label selector automatically create endpoints that points to pods, endpoint can be created manually with the same name as selectorless svc that points to an external static ip
- When container images are instantiated as containers, the container needs context - context to CPU, memory, and I/O resources. Pods provide the network and filesystem context for the containers within. The network is provided as the Pod’s virtual IP and the file system is mounted to the hosting node’s filesystem. Applications running in the container can interact with the file system as part of the Pod context. A container’s temporary filesystem is isolated from any other container or Pod and is not persisted beyond a Pod restart. 
- A Volume is a Kubernetes capability that persists data beyond a Pod restart. Essentially, a Volume is a directory that’s shareable between multiple containers of a Pod.
- Persistent Volumes are a specific category of the wider concept of Volumes.  The Persistent Volume is the resource that actually persists the data to an underlying physical storage. The Persistent Volume Claim represents the connecting resource between a Pod and a Persistent Volume responsible for requesting the storage. Finally, the Pod needs to claim the Persistent Volume and mount it to a directory path available to the containers running inside of the Pod.
- When you run kubectl logs, the kubelet receives the request, reads directly from the log file on the node, and returns the content to the client. The kubectl logs command only returns the latest log content, not the log entries that have already been archived.
- For system components that do not run in the container e.g. the kubelet and the container runtime, logs will be written to journald if systemd is available. If systemd is not available, system components write their log files to the directory /var/log with the file extension .log.
- .vimrc
```
set expandtab
set tabstop=2
set shiftwidth=2

expandtab: use spaces for tab
tabstop: amount of spaces used for tab
shiftwidth: amount of spaces used during indentation
```
- misc:
  - `usermod -aG wheel student`
- doc searches
  - kubeadm init -> creating a cluster
  - pv -> configure a pod to use... docs/tasks
