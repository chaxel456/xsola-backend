# XSOLA Project Directory Structure

Version: 1.0.0

Project: XSOLA Smart Solar Energy Management Platform

Audience:
- Backend Developers
- Frontend Developers
- IoT Developers
- DevOps Engineers
- New Contributors

---

# Table of Contents

1. Introduction
2. Repository Structure
3. Backend Structure
4. Frontend Structure
5. Firmware Structure
6. Documentation Structure
7. Test Structure
8. Docker Structure
9. Configuration Files
10. Deployment Files
11. Development Workflow
12. File Naming Conventions

---

# 1. Introduction

The XSOLA project follows a modular architecture.

Each component has its own responsibility.

Modules are separated into:

- Backend
- Frontend
- Firmware
- Documentation
- Tests
- Deployment
- Configuration

This organization makes the project scalable, maintainable, and easy to understand.

---

# 2. Complete Repository Structure

```

xsola/

├── app/
├── frontend/
├── firmware/
├── docs/
├── tests/
├── docker/
├── scripts/
├── alembic/
├── .github/
├── .env.example
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── README.md
├── LICENSE
└── .gitignore

```

---

# 3. Backend Structure

```

app/

├── main.py
├── api/
├── core/
├── models/
├── schemas/
├── services/
├── repositories/
├── middleware/
├── dependencies/
├── mqtt/
├── scheduler/
├── utils/
├── database/
└── static/

```

---

## main.py

Purpose

Application entry point.

Responsibilities

- Create FastAPI instance
- Register routers
- Configure middleware
- Startup events
- Shutdown events

---

## api/

Contains all API routes.

```

api/

├── v1/
│
├── auth.py
├── waitlist.py
├── customers.py
├── devices.py
├── payments.py
├── subscriptions.py
├── reports.py
├── telemetry.py
├── notifications.py
└── health.py

```

Responsibilities

- Receive requests
- Validate inputs
- Call services
- Return responses

---

## core/

Contains application configuration.

```

core/

├── config.py
├── security.py
├── database.py
├── logging.py
└── settings.py

```

Responsibilities

- Environment variables
- JWT
- Database
- Logging
- Global settings

---

## models/

Contains SQLAlchemy models.

```

models/

├── user.py
├── customer.py
├── waitlist.py
├── payment.py
├── subscription.py
├── device.py
├── telemetry.py
└── notification.py

```

Responsibilities

Database tables.

---

## schemas/

Contains Pydantic models.

```

schemas/

├── auth.py
├── customer.py
├── payment.py
├── subscription.py
├── telemetry.py
└── device.py

```

Responsibilities

- Validation
- Serialization
- Request models
- Response models

---

## services/

Contains business logic.

```

services/

├── auth_service.py
├── payment_service.py
├── mqtt_service.py
├── report_service.py
├── telemetry_service.py
└── customer_service.py

```

Responsibilities

- Business rules
- Database operations
- External integrations

---

## repositories/

Contains database access layer.

```

repositories/

├── customer_repository.py
├── payment_repository.py
├── device_repository.py
└── telemetry_repository.py

```

Responsibilities

- CRUD operations
- Database abstraction
- Query optimization

---

## middleware/

Contains middleware.

Examples

```

auth.py

cors.py

logging.py

rate_limit.py

```

Responsibilities

- Authentication
- Logging
- CORS
- Request filtering

---

## dependencies/

Contains dependency injection.

Examples

```

current_user.py

permissions.py

database.py

```

Responsibilities

- Shared dependencies
- Authentication helpers
- Database sessions

---

## mqtt/

Contains MQTT logic.

```

mqtt/

├── publisher.py
├── subscriber.py
├── topics.py
├── handlers.py
└── client.py

```

Responsibilities

- Publish
- Subscribe
- Device communication
- Topic management

---

## scheduler/

Contains APScheduler jobs.

```

scheduler/

├── cleanup.py
├── subscription_check.py
├── reports.py
└── reminders.py

```

Responsibilities

- Background jobs
- Automation
- Maintenance tasks

---

## utils/

Contains reusable utilities.

Examples

```

helpers.py

validators.py

email.py

sms.py

```

Responsibilities

- Helper functions
- Validation
- Notifications

---

# 4. Frontend Structure

```

frontend/

├── index.html
├── login.html
├── dashboard.html
├── waitlist.html
├── customers.html
├── devices.html
├── reports.html
├── css/
├── js/
├── images/
└── assets/

```

---

## css/

