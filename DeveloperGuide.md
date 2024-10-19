
# Developer Guide

### Docker Commands

**1. Build & Push the Docker Base Image:**
- Build the base image using the specified Dockerfile.
  ```bash
  docker build -f Dockerfile.base -t <username>/amkr-studio-base:master-<commit_id>-<version> .
  ```
  Example:
  ```bash
  docker build -f Dockerfile.base -t amkrstudio/amkr-studio-base:master-0db125d-v1 .
  ```
- Push the built base image to Docker Hub.
  ```bash
  docker push <username>/amkr-studio-base:master-<commit_id>-<version>
  ```
  Example:
  ```bash
  docker push amkrstudio/amkr-studio-base:master-0db125d-v1
  ```

**2. Build & Push the Docker Image:**
- Build the API image using the specified Dockerfile.
  ```bash
  docker build -f Dockerfile -t <username>/amkr-studio-api:master-<commit_id>-<version> .
  ```
  Example:
  ```bash
  docker build -f Dockerfile -t amkrstudio/amkr-studio-api:master-0db125d-v1 .
  ```
- Push the built API image to Docker Hub.
  ```bash
  docker push docker.io/amkrstudio/amkr-studio-api:master-0db125d-v1
  ```

### Kubernetes Commands

**3. Apply the ConfigMap YAML:**
- Apply the ConfigMap to the cluster.
  ```bash
  kubectl apply -f amkr-studio-cm.yaml
  ```
- Restart the deployment to apply changes.
  ```bash
  kubectl rollout restart deployment amkr-studio-api
  ```

**4. Get Cluster Information:**
- List services in the cluster.
  ```bash
  kubectl get svc
  ```
- List pods, filtering by name.
  ```bash
  kubectl get po | grep <name>
  ```
- List all pods.
  ```bash
  kubectl get pods
  ```
- View logs for a specific pod.
  ```bash
  kubectl logs amkr-studio-api-7765458fc4-rsvj6
  ```
- Describe a specific pod for detailed information.
  ```bash
  kubectl describe pod amkr-studio-api-7765458fc4-rsvj6
  ```
- List all services.
  ```bash
  kubectl get services
  ```
- List all deployments.
  ```bash
  kubectl get deployments
  ```
- Delete a specific service.
  ```bash
  kubectl delete service amkr-studio-api-service
  ```
- Delete a specific deployment.
  ```bash
  kubectl delete deployment amkr-studio-api
  ```
- Access the bash shell of a PostgreSQL pod.
  ```bash
  kubectl exec -it postgres-<pod-name> -- bash
  ```

### PostgreSQL Commands

**5. PostgreSQL Commands:**
- Connect to the PostgreSQL pod and access the psql shell.
  ```bash
  kubectl exec -it <postgres-pod-name> -- psql -U amitmanna
  ```
- List all databases.
  ```sql
  \l
  ```
- List all users.
  ```sql
  \du
  ```
- Take a backup of the database as a .sql file.
  ```bash
  pg_dump -U amitmanna -d amkr-studio -f ~/Desktop/amkr-studio.sql
  ```
- Copy the backup file from the local machine to the pod.
  ```bash
  kubectl cp ~/Desktop/amkr-studio.sql postgres-6f4dc46bb9-z9gdj:/tmp/amkr-studio.sql
  ```
