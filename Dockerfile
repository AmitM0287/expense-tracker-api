# Stage 1: base image with Python deps + ffmpeg + packages
FROM amkrstudio/amkr-studio-api-base:master-6aad30f-v1 AS base

# Stage 2: final runtime image
FROM python:3.12.10-slim-bullseye AS final

# Python environment settings
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy required Python libs & binaries from base
COPY --from=base /usr/local/lib/python3.12 /usr/local/lib/python3.12
COPY --from=base /usr/local/bin/gunicorn /usr/local/bin/gunicorn

# Copy media folder (if needed at runtime)
COPY --from=base /app/media /app/media

# Copy Django app code
COPY . .

# Ensure necessary folders exist
RUN mkdir -p /app/media /app/static

# Collect static files (optional, if using whitenoise or S3)
RUN python manage.py collectstatic --noinput

# Expose the Gunicorn port
EXPOSE 8000

# Start Gunicorn server
CMD ["gunicorn", "amkrstudio.wsgi:application", "--bind", "0.0.0.0:8000"]
