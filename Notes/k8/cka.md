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
