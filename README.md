# Project Structure

Playdevops/
└── frontend/
├── public/
├── src/
├── .dockerignore
├── .env
├── package.json
├── package-lock.json
├── react-scripts
│
├── Dockerfile.frontend 👈 NEW (React build image)
│
├── nginx/
│ ├── Dockerfile 👈 NEW (Nginx image)
│ └── nginx.conf
│
└── docker-compose.yml 👈 optional but recommended

