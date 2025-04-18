

# Use the official Python image as a base
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose port 8000 (Django's default port)
EXPOSE 8000

# Set environment variable for Django settings
ENV DJANGO_SETTINGS_MODULE=projectname.settings


# Command to run the Django app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
