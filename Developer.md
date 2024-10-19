# Build & Push the Docker Base Image:
	docker build -f Dockerfile.base -t <username>/amkr-studio-base:master-<commit_id>-<version> .
-	docker build -f Dockerfile.base -t amkrstudio/amkr-studio-base:master-0db125d-v1 .
-	docker push amkrstudio/amkr-studio-base:master-0db125d-v1

# Build & Push the Docker Image:
	docker build -f Dockerfile -t <username>/amkr-studio-api:master-<commit_id>-<version> .
-	docker build -f Dockerfile -t amkrstudio/amkr-studio-api:master-0db125d-v1 .
-	docker push docker.io/amkrstudio/amkr-studio-api:master-0db125d-v1
