# XSOLA Data Flow Documentation

Version: 1.0.0

Project: XSOLA Smart Solar Energy Management Platform

---

# Table of Contents

1. Introduction
2. Overall System Data Flow
3. User Authentication Flow
4. Waitlist Flow
5. Customer Management Flow
6. Device Registration Flow
7. Device Control Flow
8. Telemetry Flow
9. Payment Flow
10. Subscription Flow
11. Notification Flow
12. Report Generation Flow
13. Dashboard Flow
14. Database Flow
15. MQTT Flow
16. Error Handling Flow
17. Background Scheduler Flow
18. Complete System Workflow

---

# 1. Introduction

The XSOLA platform consists of multiple independent modules that exchange information through secure APIs, MQTT messaging, and database operations.

Every user action follows a predictable path:

```
User

↓

Frontend

↓

FastAPI

↓

Database

↓

Response
```

For IoT devices:

```
ESP32

↓

MQTT Broker

↓

Backend

↓

Database

↓

Dashboard
```

---

# 2. Overall System Data Flow

```
                     USER
                      │
                      ▼
          HTML / CSS / JavaScript
                      │
                      ▼
             FastAPI REST API
                      │
        ┌─────────────┼─────────────┐
        ▼             ▼             ▼
 PostgreSQL      MQTT Broker     Scheduler
        │             │
        ▼             ▼
 Reports      ESP32 Devices
        │             │
        └──────► Dashboard ◄──────┘
```

---

# 3. User Authentication Flow

```
User enters email/password

↓

Frontend validates input

↓

POST /api/v1/auth/login

↓

FastAPI

↓

Verify password

↓

Generate JWT

↓

Return Token

↓

Store Token

↓

Redirect Dashboard
```

Example Request

```json
{
  "email":"admin@xsola.com",
  "password":"password123"
}
```

Example Response

```json
{
  "access_token":"eyJhbGc...",
  "token_type":"Bearer"
}
```

---

# 4. Waitlist Flow

```
Visitor

↓

Landing Page

↓

Waitlist Form

↓

POST /waitlist

↓

FastAPI Validation

↓

Database Insert

↓

Success Response

↓

Frontend Success Message
```

Database Table

```
waitlist
```

Stored Data

- Name
- Email
- Phone
- Institution
- Created At

---

# 5. Customer Management Flow

```
Admin

↓

Dashboard

↓

Customer Form

↓

POST /customers

↓

Validation

↓

SQLAlchemy

↓

PostgreSQL

↓

Response

↓

Dashboard Refresh
```

Operations

- Create
- Read
- Update
- Delete
- Search

---

# 6. Device Registration Flow

When a new ESP32 boots for the first time.

```
ESP32 Starts

↓

Connect Wi-Fi

↓

Connect MQTT

↓

Publish Registration

↓

Backend

↓

Validate Device

↓

Store Device

↓

Status = Active

↓

Send ACK
```

MQTT Topic

```
xsola/device/{device_id}/register
```

---

# 7. Device Control Flow

Admin remotely turns electricity ON.

```
Dashboard

↓

POST Control API

↓

FastAPI

↓

MQTT Publish

↓

ESP32

↓

Relay ON

↓

ACK

↓

Backend

↓

Dashboard Updated
```

Example Command

```json
{
  "command":"relay_on"
}
```

---

# 8. Telemetry Flow

Every 30 seconds.

```
Voltage Sensor

↓

ESP32

↓

MQTT Publish

↓

Backend Subscriber

↓

Validation

↓

Database

↓

Dashboard Charts
```

Telemetry Example

```json
{
  "battery_voltage":25.4,
  "solar_voltage":39.2,
  "temperature":31,
  "relay":"ON"
}
```

Stored In

```
telemetry
```

---

# 9. Payment Flow

Customer makes payment.

```
Customer

↓

Frontend

↓

Paystack Checkout

↓

Payment

↓

Paystack Webhook

↓

Backend Verification

↓

Subscription Activated

↓

MQTT Publish

↓

ESP32 Relay ON
```

If payment fails

```
Subscription Remains Inactive
```

---

# 10. Subscription Flow

