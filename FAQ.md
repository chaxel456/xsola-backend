# XSOLA Frequently Asked Questions (FAQ)

Version: 1.0.0

Project: XSOLA Smart Solar Energy Management Platform

Audience:
- Customers
- Developers
- Administrators
- Installers
- Support Engineers

---

# Table of Contents

1. General Questions
2. Customer Questions
3. Account Questions
4. Subscription Questions
5. Payment Questions
6. Device Questions
7. Technical Questions
8. Developer Questions
9. Administrator Questions
10. Security Questions
11. Deployment Questions
12. Hardware Questions
13. Troubleshooting Questions
14. Future Features

---

# 1. General Questions

## What is XSOLA?

XSOLA is a cloud-based Smart Solar Energy Management Platform that allows administrators and customers to manage solar energy systems remotely. It combines web technologies, cloud computing, IoT hardware, and payment automation into one integrated platform.

---

## What problems does XSOLA solve?

XSOLA helps solve several common challenges:

- Manual customer management
- Difficulty monitoring solar systems remotely
- Delayed payment verification
- Lack of remote device control
- Poor maintenance visibility
- No real-time telemetry
- Limited reporting and analytics

---

## Who can use XSOLA?

XSOLA is designed for:

- Solar installation companies
- Schools and universities
- Homes
- Small businesses
- Large enterprises
- Government organizations
- NGOs
- Rural electrification projects

---

# 2. Customer Questions

## How do I become a customer?

You can:

1. Join the waitlist.
2. Be approved by an administrator.
3. Receive a device installation.
4. Choose a subscription.
5. Complete payment.
6. Begin using the service.

---

## Can I monitor my solar system?

Yes.

Depending on your installation, you can monitor:

- Battery level
- Battery voltage
- Solar voltage
- Solar current
- Temperature
- Device status
- Power usage
- Energy generation

---

## Can I use XSOLA on my phone?

Yes.

XSOLA is designed to work in modern web browsers on:

- Android
- iPhone
- Tablets
- Windows PCs
- macOS computers

A dedicated mobile application is planned for a future release.

---

# 3. Account Questions

## How do I register?

If registration is enabled:

- Open the XSOLA website.
- Click **Sign Up**.
- Complete the registration form.
- Verify your account if required.

Some deployments may require an administrator to create customer accounts.

---

## I forgot my password.

Use the **Forgot Password** feature if available or contact your administrator for assistance.

---

## Can I change my email?

Yes.

Go to:

```
Profile

↓

Edit Profile

↓

Save
```

Some installations may require administrator approval.

---

# 4. Subscription Questions

## What subscription plans are available?

Subscription plans depend on the organization operating XSOLA.

Examples include:

- Daily
- Weekly
- Monthly
- Quarterly
- Annual

---

## What happens when my subscription expires?

When a subscription expires:

- Your account status changes to **Expired**.
- Access to services may be restricted.
- If configured, the backend can send a command through MQTT to disconnect the supported load until the subscription is renewed.

---

## Can I renew before expiry?

Yes.

Early renewal is supported and helps avoid service interruption.

---

# 5. Payment Questions

## Which payment gateway does XSOLA use?

XSOLA currently integrates with **Paystack** for payment processing.

Future versions may support additional payment providers.

---

## How do I know my payment was successful?

You will typically receive:

- A payment confirmation
- A receipt
- An updated subscription status
- A dashboard notification

---

## My payment was successful but my subscription is not active.

Possible causes:

- Webhook processing delay
- Network interruption
- Payment verification still pending

If the issue continues, contact support with your transaction reference.

---

# 6. Device Questions

## What hardware does XSOLA use?

Typical hardware includes:

- ESP32
- Relay module
- Battery sensors
- Voltage sensors
- Current sensors
- Solar inverter
- Battery bank
- Solar panels

---

## Why is my device offline?

Possible causes:

- No electrical power
- Wi-Fi unavailable
- Internet outage
- MQTT broker unavailable
- Hardware malfunction

---

## Can the administrator control my device remotely?

Yes, if your deployment supports remote control.

Administrators may send commands to:

- Turn supported loads ON or OFF
- Restart the device
- Update firmware
- Synchronize configuration

---

# 7. Technical Questions

