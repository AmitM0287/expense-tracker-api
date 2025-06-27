# Dockerfile

# Stage 1: base image with Python deps + ffmpeg
FROM amkrstudio/amkr-studio-base:master-0db125d-v1 AS base

# Stage 2: final runtime image
FROM python:3.12.10-slim AS final

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Only copy minimal binaries needed
COPY --from=base /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=base /usr/local/bin/gunicorn /usr/local/bin/

# Copy project code
COPY . .

# Collect static files (if using whitenoise or storing in S3)
RUN python manage.py collectstatic --noinput

# Expose default app port
EXPOSE 8000

# Run using gunicorn
CMD ["gunicorn", "amkrstudio.wsgi:application", "--bind", "0.0.0.0:8000"]