```

css/

├── style.css
├── dashboard.css
├── login.css
├── customers.css
└── responsive.css

```

Responsibilities

- Layout
- Components
- Responsive design

---

## js/

```

js/

├── config.js
├── auth.js
├── dashboard.js
├── waitlist.js
├── customers.js
├── devices.js
├── payments.js
├── reports.js
└── utils.js

```

Responsibilities

- API calls
- UI logic
- Authentication
- Event handling

---

## images/

Contains:

- Logos
- Icons
- Photos
- Backgrounds

---

## assets/

Contains:

- Fonts
- Downloads
- Static files

---

# 5. Firmware Structure

```

firmware/

├── src/
├── include/
├── lib/
├── platformio.ini
└── README.md

```

---

## src/

```

src/

├── main.cpp
├── wifi.cpp
├── mqtt.cpp
├── relay.cpp
├── telemetry.cpp
├── sensors.cpp
└── ota.cpp

```

Responsibilities

- Device control
- Sensor reading
- MQTT communication
- OTA updates

---

## include/

Header files.

```

wifi.h

mqtt.h

relay.h

```

---

## lib/

External libraries.

Examples

- ArduinoJson
- PubSubClient

---

# 6. Documentation Structure

```

docs/

├── README.md
├── API.md
├── ARCHITECTURE.md
├── AUTHENTICATION.md
├── BACKEND.md
├── DATABASE.md
├── MQTT.md
├── ESP32.md
├── HARDWARE.md
├── DEVICE_PROTOCOL.md
├── DATA_FLOW.md
├── DEPLOYMENT.md
├── INSTALLATION.md
├── SECURITY.md
├── TESTING.md
├── MONITORING.md
├── ADMIN_GUIDE.md
├── USER_GUIDE.md
├── FAQ.md
├── TROUBLESHOOTING.md
├── CODING_STANDARDS.md
├── DIRECTORY_STRUCTURE.md
├── FEATURES.md
├── RELEASE_PROCESS.md
├── GLOSSARY.md
└── CHANGELOG.md

```

---

# 7. Test Structure

```

tests/

├── test_auth.py
├── test_customers.py
├── test_waitlist.py
├── test_devices.py
├── test_payments.py
├── test_reports.py
├── test_telemetry.py
└── conftest.py

```

Responsibilities

- Unit tests
- Integration tests
- API tests
- Fixtures

---

# 8. Docker Structure

```

docker/

├── nginx/
├── postgres/
├── mosquitto/
└── scripts/

```

Responsibilities

- Reverse proxy
- Database container
- MQTT broker
- Startup scripts

---

# 9. Configuration Files

## requirements.txt

Python dependencies.

---

## Dockerfile

Backend container configuration.

---

## docker-compose.yml

Defines multi-container services:

- Backend
- PostgreSQL
- MQTT Broker
- Nginx

---

## .env.example

Template for environment variables.

---

## .gitignore

Files excluded from Git.

Examples

```
venv/
__pycache__/
.env
*.pyc
node_modules/
```

---

# 10. Deployment Files

```

.github/

└── workflows/

deploy.yml

tests.yml

lint.yml

```

Responsibilities

- Continuous Integration
- Automated Testing
- Automated Deployment

---

# 11. Development Workflow

```
Clone Repository

↓

Create Branch

↓

Implement Feature

↓

Run Tests

↓

Update Documentation

↓

Commit

↓

Push

↓

Pull Request

↓

Code Review

↓

Merge

↓

Deploy
```

---

# 12. File Naming Conventions

Python

```
snake_case.py
```

Example

```
customer_service.py
```

Classes

```
PascalCase
```

Example

```
CustomerService
```

Variables

```
snake_case
```

Example

```
customer_name
```

Constants

```
UPPER_CASE
```

Example

```
JWT_SECRET
```

HTML

```
dashboard.html
```

CSS

```
dashboard.css
```

JavaScript

```
dashboard.js
```

---

# Project Dependency Overview

```
Frontend
    │
    ▼
Backend (FastAPI)
    │
    ├────────► PostgreSQL
    │
    ├────────► MQTT Broker
    │              │
    │              ▼
    │           ESP32 Firmware
    │              │
    │              ▼
    │           Relay & Sensors
    │
    ├────────► Paystack
    │
    └────────► Reports & Notifications
```

---

# Conclusion

The XSOLA directory structure is organized around clear separation of concerns. Each folder has a single responsibility, making the project easier to develop, test, deploy, and maintain. This modular design supports future growth while helping new contributors quickly understand the codebase.