## What backend framework does XSOLA use?

FastAPI.

---

## Which database is used?

PostgreSQL.

Supabase may be used as a managed PostgreSQL service.

---

## Which ORM is used?

SQLAlchemy.

---

## Which migration tool is used?

Alembic.

---

## Which communication protocol is used for devices?

MQTT.

---

## Which authentication method is used?

JWT (JSON Web Tokens).

---

# 8. Developer Questions

## Where is the API documentation?

Swagger UI

```
/docs
```

ReDoc

```
/redoc
```

---

## Which programming language is used?

Backend:

Python

Frontend:

HTML

CSS

JavaScript

Future versions may include React or Next.js.

---

## How are APIs organized?

Example:

```
/api/v1/auth

/api/v1/customers

/api/v1/devices

/api/v1/payments

/api/v1/reports
```

---

## Does XSOLA support Docker?

Yes.

Docker and Docker Compose are supported for containerized deployments.

---

# 9. Administrator Questions

## Can I create multiple administrators?

Yes, if your role has the required permissions.

---

## Can I export reports?

Yes.

Supported formats may include:

- CSV
- Excel
- PDF

---

## Can I monitor devices in real time?

Yes.

Telemetry is received from ESP32 devices through MQTT and displayed on the dashboard.

---

# 10. Security Questions

## Is my password stored in plain text?

No.

Passwords should be securely hashed before storage.

---

## Does XSOLA use HTTPS?

It should be deployed behind HTTPS in production environments.

---

## Are API requests authenticated?

Protected endpoints require a valid JWT bearer token.

Example:

```
Authorization: Bearer eyJhbGc...
```

---

# 11. Deployment Questions

## Where can XSOLA be deployed?

Examples include:

- Render
- AWS
- Azure
- DigitalOcean
- Railway
- Self-hosted servers

---

## Can I use Supabase?

Yes.

Supabase can provide a managed PostgreSQL database and additional services.

---

## Does XSOLA support Docker?

Yes.

Docker is recommended for consistent deployments across environments.

---

# 12. Hardware Questions

## Does XSOLA require an ESP32?

The reference implementation uses ESP32, but the platform can be adapted for other compatible microcontrollers with appropriate firmware.

---

## Which relay modules are supported?

Any relay module compatible with the selected ESP32 GPIO and electrical requirements can be used.

---

## Which sensors are supported?

Examples include:

- Voltage sensors
- Current sensors
- Temperature sensors
- Battery monitoring sensors

Support depends on the installed firmware.

---

# 13. Troubleshooting Questions

## The dashboard is blank.

Check:

- Backend availability
- Browser console
- Authentication token
- API connectivity

---

## Telemetry is not updating.

Verify:

- ESP32 power
- Wi-Fi connection
- MQTT broker
- Backend subscriber
- Sensor operation

---

## The backend will not start.

Check:

- Python installation
- Dependencies
- Environment variables
- Database connection
- Application logs

---

## I receive a 401 Unauthorized error.

Verify:

- Your JWT token has not expired.
- The Authorization header is correctly formatted.
- You are logged in.

---

# 14. Future Features

Planned enhancements include:

- Native Android application
- Native iOS application
- AI-powered energy analytics
- Smart battery optimization
- Predictive maintenance
- Multi-branch management improvements
- Carbon footprint reporting
- Multi-language support
- Offline synchronization
- Smart meter integration
- Advanced analytics dashboard
- Enhanced notification channels

---

# Quick Reference

| Question | Answer |
|----------|--------|
| Backend | FastAPI |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Authentication | JWT |
| Payment Gateway | Paystack |
| Device Communication | MQTT |
| Hardware | ESP32 |
| Deployment | Render, Docker, Cloud Providers |
| API Documentation | /docs, /redoc |

---

# Additional Help

If your question is not answered here:

1. Review the User Guide.
2. Review the Administrator Guide.
3. Check the API documentation.
4. Review the Troubleshooting Guide.
5. Contact your system administrator or support team.

---

# Conclusion

This FAQ provides quick answers to the most common questions about XSOLA. It is intended as a first point of reference for users, developers, administrators, and installers. For detailed procedures and technical implementation details, refer to the corresponding documentation in the `docs/` directory.
