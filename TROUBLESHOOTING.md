# XSOLA Troubleshooting Guide

Version: 1.0.0

Project: XSOLA Smart Solar Energy Management Platform

Audience:
- Developers
- System Administrators
- DevOps Engineers
- IoT Engineers
- Support Team

---

# Table of Contents

1. Introduction
2. Troubleshooting Methodology
3. Backend Issues
4. Frontend Issues
5. Database Issues
6. Authentication Issues
7. MQTT Issues
8. ESP32 Issues
9. Device Control Issues
10. Payment Issues
11. Deployment Issues
12. Docker Issues
13. Render Issues
14. Supabase Issues
15. Network Issues
16. Performance Issues
17. Logging & Diagnostics
18. Emergency Recovery
19. Support Checklist

---

# 1. Introduction

This guide provides solutions for common issues that may occur during the development, deployment, and operation of the XSOLA platform.

Before making changes:

- Read the error message carefully.
- Check application logs.
- Verify configuration values.
- Confirm network connectivity.
- Test each component independently.

---

# 2. Troubleshooting Methodology

Follow this workflow:

```
Problem

↓

Identify Symptoms

↓

Check Logs

↓

Verify Configuration

↓

Test Individual Components

↓

Apply Fix

↓

Retest

↓

Document Resolution
```

---

# 3. Backend Issues

## Backend Does Not Start

### Symptoms

- Uvicorn exits immediately.
- Server fails to bind.
- Import errors.

### Possible Causes

- Missing dependencies
- Incorrect Python version
- Syntax errors
- Missing environment variables

### Solutions

Verify Python version

```bash
python --version
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run with detailed logs

```bash
uvicorn app.main:app --reload
```

---

## Port Already In Use

### Error

```
Address already in use
```

### Solution

Windows

```bash
netstat -ano | findstr :8000
```

Terminate the process

```bash
taskkill /PID <PID> /F
```

Linux

```bash
lsof -i :8000
kill -9 <PID>
```

---

## Internal Server Error (500)

Possible causes:

- Database failure
- Unhandled exception
- Missing environment variable

Actions:

- Check FastAPI logs.
- Review traceback.
- Verify database connectivity.
- Inspect recent code changes.

---

# 4. Frontend Issues

## API Requests Fail

### Symptoms

- Loading forever
- Fetch errors
- Network errors

### Verify

- API URL
- Backend is running
- Internet connection
- Browser console

Example

```javascript
const BASE_URL =
"https://xsola-backend.onrender.com";
```

---

## CORS Error

Example

```
Access to fetch blocked by CORS
```

Backend Fix

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
```

Use specific origins in production instead of `"*"`.

---

## Blank Dashboard

Possible Causes

- Invalid JWT
- API unavailable
- JavaScript error

Actions

- Open browser Developer Tools (F12).
- Check Console and Network tabs.
- Verify API responses.
- Confirm authentication token exists.

---

# 5. Database Issues

## Cannot Connect to PostgreSQL

### Error

```
connection refused
```

### Verify

- PostgreSQL service is running.
- DATABASE_URL is correct.
- Database exists.
- User permissions are valid.

Test

```bash
psql -U xsola_user -d xsola
```

---

## Migration Failure

Run

```bash
alembic current
```

Then

```bash
alembic upgrade head
```

If conflicts exist:

```bash
alembic history
```

Review migration files before modifying them.

---

## Duplicate Key Error

Example

```
duplicate key value violates unique constraint
```

Possible Causes

- Duplicate email
- Duplicate device ID

Solution

Validate uniqueness before inserting records.

---

# 6. Authentication Issues

## Invalid JWT

Symptoms

- Unauthorized (401)
- Login loop

Verify

- Token not expired.
- SECRET_KEY matches.
- Authorization header format.

Correct format

```
Authorization: Bearer eyJhbGc...
```

---

## Login Always Fails

Possible Causes

- Incorrect password
- User not found
- Password hash mismatch

Verify

- Stored password hash
- User record
- Password hashing logic

---

# 7. MQTT Issues

## Cannot Connect to Broker

Verify

- Broker hostname
- Port
- Firewall
- Internet access

Test

```bash
mosquitto_sub -t test
```

---

## Device Not Receiving Commands

Possible Causes

- Wrong topic
- Device offline
- Incorrect Client ID

Verify

```
xsola/device/device001/control
```

Confirm the ESP32 is subscribed to the correct topic.

---

## Telemetry Missing

