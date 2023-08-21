# CI-CD-Jenkins-ArgoCD

Manifest Repository [CI-CD-Jenkins-ArgoCD-repo](https://github.com/Teebra/CI-CD-Jenkins-ArgoCD-repo)

## SSH into EC2 instance, you can follow these steps:

Give permission to SSH KEY:
```
chmod 400 <SHH-KEY>
```
Eg: chmod 400 MyEC2CO.pem

Pass SSH Key to Instance:
```
ssh -i <SSH-KEY> <EC2-OS>@<IP-ADDRESS>
```
Eg: chmod 400 MyEC2CO.pem

## To install Python 3 and pip on Ubuntu, you can follow these steps:

```
sudo apt-get update
```

Install Python 3:

```
sudo apt-get install -y python3 python3-dev python3-venv
```

Install pip for Python 3:

```
sudo apt-get install -y python3-pip
```

Verify Installation:

```
python3 --version
pip3 --version
```

## To Install Docker on Ubuntu, you can follow these steps:

```
sudo apt install -y docker.io
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker $USER
sudo chmod 666 /var/run/docker.sock
```

## To install Kubectl on Ubuntu, you can follow these steps:

```
sudo snap install kubectl --classic
```

## To install Minikube:

Installation:

```
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
```

minikube start:

```
minikube start
```

## Configure a Sonar Server locally
```
apt install unzip
adduser sonarqube
wget https://binaries.sonarsource.com/Distribution/sonarqube/sonarqube-10.1.0.73491.zip
unzip *
chmod -R 755 /home/sonarqube/sonarqube-10.1.0.73491.zip
chown -R sonarqube:sonarqube /home/sonarqube/sonarqube-10.1.0.73491.zip
cd sonarqube-10.1.0.73491.zip/bin/linux-x86-64/
./sonar.sh start
```
Now you can access the SonarQube Server on http://<ip-address>:9000

### SonarQube (Login):
User: ```admin```
pass: ```admin```


