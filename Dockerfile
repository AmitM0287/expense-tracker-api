# Stage 1: base image with Python deps + ffmpeg + packages
FROM amitkrishnadev/amkrstudio:amkr-studio-api-base-master-v1.0.8 AS base

# Copy entire Django project (excluding what's in .dockerignore)
COPY . .

# Expose Gunicorn port
EXPOSE 8000

# Run Gunicorn
CMD ["gunicorn", "amkrstudio.wsgi:application", "--bind", "0.0.0.0:8000"]
