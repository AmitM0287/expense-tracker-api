# Use the base image
FROM yourusername/amkr-studio-base:latest AS final

# Set the working directory inside the container
WORKDIR /app

# Copy the rest of your Django project files into the container
COPY . /app/

# Expose the port the Django app runs on (replace 8000 with your actual port if needed)
EXPOSE 8000

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
