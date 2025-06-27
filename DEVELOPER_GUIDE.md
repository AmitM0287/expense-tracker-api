# 🧑‍💻 AMKR STUDIO API – Developer Guide

---

## 🐳 Docker Commands

### 1️⃣ Build & Push the Docker Base Image

- Build the base image using `Docker.base`:
```bash
docker build -f Dockerfile.base -t amkrstudio/amkr-studio-api-base:master-600432f-v108 .
```

- Push the base image to Docker Hub:
```bash
docker push amkrstudio/amkr-studio-api-base:master-600432f-v108
```

---

### 2️⃣ Build & Push the Docker API Image

- Build the API image using `Dockerfile`:
```bash
docker build -f Dockerfile -t amkrstudio/amkr-studio-api:master-600432f-v108 .
```

- Push the image to Docker Hub:
```bash
docker push amkrstudio/amkr-studio-api:master-600432f-v108
```

---

## ☸️ Kubernetes Commands

### 3️⃣ Apply ConfigMap & Restart

- Apply the ConfigMap:
```bash
kubectl apply -f amkr-studio-cm.yaml
```

- Restart the deployment:
```bash
kubectl rollout restart deployment amkr-studio-api
```

---

### 4️⃣ Cluster Management

```bash
kubectl get services                # List all services
kubectl get deployments            # List all deployments
kubectl get pods                   # List all pods
kubectl get pods -o wide           # Get detailed pod info
kubectl get pods | grep amkr       # Filter pods by name
kubectl logs <pod-name>            # View logs of a pod
kubectl describe pod <pod-name>    # Detailed info of a pod
kubectl delete deployment <name>   # Delete deployment
kubectl delete service <name>      # Delete service
kubectl exec -it <pg-pod> -- bash  # Enter PostgreSQL pod
```

---

## 🐘 PostgreSQL Commands (Inside Pod)

```bash
kubectl exec -it <pg-pod> -- psql -U amitmanna
```

Inside psql:
```sql
\l         -- List databases
\du        -- List users
```

Take DB backup (from local):
```bash
pg_dump -U amitmanna -d amkr-studio -f ~/Desktop/amkr-studio.sql
```

Copy dump to pod:
```bash
kubectl cp ~/Desktop/amkr-studio.sql <pg-pod>:/tmp/amkr-studio.sql
```

---

## 🔐 Utility Commands

### Base64 Encode/Decode

```bash
echo -n "test@1234" | base64          # Encode
echo "dGVzdEAxMjM0" | base64 --decode # Decode
```

---

## 🧰 Git Commands

### Manage Remote URLs

- View existing remotes:
```bash
git remote -v
```

- Remove existing origin:
```bash
git remote remove origin
```

- Add a new origin:
```bash
git remote add origin https://github.com/newuser/newrepo.git
```

- Push to new origin:
```bash
git push -u origin main
```

> Replace `main` with `master` if applicable.

---

## ✅ Best Practices

- ✅ Use `--no-cache-dir` in all `pip install`
- ✅ Keep Docker base image minimal (Python + ffmpeg only)
- ✅ Always use `.dockerignore` for faster and cleaner builds
- ✅ Tag Docker images with traceable versions (`master-<commit_id>-v108`)
- ✅ Use meaningful commit messages and environment-specific ConfigMaps

---

