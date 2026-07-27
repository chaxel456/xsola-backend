# XSOLA Monitoring Documentation

## Introduction

Monitoring is essential for ensuring the XSOLA platform remains healthy, secure, and reliable. It provides visibility into the performance of the backend, database, MQTT communication, ESP32 devices, scheduled tasks, and integrations with external services such as Paystack.

The goal of monitoring is to detect issues early, minimize downtime, and provide operational insight into the system.

---

# Monitoring Objectives

The XSOLA monitoring strategy aims to:

- Monitor API availability
- Monitor backend performance
- Monitor database health
- Monitor MQTT connectivity
- Monitor ESP32 device status
- Track scheduled jobs
- Detect failed payments
- Identify application errors
- Support troubleshooting
- Improve reliability

---

# Monitoring Architecture

```text
                 Users
                   │
                   ▼
             Frontend (HTML/CSS/JS)
                   │
                   ▼
             FastAPI Backend
         ┌─────────┼─────────┐
         ▼         ▼         ▼
      Logs     Metrics    Health Checks
         │         │         │
         └─────────┼─────────┘
                   ▼
          Monitoring Dashboard
                   │
        ┌──────────┼──────────┐
        ▼          ▼          ▼
   PostgreSQL    MQTT      Scheduler
        │          │          │
        ▼          ▼          ▼
     Alerts     ESP32     Notifications
```

---

# Components to Monitor

| Component | What to Monitor |
|-----------|-----------------|
| FastAPI | Availability, latency, errors |
| PostgreSQL | Connections, queries, storage |
| MQTT Broker | Connected clients, message throughput |
| ESP32 | Online status, heartbeat, telemetry |
| Scheduler | Successful and failed jobs |
| Paystack | Payment verification and webhook events |
| Frontend | API failures and loading times |

---

# Application Logging

Every significant event should be logged.

Examples:

- Application startup
- User login
- Failed login
- Customer creation
- Device registration
- Payment verification
- Subscription activation
- MQTT publish/subscribe
- Scheduler execution
- Unhandled exceptions

Recommended log levels:

| Level | Description |
|-------|-------------|
| DEBUG | Development information |
| INFO | Normal operations |
| WARNING | Potential issues |
| ERROR | Recoverable failures |
| CRITICAL | System failures |

---

# Health Checks

The backend should expose health endpoints.

Example:

```http
GET /health
```

Response:

```json
{
  "status": "healthy"
}
```

Additional checks may include:

- Database connectivity
- MQTT broker connectivity
- Scheduler status
- Disk space
- Memory usage

---

# API Monitoring

Track:

- Requests per minute
- Average response time
- Slow endpoints
- Error rate (4xx / 5xx)
- Authentication failures

Recommended metrics:

- Average latency
- 95th percentile latency
- Requests per second
- Active sessions

---

# Database Monitoring

Monitor:

- Active connections
- Slow queries
- Index usage
- Table size
- Disk utilization
- Replication status (future)

Alerts should be configured for:

- Connection failures
- High CPU usage
- Storage nearing capacity

---

# MQTT Monitoring

Track:

- Broker uptime
- Connected devices
- Messages published
- Messages received
- Failed publishes
- Topic activity

Important topics:

```text
xsola/device/{device_id}/control
xsola/device/{device_id}/telemetry
xsola/device/{device_id}/status
xsola/device/{device_id}/heartbeat
```

---

# ESP32 Monitoring

Each device should periodically publish a heartbeat.

Example payload:

```json
{
  "device_id": "device001",
  "status": "online",
  "timestamp": "2026-07-27T12:00:00Z"
}
```

Monitor:

- Last heartbeat
- Battery voltage
- Solar voltage
- Temperature
- Relay status
- Wi-Fi signal strength

If no heartbeat is received within the configured interval, mark the device as offline.

---

# Scheduler Monitoring

Track scheduled jobs such as:

- Subscription expiration checks
- Reminder notifications
- Report generation
- Cleanup tasks

Log:

- Start time
- End time
- Duration
- Status
- Errors

---

# Payment Monitoring

Monitor:

- Payment initialization
- Payment verification
- Webhook delivery
- Failed transactions
- Duplicate events

Log transaction references for traceability.

---

# Alerting

Configure alerts for:

- Backend unavailable
- Database unavailable
- MQTT broker offline
- Device offline
- Scheduler failures
- Payment verification failures
- High error rate

Alerts may be sent via:

- Email
- SMS
- Slack (future)
- Microsoft Teams (future)

---

# Dashboard Metrics

Suggested dashboard widgets:

- Total customers
- Active subscriptions
- Online devices
- Offline devices
- Today's revenue
- API uptime
- MQTT status
- Database status

---

# Log Retention

Recommendations:

- Development: 7 days
- Staging: 30 days
- Production: 90 days (or according to business requirements)

Archive older logs for auditing if necessary.

---

# Monitoring Tools (Future)

Recommended tools include:

- Prometheus
- Grafana
- Loki
- OpenTelemetry
- Sentry
- UptimeRobot
- Render Metrics

These can be introduced as the platform grows.

---

# Best Practices

- Monitor all critical services
- Centralize logs
- Set actionable alerts
- Review metrics regularly
- Test health endpoints
- Document incidents
- Perform periodic capacity reviews

---

# Conclusion

Effective monitoring ensures the XSOLA platform remains stable, secure, and responsive. By combining health checks, structured logging, metrics, alerts, and operational dashboards, administrators can quickly identify and resolve issues before they affect customers or connected solar systems.