```
Customer

↓

Choose Plan

↓

Payment

↓

Verification

↓

Subscription Table

↓

Active

↓

Scheduler Monitors Expiry

↓

Expired?

↓

Relay OFF
```

---

# 11. Notification Flow

```
Event

↓

Backend

↓

Notification Service

↓

Database

↓

Email

↓

SMS

↓

Dashboard Notification
```

Events

- Payment Success
- Payment Failure
- Low Battery
- Device Offline
- Subscription Expired

---

# 12. Report Generation Flow

```
Dashboard

↓

GET Reports

↓

Backend

↓

Database Queries

↓

Statistics

↓

JSON Response

↓

Charts
```

Reports

- Revenue
- Customers
- Devices
- Payments
- Telemetry

---

# 13. Dashboard Flow

```
Login

↓

JWT Token

↓

Dashboard Loads

↓

API Calls

↓

Statistics

↓

Tables

↓

Charts

↓

Auto Refresh
```

Dashboard Endpoints

```
/dashboard

/customers

/payments

/devices

/reports

/telemetry
```

---

# 14. Database Flow

```
API Request

↓

Validation

↓

SQLAlchemy

↓

PostgreSQL

↓

Commit

↓

Return Object
```

Operations

- INSERT
- UPDATE
- DELETE
- SELECT

---

# 15. MQTT Flow

```
Backend

↓

MQTT Broker

↓

ESP32

↓

Relay

↓

ACK

↓

Broker

↓

Backend

↓

Dashboard
```

Topics

```
register

control

telemetry

status

heartbeat

alert

firmware

ack
```

---

# 16. Error Handling Flow

```
Request

↓

Validation

↓

Exception?

↓

YES

↓

Error Handler

↓

JSON Error

↓

Frontend
```

Example

```json
{
  "detail":"Customer not found"
}
```

Status

```
404
```

---

# 17. Background Scheduler Flow

APScheduler performs automated tasks.

```
Scheduler

↓

Check Expired Subscriptions

↓

Deactivate Subscription

↓

Publish MQTT

↓

Relay OFF

↓

Notify Customer
```

Other Jobs

- Daily Reports
- Database Cleanup
- Reminder Emails
- Device Health Checks

---

# 18. Complete XSOLA Workflow

```
                 USER
                  │
                  ▼
        Landing Page / Dashboard
                  │
                  ▼
         HTML CSS JavaScript
                  │
                  ▼
             FastAPI Backend
                  │
     ┌────────────┼────────────┐
     ▼            ▼            ▼
 PostgreSQL   MQTT Broker   Scheduler
     │            │
     ▼            ▼
 Reports       ESP32 Device
                  │
     ┌────────────┼────────────┐
     ▼            ▼            ▼
 Relay      Voltage Sensor   Current Sensor
     │            │            │
     └────────────┼────────────┘
                  ▼
            Solar System
                  │
                  ▼
              Electricity
```

---

# Data Validation

Every request passes through:

```
Frontend Validation

↓

FastAPI Validation

↓

Pydantic

↓

Business Logic

↓

Database Validation
```

This prevents:

- Invalid data
- SQL Injection
- Missing fields
- Invalid formats
- Duplicate records

---

# Security Flow

```
User Login

↓

JWT Generated

↓

Stored in Browser

↓

Authorization Header

↓

Backend Verification

↓

Access Granted
```

Authorization Header

```
Authorization: Bearer eyJhbGc...
```

---

# Logging Flow

```
Request

↓

Logger

↓

Database

↓

File Logs

↓

Monitoring Dashboard
```

Logged Events

- Login
- Payment
- Device Registration
- Errors
- MQTT Messages
- Scheduler Jobs

---

# Performance Optimization

XSOLA improves performance by:

- SQLAlchemy connection pooling
- Indexed database tables
- Efficient SQL queries
- MQTT asynchronous messaging
- FastAPI asynchronous endpoints
- Background scheduling
- Stateless JWT authentication

---

# Conclusion

The XSOLA data flow architecture ensures secure, reliable, and scalable communication between users, cloud services, databases, payment providers, MQTT brokers, and IoT devices. Every module has a clearly defined responsibility, allowing the platform to process user requests, monitor solar systems, automate subscriptions, and control hardware in real time while maintaining data integrity and high performance.
