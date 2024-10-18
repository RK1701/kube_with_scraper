# kube_with_scraper

This project demonstrates how to set up and run a web scraper using Docker and Kubernetes.

## Prerequisites

- Docker installed
- Kubernetes (Minikube or any other cluster)
- `kubectl` command-line tool installed

## Docker Commands

### Build Docker Image

Navigate to your project directory and build the Docker image.

```bash
docker build -t your-image-name:tag .
```

Some Use full docker operations command

```bash
docker stop your-container-name

docker rm your-container-name
docker rmi your-images-name

docker images

docker system prune

```


## Deploy to Minikube

First check minikube is runnig or not

```bash
minikube status
```

If not run then start minikube
```bash
minikube start
```
Load the Docker image to Minikube
```bash
eval $(minikube docker-env)
docker build -t blog_scraper_image .
```
Apply the deployment
```bash
kubectl apply -f deployment.yaml
```
Check the status of the pods and logs:
```bash
kubectl get pods
kubectl logs <pod-name>
```
Now kubernates operations command
```bash
kubectl get pods

kubectl apply -f your-deployment-file.yml

kubectl describe deployment <deployment-name>

kubectl delete deployment <deployment-name>

kubectl get deployments

kubectl delete pods --all

kubectl logs your-pod-name

```


