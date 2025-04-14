# Analytics-api

1. Download and Install Python3
2. Create venv
3. Install python packages
4. FastAPI Hello World
5. Docker Desktop and Compose
6. Production Dockerfile for FastAPI
7. Docker-based FastAPI Hello World

## Docker
- `docker build -t analytics-api -f Dockerfile.web .`
- `docker run analytics-api`

becomes
- `docker compose up --watch`
- `docker compose down` or `docker compose down -v`