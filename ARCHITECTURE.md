# XSOLA System Architecture

## Introduction

The XSOLA architecture is designed as a modern, cloud-based Internet of Things (IoT) platform that connects users, web applications, cloud services, databases, payment systems, and physical solar hardware into a single integrated ecosystem.

The architecture follows a layered approach where each layer has a specific responsibility while communicating securely with the next layer. This modular design makes the system scalable, maintainable, secure, and easy to expand as new features are introduced.

---

# High-Level Architecture

```text
                        +----------------------+
                        |      End Users       |
                        | Customers & Admins   |
                        +----------+-----------+
                                   |
                                   |
                         Web Browser (HTTPS)
                                   |
                                   ▼
                    +----------------------------+
                    |        Frontend            |
                    | HTML • CSS • JavaScript    |
                    +-------------+--------------+
                                  |
                        REST API Requests
                                  |
                                  ▼
                    +----------------------------+
                    |      FastAPI Backend       |
                    | Authentication             |
                    | Business Logic             |
                    | Payment Processing         |
                    | Device Management          |
                    | Notifications              |
                    | Reports                    |
                    +-------------+--------------+
                                  |
                   +--------------+--------------+
                   |                             |
                   ▼                             ▼
          PostgreSQL Database             MQTT Broker
              (Supabase)                 (Message Queue)
                                               |
                                               |
                                               ▼
                                      ESP32 IoT Controller
                                               |
                                               ▼
                                         Relay Module
                                               |
                                               ▼
                              Solar Inverter & Electrical Load
                                               |
                                               ▼
                                    Customer Receives Power
```

---

# Overall System Flow

```text
Customer

↓

Frontend Website

↓

FastAPI Backend

↓

PostgreSQL Database

↓

MQTT Broker

↓

ESP32

↓

Relay

↓

Solar System

↓

Electricity
```

---

# Architecture Layers

The XSOLA platform is divided into multiple layers.

Each layer performs a dedicated function.

---

# Layer 1 — Frontend

## Purpose

The frontend is the presentation layer of XSOLA.

It is responsible for all user interaction.

Users never communicate directly with the database or hardware.

Every request passes through the backend.

---

## Responsibilities

- Landing page
- Waitlist registration
- Login
- Dashboard
- Customer management
- Device management
- Payment management
- Reports
- Notifications

---

## Technologies

- HTML5
- CSS3
- JavaScript

---

## Pages

```text
index.html

↓

waitlist.html

↓

login.html

↓

dashboard.html
```

---

## Communication

The frontend communicates with the backend using HTTPS REST APIs.

Example:

```javascript
fetch("https://xsola-backend-7.onrender.com/api/v1/waitlist/",{
    method:"POST",
    body:JSON.stringify(data)
})
```

---

# Layer 2 — Backend

## Purpose

The backend is the brain of XSOLA.

It controls every business process.

No data reaches the database without first passing through the backend.

---

## Responsibilities

- Authentication
- Authorization
- Customer Management
- Waitlist
- Devices
- Payments
- Reports
- Notifications
- Telemetry
- MQTT Communication
- Scheduler
- Logging

---

## Technology

- FastAPI
- Python
- SQLAlchemy
- Pydantic
- JWT
- APScheduler

---

## API Example

```text
POST

/api/v1/waitlist/
```

↓

Validate Request

↓

Save Database

↓

Return Response

---

# Layer 3 — Database

## Purpose

Stores every piece of information permanently.

---

## Database

PostgreSQL

Hosted on

Supabase

---

## Stored Information

- Users
- Customers
- Waitlist
- Devices
- Payments
- Notifications
- Reports
- Telemetry
- Subscriptions

---

## Advantages

- Reliable
- Secure
- ACID Transactions
- Fast
- Cloud Hosted

---

# Layer 4 — MQTT Broker

## Purpose

Acts as the communication bridge between the cloud backend and physical IoT devices.

Unlike REST APIs, MQTT is lightweight and optimized for devices with limited bandwidth and processing power.

---

## Responsibilities

- Deliver commands
- Receive telemetry
- Receive alerts
- Receive heartbeat
- Publish status

---

## Publish Topics

```text
xsola/device/{device_id}/control
```

---

