# XSOLA Backend API Documentation

**Version:** 1.0.0

**Base URL**

```
https://xsola-backend-7.onrender.com
```

**Swagger Documentation**

```
https://xsola-backend-7.onrender.com/docs
```

---

# Introduction

The XSOLA Backend exposes a RESTful API built with FastAPI.

The API enables communication between:

- Frontend Web Application
- Mobile Applications
- ESP32 IoT Devices
- Third-party Services (Paystack)
- Administrator Dashboard

All responses are returned in JSON format.

---

# Authentication

Authentication uses JWT (JSON Web Tokens).

Protected endpoints require:

```http
Authorization: Bearer <JWT_TOKEN>
```

---

# Authentication Endpoints

## Register User

**Endpoint**

```http
POST /api/v1/auth/auth/register
```

### Request

```json
{
    "name":"John Doe",
    "email":"john@example.com",
    "password":"password123"
}
```

### Success Response

```json
{
    "id":1,
    "name":"John Doe",
    "email":"john@example.com",
    "access_token":"eyJhbGciOiJIUzI1NiIs...",
    "token_type":"bearer"
}
```

---

## Login

**Endpoint**

```http
POST /api/v1/auth/auth/login
```

### Request

```json
{
    "email":"john@example.com",
    "password":"password123"
}
```

### Response

```json
{
    "access_token":"eyJhbGc...",
    "token_type":"bearer"
}
```

---

## Current User

**Endpoint**

```http
GET /api/v1/auth/auth/me
```

**Headers**

```http
Authorization: Bearer JWT_TOKEN
```

### Response

```json
{
    "id":1,
    "name":"John Doe",
    "email":"john@example.com"
}
```

---

# Waitlist API

## Get Waitlist

```http
GET /api/v1/waitlist/
```

### Response

```json
[
    {
        "id":1,
        "full_name":"John Doe",
        "email":"john@gmail.com",
        "phone":"08012345678"
    }
]
```

---

## Create Waitlist Entry

```http
POST /api/v1/waitlist/
```

### Request

```json
{
    "full_name":"John Doe",
    "email":"john@gmail.com",
    "phone":"08012345678"
}
```

### Response

```json
{
    "id":1,
    "full_name":"John Doe",
    "email":"john@gmail.com",
    "phone":"08012345678"
}
```

---

## Get Waitlist Member

```http
GET /api/v1/waitlist/{waitlist_id}
```

### Response

```json
{
    "id":1,
    "full_name":"John Doe",
    "email":"john@gmail.com",
    "phone":"08012345678"
}
```

---

# Customers API

## Get Customers

```http
GET /api/v1/customers/customers/
```

---

## Create Customer

```http
POST /api/v1/customers/customers/
```

### Example Request

```json
{
    "full_name":"Jane Smith",
    "email":"jane@example.com",
    "phone":"08098765432",
    "address":"Owerri, Nigeria"
}
```

### Example Response

```json
{
    "id":3,
    "full_name":"Jane Smith",
    "status":"Active"
}
```

---

## Get Customer

```http
GET /api/v1/customers/customers/{customer_id}
```

---

## Delete Customer

```http
DELETE /api/v1/customers/customers/{customer_id}
```

---

# Devices API

## Get Devices

```http
GET /api/v1/devices/devices/
```

---

## Create Device

```http
POST /api/v1/devices/devices/
```

### Example Request

```json
{
    "serial_number":"XS001",
    "customer_id":5
}
```

---

## Get Device

```http
GET /api/v1/devices/devices/{device_id}
```

---

## Delete Device

```http
DELETE /api/v1/devices/devices/{device_id}
```

---

## Activate Device

```http
POST /api/v1/devices/devices/{device_id}/activate
```

### Response

```json
{
    "message":"Device Activated"
}
```

---

## Deactivate Device

```http
POST /api/v1/devices/devices/{device_id}/deactivate
```

### Response

```json
{
    "message":"Device Deactivated"
}
```

---

# Payments API

## Get Payments

```http
GET /api/v1/payments/payments/
```

---

## Create Payment

```http
POST /api/v1/payments/payments/
```

---

## Get Payment

