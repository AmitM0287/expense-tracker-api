### 🧑🏻‍💻 AMKR STUDIO API – Developer Guide ###

---

### 🐳 Docker Commands ###

### Build & Push the Docker Image [linux/amd64, linux/arm64] ###

- Docker buildx command to build and push the Base Image to registry:
```bash
docker buildx build --no-cache --platform linux/amd64,linux/arm64 -f Dockerfile.base -t amitkrishnadev/amkrstudio:amkr-studio-api-base-master-v1.0.8 --push .
```

- Docker buildx command to build and push the Final image to registry:
```bash
docker buildx build --no-cache --platform linux/amd64,linux/arm64 -f Dockerfile -t amitkrishnadev/amkrstudio:amkr-studio-api-master-v1.0.8 --push .
```

- Docker Push command to push image to Docker Hub:
```bash
docker push amitkrishnadev/amkrstudio:amitkrishnadev/amkrstudio:amkr-studio-api-master-v1.0.8
```

- Docker Pull command to pull image from Docker Hub:
```bash
docker pull amitkrishnadev/amkrstudio:amitkrishnadev/amkrstudio:amkr-studio-api-master-v1.0.8
```

- Docker Run command to run image locally:

- Ensure the container is automatically removed once it stops [--rm]
```bash
docker run --rm --env-file .env -p 8000:8000 --name amkrstudio-api amitkrishnadev/amkrstudio:amkr-studio-api-master-v1.0.8
```

- Ensure the container is detached, will not get automatically removed once it stops [-d]
```bash
docker run -d --env-file .env -p 8000:8000 --name amkrstudio-api amitkrishnadev/amkrstudio:amkr-studio-api-master-v1.0.8
```

- Detached + Manual Cleanup [safer for prod]
```bash
docker rm -f amkrstudio-api
```

- Check platform of image

- To confirm your image supports ARM:
```bash
docker buildx imagetools inspect amitkrishnadev/amkrstudio:amkr-studio-api-master-v1.0.8
```

---

### 🐘 PostgreSQL Commands ###

- Inside Pod:
```bash
kubectl exec -it podname -- psql -U dbuser
```

- Inside psql:
```sql
\l         -- List databases
\du        -- List users
```

- Take DB backup from local:
```bash
pg_dump -U dbuser -d amkrstudio -f ~/Downloads/amkrstudio.sql
```

- Copy dump to pod:
```bash
kubectl cp ~/Downloads/amkrstudio.sql podname:/tmp/amkrstudio.sql
```

---

### 🔐 Utility Commands ###

### Base64 Encode/Decode ###

- Encode Base64:
```bash
echo -n "test@1234" | base64
```

- Decode Base64:
```bash
echo "dGVzdEAxMjM0" | base64 --decode
```

---

### 🧰 Git Commands ###

### Manage Remote URLs ###

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
git remote add origin https://github.com/amitkrishnadev/amkr-studio-api.git
```

- Push to new origin:
```bash
git push -u origin master
```

---

### ✅ Best Practices ###

- ✅ Use `--no-cache-dir` in all `pip install`
- ✅ Keep Docker base image minimal (Python + ffmpeg only)
- ✅ Always use `.dockerignore` for faster and cleaner builds
- ✅ Tag Docker images with traceable versions (`master-<commit_id>-v108`)
- ✅ Use meaningful commit messages and environment-specific ConfigMaps

---
