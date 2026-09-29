# Container Deployment Guide

## Docker Build and Run

```bash
docker build -t fast-fatoora:latest .
docker run -d -p 8000:8000 --name fatoora-service fast-fatoora:latest
```

## Health Check
Visit http://localhost:8000/docs to inspect interactive Swagger documentation.