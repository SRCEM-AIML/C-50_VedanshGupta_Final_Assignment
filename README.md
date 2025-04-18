## 🚀 Features

### 🧩 Part 1: Flask Application

- Displays "Hello, World!" on the homepage
- Second route accepts user name and age via a form and returns a personalized greeting
- Basic error handling for invalid inputs

### 🧩 Part 2: Django Application

- Homepage displays a list of tasks from a database
- Admin panel allows creation, modification, and deletion of tasks
- Form on homepage to add new tasks dynamically

### 🐳 Part 3: Docker Compose Setup

- Flask and Django apps are containerized using Docker
- Docker Compose used to manage both containers
- Flask accessible on **port 5000**
- Django accessible on **port 8000**

---

## 🔧 Tech Stack

- Python 3.9
- Flask 2.x
- Django 3.2.x
- Docker & Docker Compose

---

## 📦 Project Structure

```
project-root/
├── flask_app/
│   ├── app.py
│   ├── templates/
│   ├── static/
│   ├── requirements.txt
│   └── Dockerfile
├── django_app/
│   ├── manage.py
│   ├── myapp/
│   ├── db.sqlite3
│   ├── requirements.txt
│   └── Dockerfile
└── docker-compose.yml
```

## ▶️ How to Run the Project

### Step 1: Install Docker and Docker Compose
Make sure Docker is installed on your system. You can verify by running:

```bash
docker --version
docker-compose --version
```

---

### Step 2: Build and Start the Containers

Navigate to the project root (where `docker-compose.yml` is located):

```bash
docker-compose up --build
```

This command will:
- Build images for both Flask and Django
- Start both containers

---

### Step 3: Access the Applications

- **Flask App:** [http://localhost:5000](http://localhost:5000)
- **Django App:** [http://localhost:8000](http://localhost:8000)
- **Django Admin Panel:** [http://localhost:8000/admin](http://localhost:8000/admin)

---

## 🔐 Django Admin Credentials

- **Username:** `admin`
- **Email:** `admin@example.com`
- **Password:** `Admin@2025`

---

## 📤 Deployment & Submission

- ✅ Project pushed to **GitHub**
- ✅ Docker images built and can be pushed to **Docker Hub**
- ✅ `assignment3_results` sheet contains GitHub and Docker Hub URLs

