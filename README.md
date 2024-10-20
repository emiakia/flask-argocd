# Hello World Flask Application with Docker

This repository contains a simple Hello World project built using Flask, which is packaged as a Docker image. The Docker image is hosted in a private GitHub Container Registry (GHCR) and will be deployed to a K3s Kubernetes cluster using Argo CD.

## Project Overview

The project demonstrates how to build and deploy a basic Python Flask application as a Docker image. The application responds with "Hello, World!" when accessed.

We will use GitHub Actions to build and push the Docker image to the GitHub Container Registry. Since the image is private, we will store the credentials in our Kubernetes cluster as a secret for authentication.

### Key Components
- **Flask**: A lightweight Python web framework.
- **Docker**: The application is containerized using Docker.
- **GitHub Container Registry (GHCR)**: The Docker image is stored in a private registry.
- **Kubernetes (K3s)**: A lightweight Kubernetes distribution used for deploying the application.
- **Argo CD**: A declarative, GitOps continuous delivery tool for Kubernetes.

## Prerequisites

Before deploying the application, make sure you have the following set up:
- A GitHub account with access to the repository.
- Docker installed and configured.
- A K3s cluster set up with access to `kubectl`.
- Argo CD installed in your Kubernetes cluster.

## Steps to Build and Deploy

### 1. Build and Push Docker Image to GitHub Container Registry

In this project, we use GitHub Actions to automate the build and push process for the Docker image. The `Dockerfile` is located in the root directory of the project.

The GitHub Action will:
- Build the Docker image from the source code.
- Tag the image with the appropriate version.
- Push the image to the private GitHub Container Registry (`ghcr.io/emiakia/flask-app`).

### 2. Create a Kubernetes Secret for GHCR Authentication

Since the image is private, Kubernetes needs a way to authenticate to the GitHub Container Registry. We will create a Docker registry secret in the K3s cluster.

Run the following command to create the secret in your Kubernetes cluster:

```bash
kubectl create secret docker-registry ghcr-secret \
  --docker-server=ghcr.io \
  --docker-username=emiakia \
  --docker-password=${{ secrets.GHT_TOKEN }} \
  --docker-email=emran.kia@gmail.com
```

This command creates a Kubernetes secret called ghcr-secret with the necessary authentication details to pull the private image from GitHub Container Registry.

### 3. Deploy the Flask Application Using Argo CD
Once the secret is created, apply the flask-argocd.yaml manifest file to deploy the Flask application. The manifest file contains the necessary configuration for Argo CD to manage the deployment.

To apply the manifest:
```bash
kubectl apply -f flask-argocd.yaml
```
Argo CD will monitor the repository and ensure that the application is deployed and kept in sync with the state defined in the flask-argocd.yaml file.

### 4. Access the Application
After the deployment is successful, the Flask application will be accessible via the service URL exposed by your Kubernetes cluster.

### Troubleshooting
Ensure that the secret is correctly created in the namespace where you are deploying the application.
Check the logs of the application pod if the image fails to pull, as this could indicate an issue with the secret or registry credentials.

### Conclusion
This repository demonstrates how to build, package, and deploy a simple Flask application using Docker, GitHub Container Registry, and Kubernetes. Argo CD ensures the deployment is automated and stays in sync with the repository.