## Subscribe Topics

```text
xsola/device/{device_id}/telemetry

xsola/device/{device_id}/status

xsola/device/{device_id}/alerts
```

---

# Layer 5 — ESP32

## Purpose

The ESP32 is the field controller installed inside each customer’s solar installation.

It connects the physical solar hardware to the XSOLA cloud platform.

---

## Responsibilities

- Connect to WiFi
- Connect to MQTT Broker
- Receive commands
- Read sensors
- Send telemetry
- Monitor battery
- Monitor inverter
- Monitor solar charging
- Operate relay
- Report faults

---

## Example Telemetry

```json
{
  "device_id":"XS001",
  "battery":95,
  "solar_voltage":24.6,
  "load_voltage":220,
  "relay":"ON"
}
```

---

# Layer 6 — Relay Module

## Purpose

The relay is the physical switch that controls electricity supplied to the customer.

It receives instructions from the ESP32.

---

## Operations

Relay ON

↓

Electricity Enabled

Relay OFF

↓

Electricity Disabled

---

## Trigger Conditions

- Successful payment
- Subscription activation
- Subscription expiry
- Manual admin control
- Safety shutdown
- Emergency maintenance

---

# Layer 7 — Solar Energy System

The relay controls the customer's solar power system.

Components include:

- Solar Panels
- Charge Controller
- Battery Bank
- Inverter
- Distribution Board
- Electrical Load

---

## Power Flow

```text
Solar Panels

↓

Charge Controller

↓

Battery

↓

Inverter

↓

Relay

↓

Customer Appliances
```

---

# Data Flow

## Waitlist Registration

```text
Customer

↓

Frontend

↓

Backend API

↓

Database

↓

Success Response

↓

Frontend
```

---

## Customer Registration

```text
Admin

↓

Frontend Dashboard

↓

Backend

↓

Database

↓

Customer Created
```

---

## Payment Flow

```text
Customer

↓

Paystack

↓

Backend

↓

Verify Payment

↓

Subscription Updated

↓

Database

↓

MQTT Publish

↓

ESP32

↓

Relay ON
```

---

## Device Control Flow

```text
Administrator

↓

Dashboard

↓

Backend

↓

MQTT Broker

↓

ESP32

↓

Relay

↓

Electricity
```

---

## Telemetry Flow

```text
ESP32

↓

MQTT Broker

↓

Backend

↓

Database

↓

Dashboard

↓

Administrator
```

---

# Security Architecture

Security is enforced at multiple layers.

## Frontend

- HTTPS
- Input validation

---

## Backend

- JWT Authentication
- Password hashing
- Authorization
- Request validation
- CORS protection

---

## Database

- Secure credentials
- Restricted access
- Cloud backups

---

## MQTT

- Username/password authentication
- Topic-based authorization
- Encrypted connections (TLS)

---

# Scalability

XSOLA is designed to support growth from a handful of installations to thousands of devices.

The architecture supports:

- Multiple branches
- Thousands of customers
- Thousands of ESP32 devices
- Horizontal API scaling
- Cloud database scaling
- Load balancing
- Future mobile applications
- Additional payment providers
- Integration with smart meters and AI analytics

---

# Fault Tolerance

The system includes several mechanisms to improve reliability:

- Automatic backend restarts on Render
- Persistent PostgreSQL storage
- Scheduled background jobs
- Device heartbeat monitoring
- Payment verification before activation
- Telemetry logging for diagnostics
- Retry mechanisms for MQTT communication

---

# Advantages of the XSOLA Architecture

- Modular and maintainable
- Cloud-native deployment
- Secure API-driven communication
- Real-time IoT control
- Scalable to large customer bases
- Supports remote device management
- Flexible subscription model
- Easy integration with future mobile apps
- Extensible for AI-powered analytics and predictive maintenance

---

# Conclusion

The XSOLA architecture combines a modern web frontend, a FastAPI backend, a PostgreSQL cloud database, MQTT messaging, and ESP32-based IoT hardware into a unified platform for managing subscription-based solar energy systems. By separating responsibilities across layers and using industry-standard technologies, the platform delivers secure, scalable, and real-time management of customers, payments, devices, and energy delivery while providing a solid foundation for future expansion.
