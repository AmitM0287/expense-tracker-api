# Use the base image created from Dockerfile.base
FROM amkrstudio/amkr-studio-base:master-0db125d-v1

# Copy the rest of your Django project files into the container
COPY . /application/

# Expose the port the application runs on (replace 8000 with your actual port if needed)
EXPOSE 8000

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
