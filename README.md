# PlayDevOps Project

A containerized full-stack application using React (frontend) and Nginx with Docker support.

---

# 📁 Project Structure

```text
playdevops/
│
└── frontend/
    ├── public/
    ├── src/
    ├── .dockerignore
    ├── .env
    ├── package.json
    ├── package-lock.json
    ├── node_modules/ (ignored in git)
    │
    ├── Dockerfile.frontend        # React build image
    │
    ├── nginx/
    │   ├── Dockerfile             # Nginx container image
    │   └── nginx.conf            # Nginx configuration
    │
    └── docker-compose.yml        # (optional but recommended)
