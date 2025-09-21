# DockerProject

This project is a **Dockerized application** featuring two services:  
- A **Flask RESTful API** (`books-service`) that provides a JSON list of books.  
- A **PHP** (`website`) that fetches and displays this data.  

Docker Compose orchestrates these services for easy setup and management.

---

## 🚀 Prerequisites

Before running this project, ensure you have the following software installed on your system:

- **Docker**: The platform for developing, shipping, and running applications in containers.  
  [Download Docker Desktop](https://www.docker.com/get-started) from the official Docker website.  

---

## 🏃‍♀️ Getting Started

Follow these steps to set up and run the application locally.

### 1️. Clone the Repository

First, clone the project repository to your local machine:

```bash
git clone https://github.com/SultanSB/DockerProject.git
```

### 2. Build and Run the Containers
Navigate to the root directory of the cloned repository and execute the following command to build the Docker images and start the services:
```bash
docker compose up --build
```

### 3. Access the Application
Once the containers are successfully running, you can access the application components:

**Frontend Website**: Open your web browser and navigate to http://localhost:5000 to view the book list.
