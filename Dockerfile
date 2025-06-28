# Prebuilt Base Image
FROM amitkrishnadev/amkrstudio:amkr-studio-api-base-master-v1.0.8 AS base

# Copy project files
COPY . .

# Expose Gunicorn port
EXPOSE 8000

# Run the app with Gunicorn
CMD ["gunicorn", "amkrstudio.wsgi:application", "--bind", "0.0.0.0:8000"]
