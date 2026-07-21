# XSOLA System Flow

## Introduction

This document explains how information moves throughout the XSOLA platform. Every action performed by a user, administrator, payment gateway, or IoT device follows a defined workflow. Understanding these workflows helps developers, testers, and system administrators understand how different components interact.

---

# Overall System Flow

```text
User

↓

Frontend Website

↓

FastAPI Backend

↓

Business Logic

↓

PostgreSQL Database

↓

MQTT Broker (when required)

↓

ESP32 Device

↓

Relay

↓

Solar System

↓

Response Returned
```

---

# 1. Waitlist Registration Flow

The waitlist allows potential customers to register their interest before purchasing or subscribing to a solar system.

## Workflow

```text
User

↓

Opens Website

↓

Clicks "Join Waitlist"

↓

Enters:
• Full Name
• Email
• Phone Number

↓

Frontend Validation

↓

POST /api/v1/waitlist/

↓

FastAPI Backend

↓

Validate Data

↓

Save to PostgreSQL

↓

Generate Success Response

↓

Frontend Displays Success Message
```

---

## API Used

```http
POST /api/v1/waitlist/
```

---

## Database Table

```
waitlist
```

---

## Output

Customer successfully joins the waitlist.

---

# 2. User Registration Flow

Administrators create user accounts for the system.

## Workflow

```text
Administrator

↓

Register Page

↓

Enter Name

↓

Enter Email

↓

Enter Password

↓

POST /api/v1/auth/auth/register

↓

Backend Validation

↓

Password Hashing (bcrypt)

↓

Store User

↓

JWT Ready

↓

Registration Successful
```

---

# 3. Login Flow

This workflow authenticates administrators.

```text
Administrator

↓

Login Page

↓

Enter Email

↓

Enter Password

↓

POST /api/v1/auth/auth/login

↓

Backend Validation

↓

Verify Password

↓

Generate JWT Token

↓

Return Token

↓

Store Token in Browser

↓

Dashboard Opens
```

---

## API

```http
POST /api/v1/auth/auth/login
```

---

# 4. Authentication Flow

Every protected endpoint requires authentication.

```text
Frontend

↓

Reads JWT Token

↓

Authorization Header

↓

Backend

↓

Verify Token

↓

Allow Request

↓

Return Response
```

Authorization Header

```http
Authorization: Bearer <JWT_TOKEN>
```

---

# 5. Customer Creation Flow

Administrators register customers after installation approval.

```text
Admin Dashboard

↓

Customer Form

↓

POST /customers

↓

Backend Validation

↓

Save Customer

↓

Database

↓

Success Response

↓

Dashboard Updates
```

---

# 6. Device Registration Flow

Each solar installation receives an IoT device.

```text
Administrator

↓

Device Form

↓

Enter Device Information

↓

POST /devices

↓

Backend

↓

Store Device

↓

Database

↓

Device Registered
```

---

# 7. Solar Installation Flow

```text
Customer Approved

↓

Site Inspection

↓

Solar Installation

↓

Battery Installation

↓

Inverter Installation

↓

ESP32 Installed

↓

Relay Installed

↓

Internet Connected

↓

MQTT Connected

↓

Ready for Activation
```

---

# 8. Subscription Workflow

Customers purchase an electricity subscription.

```text
Customer

↓

Choose Plan

↓

Monthly

Weekly

Daily

↓

Create Subscription

↓

Database

↓

Subscription Pending
```

---

# 9. Payment Workflow

Payments are processed securely through Paystack.

```text
Customer

↓

Click Pay

↓

Paystack Payment Page

↓

Card Payment

↓

Payment Success

↓

Paystack Callback

↓

Backend Verification

↓

Payment Stored

↓

Subscription Activated

↓

MQTT Command Sent

↓

ESP32 Activated

↓

Electricity Enabled
```

---

## APIs

```http
POST /payments/initialize

GET /payments/verify/{reference}
```

---

# 10. Device Activation Flow

```text
Administrator

↓

Activate Device

↓

POST /devices/{id}/activate

↓

Backend

↓

MQTT Publish

↓

ESP32

↓

Relay ON

↓

Electricity ON

↓

Status Updated
```

---

# 11. Device Deactivation Flow

```text
Administrator

↓

Deactivate Device

↓

POST /devices/{id}/deactivate

↓

MQTT

↓

ESP32

↓

Relay OFF

↓

Electricity OFF
```

---

# 12. Automatic Subscription Expiry Flow

```text
Scheduler

↓

Check Expired Subscriptions

↓

Subscription Expired?

↓

YES

↓

MQTT Publish

↓

ESP32

↓

Relay OFF

↓

Electricity Disabled

↓

Customer Notified
```

---

# 13. Telemetry Flow

The ESP32 continuously sends device information.

```text
ESP32

↓

Battery Reading

↓

Solar Voltage

↓

Load Voltage

↓

Temperature

↓

Relay Status

↓

MQTT Publish

↓

Backend

↓

Store in Database

↓

Dashboard Updates
```

---

## Example Telemetry

```json
{
    "battery":95,
    "solar_voltage":24.5,
    "load_voltage":220,
    "relay":"ON"
}
```

---

# 14. Notification Flow

```text
Event Happens

↓

Backend

↓

Create Notification

↓

Save Database

↓

Dashboard Notification

↓

Administrator Reads Notification
```

---

# 15. Reports Flow

```text
Administrator

↓

Dashboard

↓

GET /reports/dashboard

↓

Backend

↓

Count:

Customers

Devices

Payments

Waitlist

↓

Return Statistics

↓

Dashboard Cards Updated
```

---

# 16. Health Check Flow

```text
Browser

↓

GET /health

↓

Backend

↓

Database Check

↓

Return Status

↓

Healthy
```

---

# 17. Logout Flow

```text
Administrator

↓

Logout Button

↓

Delete JWT Token

↓

Redirect Login

↓

Access Removed
```

---

# Complete End-to-End Workflow

```text
Visitor

↓

Website

↓

Waitlist Registration

↓

Admin Reviews Waitlist

↓

Customer Contacted

↓

Site Inspection

↓

Solar Installation

↓

ESP32 Installed

↓

Device Registered

↓

Customer Created

↓

Subscription Purchased

↓

Payment Processed

↓

Payment Verified

↓

Subscription Activated

↓

MQTT Command Sent

↓

ESP32 Receives Command

↓

Relay Turns ON

↓

Electricity Delivered

↓

ESP32 Sends Telemetry

↓

Backend Stores Data

↓

Dashboard Displays Live Status
```

---

# Summary of Workflows

| Workflow | Status |
|-----------|--------|
| Waitlist Registration | ✅ Implemented |
| User Authentication | ✅ Implemented |
| Customer Management | ✅ Implemented |
| Device Registration | ✅ Implemented |
| Subscription Management | ✅ Implemented |
| Payment Processing | ✅ Implemented |
| Reports Dashboard | ✅ Implemented |
| Notifications | ✅ Implemented |
| Telemetry Collection | ✅ Implemented |
| MQTT Communication | ✅ Backend Ready |
| ESP32 Integration | 🚧 Firmware In Progress |
| Automatic Device Control | 🚧 Next Phase |

---

# Conclusion

The XSOLA platform follows a clear and modular workflow from user interaction through backend processing to physical device control. Each workflow is isolated, secure, and designed to scale as the platform grows. By combining REST APIs, PostgreSQL, MQTT messaging, and ESP32 hardware, XSOLA delivers a seamless end-to-end solution for subscription-based solar energy management.
