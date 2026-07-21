# XSOLA Backend Documentation

## Introduction

The XSOLA Backend is the core of the Smart Solar Energy Management Platform. It is responsible for processing requests from the frontend, managing business logic, interacting with the PostgreSQL database, communicating with IoT devices through MQTT, integrating with payment providers, and exposing RESTful APIs.

The backend is built using **FastAPI**, a modern, asynchronous Python web framework that provides high performance, automatic API documentation, and robust data validation.

---

# Backend Overview

The backend acts as the central controller for the XSOLA ecosystem.

```text
Frontend

↓

FastAPI Backend

↓

Business Logic

↓

Database

↓

MQTT

↓

ESP32

↓

Solar Hardware
```

Every request from users, administrators, IoT devices, or payment gateways is processed by the backend before reaching other system components.

---

# Core Responsibilities

The backend is responsible for:

- User Authentication
- Authorization
- Waitlist Management
- Customer Management
- Device Management
- Subscription Management
- Payment Processing
- Notification Management
- Telemetry Collection
- Report Generation
- MQTT Communication
- Scheduler Tasks
- Database Management
- API Documentation
- Security
- Logging

---

# Technology Stack

| Technology | Purpose |
|------------|----------|
| Python | Programming Language |
| FastAPI | Web Framework |
| SQLAlchemy | ORM |
| PostgreSQL | Database |
| Supabase | Cloud Database |
| Pydantic | Data Validation |
| JWT | Authentication |
| bcrypt | Password Hashing |
| APScheduler | Background Jobs |
| MQTT | Device Communication |
| Uvicorn | ASGI Server |
| Render | Cloud Deployment |

---

# Backend Architecture

```text
Browser

↓

FastAPI

↓

Routers

↓

Schemas

↓

Services

↓

Models

↓

Database

↓

Response
```

---

# Folder Structure

```text
app/

│

├── api/

├── core/

├── models/

├── schemas/

├── services/

├── utils/

├── mqtt/

├── scheduler/

├── database/

├── main.py

└── __init__.py
```

---

# Folder Explanation

## app/

The root application package.

Contains every backend component.

---

## api/

Contains all REST API endpoints.

```text
api/

v1/

auth.py

customers.py

devices.py

payments.py

subscriptions.py

telemetry.py

reports.py

waitlist.py

notifications.py

router.py
```

Responsibilities:

- Receive HTTP requests
- Validate incoming data
- Call service layer
- Return JSON responses

---

## core/

Contains backend configuration.

Example files

```text
config.py

security.py

database.py
```

Responsibilities

- Environment variables
- JWT configuration
- Password hashing
- Database configuration
- Application settings

---

## models/

Contains SQLAlchemy models.

Each file represents a database table.

Example

```text
user.py

customer.py

device.py

payment.py

subscription.py

telemetry.py
```

Responsibilities

- Define database tables
- Relationships
- Constraints
- Primary Keys

---

## schemas/

Contains Pydantic models.

Used for request validation and API responses.

Example

```text
UserCreate

UserLogin

CustomerCreate

PaymentCreate

TelemetryCreate
```

Responsibilities

- Validate input
- Serialize output
- Generate Swagger documentation

---

## services/

Contains business logic.

Example

```text
auth_service.py

device_service.py

payment_service.py

mqtt_service.py
```

Responsibilities

- Database operations
- External API calls
- Payment verification
- MQTT publishing
- Business rules

---

## utils/

Contains reusable helper functions.

Examples

```text
email.py

logger.py

helpers.py

validators.py
```

Responsibilities

- Logging
- Email utilities
- Common functions
- Input validation

---

## mqtt/

Contains MQTT client configuration.

Responsibilities

- Connect broker
- Subscribe topics
- Publish commands
- Handle telemetry
- Handle disconnects

---

## scheduler/

Contains APScheduler jobs.

Examples

```text
subscription_checker.py

cleanup.py

daily_reports.py
```

Responsibilities

- Expire subscriptions
- Send reminders
- Generate reports
- Cleanup database

---

## database/

Contains database session management.

Responsibilities

- Database engine
- Session creation
- Connection pooling

---

# Request Lifecycle

Every API request follows the same path.

```text
Browser

↓

FastAPI Route

↓

Authentication

↓

Schema Validation

↓

Business Logic

↓

Database

↓

Response
```

---

# API Modules

The backend currently provides the following modules.

| Module | Description |
|---------|-------------|
| Authentication | User login and registration |
| Waitlist | Customer interest registration |
| Customers | Customer management |
| Devices | Device management |
| Payments | Payment processing |
| Reports | Dashboard statistics |
| Notifications | Alerts and messages |
| Telemetry | IoT data collection |
| Subscriptions | Energy plans |

---

# Authentication Layer

Uses JWT.

```text
Login

↓

Generate Token

↓

Store Token

↓

Authorization Header

↓

Protected APIs
```

---

# Database Layer

Uses SQLAlchemy ORM.

Advantages

- SQL Injection protection
- Relationships
- Easy migrations
- Database independence

---

# Business Logic Layer

The service layer separates business rules from API routes.

Example

```text
Route

↓

Payment Service

↓

Verify Paystack

↓

Update Database

↓

Publish MQTT
```

---

# MQTT Integration

The backend communicates with ESP32 devices using MQTT.

Example

```text
Backend

↓

MQTT Publish

↓

ESP32

↓

Relay
```

---

# Scheduler

Background jobs run automatically.

Examples

- Subscription expiry
- Daily reports
- Database cleanup
- Payment reminders

---

# Error Handling

Standard response format:

```json
{
    "success": false,
    "message": "Customer not found"
}
```

---

# Logging

The backend logs:

- Server startup
- Database connection
- MQTT connection
- Login attempts
- Payment verification
- Device activation
- Errors
- Scheduler events

---

# Security

Security measures include:

- JWT Authentication
- bcrypt Password Hashing
- HTTPS
- Environment Variables
- SQLAlchemy ORM
- Input Validation
- CORS
- Secret Key Protection

---

# Deployment

Current production deployment:

Backend

```
Render
```

Database

```
Supabase PostgreSQL
```

---

# Performance Features

- Async FastAPI routes
- Connection pooling
- Automatic OpenAPI generation
- Efficient ORM queries
- Lightweight MQTT communication
- Background scheduling

---

# API Documentation

FastAPI automatically generates documentation.

Swagger

```
/docs
```

OpenAPI

```
/openapi.json
```

---

# Backend Workflow

```text
User

↓

Frontend

↓

Backend Route

↓

Authentication

↓

Validation

↓

Business Logic

↓

Database

↓

MQTT (if required)

↓

Response
```

---

# Future Backend Improvements

- Redis caching
- WebSocket support
- AI analytics services
- Multi-tenant architecture
- Background task queue (Celery)
- Distributed MQTT brokers
- API rate limiting
- Audit logging
- Cloud storage integration
- SMS and Email microservices

---

# Conclusion

The XSOLA backend is designed using a modular architecture that separates routing, business logic, data models, validation, configuration, and utilities into independent components. This structure improves maintainability, scalability, and testability while supporting cloud deployment, IoT integration, secure authentication, and real-time solar energy management.
