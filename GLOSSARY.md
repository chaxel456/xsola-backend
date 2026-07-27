# XSOLA Glossary

Version: 1.0.0

Project: XSOLA Smart Solar Energy Management Platform

Audience:
- Developers
- Administrators
- Customers
- Installers
- Support Engineers
- Investors

---

# Table of Contents

A
B
C
D
E
F
G
H
I
J
L
M
N
O
P
Q
R
S
T
U
V
W

---

# A

## Access Token

A temporary authentication token generated after a successful login. It is sent with API requests using the Authorization header.

Example

```
Authorization: Bearer eyJhbGc...
```

---

## Administrator

A user with permission to manage customers, devices, payments, subscriptions, reports, and system settings.

---

## Alembic

The database migration tool used with SQLAlchemy to create and update the PostgreSQL database schema.

Example

```
alembic upgrade head
```

---

## API

Application Programming Interface.

A collection of endpoints used by the frontend, mobile applications, and external systems to communicate with the XSOLA backend.

Example

```
GET /api/v1/customers
```

---

## APScheduler

A Python scheduling library used for running background jobs such as subscription checks, reminders, report generation, and maintenance tasks.

---

# B

## Backend

The server-side application built with FastAPI that processes requests, manages business logic, communicates with the database, and controls IoT devices.

---

## bcrypt

A password hashing algorithm used to securely store user passwords.

---

## Broker

The MQTT server responsible for receiving and forwarding messages between the backend and IoT devices.

Examples:

- Eclipse Mosquitto
- HiveMQ
- EMQX

---

# C

## Customer

A person or organization receiving solar services through XSOLA.

---

## CORS

Cross-Origin Resource Sharing.

A browser security mechanism that controls which websites can access the backend API.

---

## CRUD

Create

Read

Update

Delete

The four fundamental database operations.

---

## Cloud Deployment

Running XSOLA on cloud infrastructure such as Render or another supported hosting provider.

---

# D

## Dashboard

The administrator interface used to monitor customers, devices, subscriptions, telemetry, and payments.

---

## Database

The persistent storage layer of XSOLA.

Current implementation:

```
PostgreSQL
```

---

## Device

The installed hardware unit at a customer site.

Typically consists of:

- ESP32
- Relay
- Sensors
- Wi-Fi module
- Solar controller interface

---

## Docker

A containerization platform used to package and deploy XSOLA consistently across different environments.

---

# E

## Endpoint

A URL exposed by the backend API.

Example

```
POST /api/v1/auth/login
```

---

## ESP32

A Wi-Fi-enabled microcontroller used to control relays, read sensors, and communicate with the backend through MQTT.

---

## Environment Variables

Configuration values stored outside the application code.

Example

```
DATABASE_URL

SECRET_KEY

MQTT_BROKER
```

---

# F

## FastAPI

The Python framework used to build the XSOLA backend.

Features include:

- High performance
- Automatic API documentation
- Type validation
- Async support

---

## Firmware

Software running on the ESP32 that manages sensors, MQTT communication, and relay control.

---

# G

## Git

A distributed version control system used to manage the XSOLA source code.

---

## GitHub

The remote repository hosting platform used for collaboration, issue tracking, and deployment integration.

---

# H

## Heartbeat

A periodic message sent by an ESP32 device indicating that it is online and functioning correctly.

Example topic

```
xsola/device/device001/heartbeat
```

---

## HTTPS

The secure version of HTTP that encrypts communication between clients and the backend.

---

# I

## IoT

Internet of Things.

The network of connected devices that communicate with the XSOLA backend.

---

## Index

A database optimization structure that improves query performance.

---

# J

## JSON

JavaScript Object Notation.

The data format used for API communication.

Example

```json
{
  "device_id": "device001",
  "status": "online"
}
```

---

## JWT

JSON Web Token.

Used for authenticating API requests.

---

# L

## Logging

Recording application events for debugging, auditing, and monitoring.

---

# M

## Migration

Updating the database schema using Alembic migration scripts.

---

## MQTT

Message Queuing Telemetry Transport.

A lightweight messaging protocol used for communication between the backend and IoT devices.

---

## Middleware

Software that processes requests before they reach API endpoints.

Examples:

- Authentication
- Logging
- CORS
- Rate limiting

---

# N

## Notification

A message sent to users or administrators regarding payments, subscriptions, or device status.

---

# O

## ORM

Object-Relational Mapper.

SQLAlchemy maps Python classes to database tables.

---

# P

## Paystack

The payment gateway integrated with XSOLA for processing subscription payments.

---

## PostgreSQL

The relational database management system used to store application data.

---

## Pydantic

The validation library used by FastAPI to validate request and response data.

---

# Q

## QoS

Quality of Service.

MQTT message delivery level.

Levels:

```
0

1

2
```

---

# R

## Relay

An electrically operated switch controlled by the ESP32 to enable or disable supported electrical loads.

---

## Render

The cloud hosting platform used to deploy the XSOLA backend.

---

## Repository

The source code project managed with Git.

---

## REST API

A web API following REST principles for client-server communication.

---

# S

## Scheduler

The background task manager responsible for automated operations such as checking subscription expiry.

---

## Schema

A Pydantic model defining the structure of API request and response data.

---

## Sensor

A hardware component that measures physical values such as voltage, current, temperature, or battery level.

---

## SQLAlchemy

The ORM used by XSOLA to interact with PostgreSQL.

---

## Subscription

A customer's active service plan granting access to the solar system.

---

## Supabase

A managed backend platform providing PostgreSQL and supporting services for XSOLA deployments.

---

## Swagger UI

The interactive API documentation automatically generated by FastAPI.

Available at

```
/docs
```

---

# T

## Telemetry

Operational data collected from an ESP32 device and sent to the backend.

Examples:

- Voltage
- Current
- Battery level
- Temperature

---

## Topic

A communication channel used in MQTT.

Example

```
xsola/device/device001/control
```

---

# U

## Uvicorn

The ASGI server used to run the FastAPI application.

Example

```bash
uvicorn app.main:app --reload
```

---

# V

## Virtual Environment

An isolated Python environment containing project-specific dependencies.

Example

```bash
python -m venv venv
```

---

# W

## Waitlist

A collection of prospective customers who have expressed interest in joining XSOLA before installation or account activation.

---

## Webhook

An HTTP callback used by services such as Paystack to notify the XSOLA backend about completed events like successful payments.

---

## Workflow

A defined sequence of actions performed by the system.

Example:

```
Customer

↓

Payment

↓

Verification

↓

Subscription Activation

↓

MQTT Command

↓

ESP32

↓

Relay

↓

Power Available
```

---

# Acronyms

| Acronym | Meaning |
|----------|---------|
| API | Application Programming Interface |
| ASGI | Asynchronous Server Gateway Interface |
| CRUD | Create, Read, Update, Delete |
| CORS | Cross-Origin Resource Sharing |
| ESP32 | Espressif 32-bit Microcontroller |
| HTTPS | Hypertext Transfer Protocol Secure |
| IoT | Internet of Things |
| JSON | JavaScript Object Notation |
| JWT | JSON Web Token |
| MQTT | Message Queuing Telemetry Transport |
| ORM | Object-Relational Mapper |
| OTA | Over-the-Air Firmware Update |
| QoS | Quality of Service |
| REST | Representational State Transfer |
| SQL | Structured Query Language |
| UI | User Interface |
| URL | Uniform Resource Locator |

---

# Conclusion

This glossary provides a shared vocabulary for everyone working with XSOLA. It standardizes technical terms, platform concepts, and IoT terminology, making communication clearer across development, operations, documentation, and customer support.
