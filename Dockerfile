# First stage: build the application
FROM amkrstudio/amkr-studio-base:master-0db125d-v1 as build

# Set the working directory inside the container
WORKDIR /app

# Copy the rest of your Django project files into the container
COPY . /app/

# Install any additional dependencies if needed
RUN pip install --no-cache-dir -r requirements.txt

# Second stage: create the final image
FROM python:3.12.0-alpine as final

# Install build dependencies
RUN apk add --no-cache gcc musl-dev linux-headers

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Copy only the necessary files from the build stage
COPY --from=build /app /app

# Install uWSGI
RUN pip install --no-cache-dir uwsgi

# Expose the port the application runs on (replace 8000 with your actual port if needed)
EXPOSE 8000

# Start uWSGI server
CMD ["uwsgi", "--http", "0.0.0.0:8000", "--module", "amkrstudio.wsgi:application", "--master", "--processes", "4", "--threads", "2"]
