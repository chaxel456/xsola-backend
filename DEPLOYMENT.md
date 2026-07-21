# XSOLA Deployment Documentation

## Introduction

The XSOLA platform is deployed as a cloud-native application. The backend is hosted on **Render**, the PostgreSQL database is hosted on **Supabase**, the source code is managed with **GitHub**, and Docker is used to ensure a consistent runtime environment.

This deployment strategy provides:

- Automatic deployments
- High availability
- Secure environment variables
- Managed PostgreSQL
- Easy scaling
- Continuous Integration (CI)

---

# Production Architecture

```text
                GitHub Repository
                        │
                git push origin main
                        │
                        ▼
                  Render Build
                        │
         Install Dependencies
                        │
                        ▼
                 Start FastAPI
                        │
        ┌───────────────┴───────────────┐
        ▼                               ▼
   REST API                       MQTT Client
        │                               │
        ▼                               ▼
 Frontend                      MQTT Broker
        │                               │
        ▼                               ▼
   Administrator                   ESP32 Devices
        │
        ▼
 Supabase PostgreSQL
```

---

# Deployment Components

| Component | Service |
|------------|----------|
| Source Control | GitHub |
| Backend | Render |
| Database | Supabase PostgreSQL |
| API Documentation | FastAPI Swagger |
| IoT Communication | MQTT Broker |
| Payment Gateway | Paystack |

---

# Backend Deployment

Backend Framework

```
FastAPI
```

Production Server

```
Uvicorn
```

Deployment Platform

```
Render
```

Production URL

```
https://xsola-backend-7.onrender.com
```

Swagger

```
https://xsola-backend-7.onrender.com/docs
```

---

# Source Code

The source code is stored in GitHub.

Repository Structure

```text
xsola-backend/

├── app/
├── tests/
├── docs/
├── requirements.txt
├── Dockerfile
├── render.yaml
└── README.md
```

---

# Git Workflow

Clone repository

```bash
git clone https://github.com/username/xsola-backend.git
```

Create feature branch

```bash
git checkout -b feature/new-feature
```

Commit changes

```bash
git add .

git commit -m "Add new feature"
```

Push

```bash
git push origin feature/new-feature
```

Merge into main.

---

# Continuous Deployment

Whenever code is pushed to the **main** branch:

```text
Developer

↓

Git Commit

↓

GitHub

↓

Render

↓

Automatic Build

↓

Deploy

↓

Application Live
```

No manual deployment is required after setup.

---

# Render Configuration

Render automatically:

- Pulls latest code
- Creates build environment
- Installs dependencies
- Starts FastAPI
- Monitors application
- Restarts on failure

Typical Start Command

```bash
uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

---

# Docker

Docker ensures the application runs consistently across development and production.

Example Dockerfile

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn","app.main:app","--host","0.0.0.0","--port","10000"]
```

Benefits

- Reproducible builds
- Dependency isolation
- Easier deployment
- Portable runtime

---

# Supabase Database

Database

```
PostgreSQL
```

Hosted by

```
Supabase
```

Responsibilities

- Store users
- Store customers
- Store devices
- Store subscriptions
- Store payments
- Store telemetry
- Store notifications
- Store waitlist

---

# Database Connection

FastAPI connects using

```env
DATABASE_URL=
```

SQLAlchemy creates the database engine.

```text
FastAPI

↓

SQLAlchemy

↓

Supabase PostgreSQL
```

---

# Environment Variables

Render stores secrets securely.

Example

```env
DATABASE_URL=

SECRET_KEY=

ACCESS_TOKEN_EXPIRE_MINUTES=

ALGORITHM=

PAYSTACK_SECRET_KEY=

PAYSTACK_PUBLIC_KEY=

MQTT_BROKER=

MQTT_PORT=

MQTT_USERNAME=

MQTT_PASSWORD=

SUPABASE_URL=

SUPABASE_KEY=
```

These values should **never** be committed to GitHub.

---

# Build Process

```text
GitHub

↓

Render Clone

↓

Install Python

↓

Install Requirements

↓

Run Build

↓

Start Uvicorn

↓

Application Running
```

---

# Health Checks

Render periodically checks the application.

Endpoint

```http
GET /health
```

Expected Response

```json
{
    "status":"healthy"
}
```

If the health check fails repeatedly, Render restarts the service.

---

# Database Migrations

Alembic is used for schema changes.

Create migration

```bash
alembic revision --autogenerate -m "Create payments table"
```

Apply migration

```bash
alembic upgrade head
```

---

# Deployment Workflow

```text
Developer

↓

Code Changes

↓

Local Testing

↓

Git Commit

↓

GitHub Push

↓

Render Build

↓

Deploy

↓

Health Check

↓

Production Ready
```

---

# Rollback Strategy

If a deployment fails:

```text
Render

↓

Previous Successful Deployment

↓

Rollback

↓

Application Restored
```

---

# Logging

Render automatically captures:

- Server startup
- API requests
- Exceptions
- Build logs
- Runtime logs

Application logs should also include:

- Authentication events
- MQTT events
- Payment verification
- Scheduler execution
- Device activation

---

# Scaling

Current

```text
1 Web Service
1 PostgreSQL Database
```

Future

```text
Load Balancer

↓

Multiple Backend Instances

↓

Shared Database

↓

MQTT Cluster
```

---

# Security During Deployment

- HTTPS enabled
- Environment variables encrypted
- Secrets not committed
- JWT secret protected
- Database credentials hidden
- CORS configured
- Secure cookies (future)
- Regular dependency updates

---

# Monitoring

Production monitoring should include:

- API uptime
- CPU usage
- Memory usage
- Response times
- Database performance
- MQTT connectivity
- Error rates

---

# Disaster Recovery

Recommendations

- Daily database backups
- Source code in GitHub
- Versioned releases
- Infrastructure as Code
- Restore procedures documented

---

# Deployment Checklist

Before each production release:

- All tests pass
- Environment variables configured
- Database migrations applied
- API documentation updated
- Swagger accessible
- Health endpoint working
- MQTT broker reachable
- Paystack keys verified
- Logs reviewed
- Backup completed

---

# Production Deployment Flow

```text
Developer

↓

git add .

↓

git commit

↓

git push origin main

↓

GitHub

↓

Render Detects Changes

↓

Build Environment

↓

Install Dependencies

↓

Run Application

↓

Health Check

↓

Backend Live

↓

Frontend Connects

↓

Customers Use System
```

---

# Future Deployment Enhancements

Planned improvements include:

- Docker Compose for local development
- Kubernetes deployment
- Blue/Green deployments
- Zero-downtime releases
- GitHub Actions CI/CD
- Automated testing pipeline
- Redis caching
- CDN integration
- Multi-region deployments
- Auto-scaling

---

# Conclusion

The XSOLA deployment architecture uses GitHub for version control, Render for application hosting, Supabase for managed PostgreSQL, and Docker for consistent runtime environments. This approach provides automated deployments, secure configuration management, scalability, and reliable production operations while supporting future growth of the XSOLA platform.