```http
GET /api/v1/payments/payments/{payment_id}
```

---

## Delete Payment

```http
DELETE /api/v1/payments/payments/{payment_id}
```

---

## Initialize Payment

```http
POST /api/v1/payments/payments/initialize
```

### Example Request

```json
{
    "customer_id":5,
    "amount":50000
}
```

### Response

```json
{
    "authorization_url":"https://checkout.paystack.com/...",
    "reference":"PSK_123456789"
}
```

---

## Verify Payment

```http
GET /api/v1/payments/payments/verify/{reference}
```

### Response

```json
{
    "status":"success",
    "reference":"PSK_123456789"
}
```

---

## Paystack Webhook

```http
POST /api/v1/payments/payments/webhook
```

Receives payment events directly from Paystack.

---

# Subscriptions API

## Get Subscriptions

```http
GET /api/v1/subscriptions/
```

---

## Create Subscription

```http
POST /api/v1/subscriptions/
```

---

## Get Subscription

```http
GET /api/v1/subscriptions/{subscription_id}
```

---

## Customer Subscriptions

```http
GET /api/v1/subscriptions/customer/{customer_id}
```

---

# Notifications API

## Get Notifications

```http
GET /api/v1/notifications/notifications/
```

---

## Create Notification

```http
POST /api/v1/notifications/notifications/
```

---

## Get Notification

```http
GET /api/v1/notifications/notifications/{notification_id}
```

---

## Delete Notification

```http
DELETE /api/v1/notifications/notifications/{notification_id}
```

---

## Mark Notification as Read

```http
PUT /api/v1/notifications/notifications/{notification_id}/read
```

---

# Reports API

## Dashboard Statistics

```http
GET /api/v1/reports/reports/dashboard
```

### Example Response

```json
{
    "waitlist":120,
    "customers":54,
    "devices":52,
    "payments":210,
    "subscriptions":50
}
```

---

# Telemetry API

## Get Telemetry

```http
GET /api/v1/telemetry/telemetry/
```

---

## Create Telemetry

```http
POST /api/v1/telemetry/telemetry/
```

### Example Request

```json
{
    "device_id":"XS001",
    "battery":96,
    "solar_voltage":24.6,
    "load_voltage":220,
    "relay":"ON"
}
```

---

## Get Telemetry by ID

```http
GET /api/v1/telemetry/telemetry/{telemetry_id}
```

---

## Delete Telemetry

```http
DELETE /api/v1/telemetry/telemetry/{telemetry_id}
```

---

## Device Telemetry

```http
GET /api/v1/telemetry/telemetry/device/{device_id}
```

---

## Latest Device Telemetry

```http
GET /api/v1/telemetry/telemetry/device/{device_id}/latest
```

---

# Health API

## Root Endpoint

```http
GET /
```

### Response

```json
{
    "message":"XSOLA Backend Running"
}
```

---

## Health Check

```http
GET /health
```

### Response

```json
{
    "status":"healthy"
}
```

---

## Database Test

```http
GET /db-test
```

Checks PostgreSQL database connectivity.

---

## Current User Test

```http
GET /me
```

Returns the authenticated user.

---

## Users Test

```http
GET /users-test
```

Returns sample user information for testing.

---

# HTTP Status Codes

| Code | Description |
|------|-------------|
|200|Request Successful|
|201|Resource Created|
|204|Resource Deleted|
|400|Bad Request|
|401|Unauthorized|
|403|Forbidden|
|404|Not Found|
|409|Conflict|
|422|Validation Error|
|500|Internal Server Error|

---

# API Modules

The XSOLA backend currently exposes the following modules:

- Authentication
- Users
- Waitlist
- Customers
- Devices
- Payments
- Subscriptions
- Notifications
- Reports
- Telemetry
- Health Monitoring

---

# Interactive API Documentation

FastAPI automatically generates interactive API documentation.

Swagger UI

```
https://xsola-backend-7.onrender.com/docs
```

OpenAPI Specification

```
https://xsola-backend-7.onrender.com/openapi.json
```

Developers are encouraged to use the Swagger interface to explore endpoints, execute requests, inspect schemas, and validate responses during development and testing.