Possible Causes

- ESP32 offline
- MQTT disconnected
- JSON parsing error

Check

- Broker logs
- ESP32 serial monitor
- Backend subscriber logs

---

# 8. ESP32 Issues

## Wi-Fi Connection Failed

Verify

```cpp
ssid
password
```

Check

- Signal strength
- Router availability
- DHCP assignment

---

## Continuous Restart

Possible Causes

- Insufficient power
- Watchdog timeout
- Memory overflow

Check

- Power supply
- Serial logs
- Heap memory

---

## Firmware Upload Failure

Verify

- Correct COM port
- USB cable supports data
- Board selected correctly in Arduino IDE or PlatformIO

---

# 9. Device Control Issues

## Relay Does Not Switch

Check

- GPIO wiring
- Relay module power
- Relay logic (HIGH/LOW)
- Backend command acknowledgement

Test relay independently before integrating with MQTT.

---

## Device Offline in Dashboard

Possible Causes

- Missing heartbeat
- Wi-Fi disconnected
- MQTT broker unavailable

Actions

- Check power.
- Verify Wi-Fi.
- Review heartbeat topic.

---

# 10. Payment Issues

## Payment Not Verified

Verify

- Paystack webhook URL
- Transaction reference
- Secret key
- Backend webhook logs

---

## Subscription Not Activated

Possible Causes

- Webhook failed
- Verification error
- Database update failed

Check

- Payment record
- Subscription table
- Application logs

---

# 11. Deployment Issues

## Application Fails After Deployment

Verify

- Environment variables
- Build logs
- Start command
- Dependencies

Example

```bash
uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

---

# 12. Docker Issues

## Container Exits Immediately

View logs

```bash
docker logs <container_id>
```

Verify

- Dockerfile
- Working directory
- Environment variables

---

## Cannot Build Image

Rebuild

```bash
docker build --no-cache -t xsola .
```

---

# 13. Render Issues

## Build Failed

Check

- Build command
- Python version
- requirements.txt

---

## Service Not Starting

Verify

- Start command
- Environment variables
- Port configuration

Render automatically assigns the application port through the `PORT` environment variable.

---

# 14. Supabase Issues

## Authentication Error

Verify

- Project URL
- API Key
- Database credentials

---

## Database Timeout

Check

- Active connections
- Query performance
- Network latency

---

# 15. Network Issues

## API Unreachable

Verify

- Internet connection
- DNS resolution
- HTTPS certificate
- Firewall rules

---

## MQTT Timeout

Check

- Broker status
- Network connectivity
- Keep Alive interval

---

# 16. Performance Issues

## Slow API Response

Investigate

- Database indexes
- Long-running queries
- External API calls
- Server resources

Recommended

- Optimize SQL queries.
- Add indexes.
- Cache frequently accessed data where appropriate.

---

## High Memory Usage

Check

- Memory leaks
- Background jobs
- Unreleased connections

Use profiling tools during development.

---

# 17. Logging & Diagnostics

Useful log sources

- FastAPI application logs
- Uvicorn logs
- PostgreSQL logs
- MQTT broker logs
- Render deployment logs
- ESP32 serial monitor

Helpful commands

```bash
docker logs container_name
```

```bash
journalctl -u mosquitto
```

---

# 18. Emergency Recovery

If the system experiences a critical failure:

1. Notify administrators.
2. Stop new deployments.
3. Back up the current database.
4. Restore from the latest verified backup if necessary.
5. Validate all services.
6. Monitor system health after recovery.
7. Record the incident and corrective actions.

---

# 19. Support Checklist

Before requesting support, collect:

- Error message
- Screenshots
- API endpoint (if applicable)
- Request payload
- Server logs
- Browser console output
- Database logs
- MQTT logs
- Device ID
- Firmware version
- Environment (Development/Production)
- Steps to reproduce

Providing this information will significantly reduce troubleshooting time.

---

# Quick Diagnostic Flow

```
Problem

↓

Frontend?

↓

Backend?

↓

Database?

↓

MQTT?

↓

ESP32?

↓

Payment?

↓

Deployment?

↓

Resolve

↓

Retest

↓

Document
```

---

# Conclusion

Effective troubleshooting depends on a structured approach. By isolating the affected component, reviewing logs, validating configuration, and testing each layer independently, most XSOLA issues can be resolved quickly and safely. This guide should be used alongside the Installation, Architecture, Monitoring, and API documentation when diagnosing production or development problems.
