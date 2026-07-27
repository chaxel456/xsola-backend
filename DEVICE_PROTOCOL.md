# XSOLA Device Communication Protocol

Version: 1.0.0

Protocol: MQTT over TCP/IP

Encoding: UTF-8 JSON

Status: Stable

---

# Table of Contents

1. Introduction
2. Communication Architecture
3. Device Identity
4. MQTT Topics
5. Topic Naming Convention
6. Message Structure
7. Authentication
8. Device Registration
9. Device Status
10. Heartbeat Messages
11. Telemetry Messages
12. Remote Commands
13. Command Acknowledgements
14. Alerts
15. Error Messages
16. Firmware Updates
17. QoS Levels
18. Retained Messages
19. Security
20. Best Practices

---

# 1. Introduction

The XSOLA Device Protocol defines how smart solar devices communicate with the XSOLA cloud platform.

Communication is performed using MQTT.

Every message is encoded as JSON.

The protocol supports:

- Device registration
- Device authentication
- Telemetry
- Remote control
- Status monitoring
- Alerts
- Firmware updates

---

# 2. Communication Architecture

```
                    XSOLA Dashboard
                           │
                           ▼
                    FastAPI Backend
                           │
                           ▼
                     MQTT Broker
                           │
        ┌──────────────────┴──────────────────┐
        ▼                                     ▼
   ESP32 Device A                       ESP32 Device B
        │                                     │
        ▼                                     ▼
     Relay                              Relay
        │                                     │
        ▼                                     ▼
   Solar System                        Solar System
```

---

# 3. Device Identity

Every device has a globally unique identifier.

Example

```
device001
```

or

```
XSOLA-IMO-0001
```

Recommended format

```
XSOLA-<STATE>-<NUMBER>
```

Example

```
XSOLA-IMO-0001

XSOLA-LAG-0002

XSOLA-ABJ-0003
```

---

# 4. MQTT Topics

Each device uses dedicated topics.

| Purpose | Topic |
|----------|-------|
| Registration | xsola/device/{device_id}/register |
| Status | xsola/device/{device_id}/status |
| Heartbeat | xsola/device/{device_id}/heartbeat |
| Telemetry | xsola/device/{device_id}/telemetry |
| Command | xsola/device/{device_id}/control |
| Acknowledgement | xsola/device/{device_id}/ack |
| Alert | xsola/device/{device_id}/alert |
| Firmware | xsola/device/{device_id}/firmware |

Example

```
xsola/device/XSOLA-IMO-0001/telemetry
```

---

# 5. Topic Naming Convention

```
xsola

↓

device

↓

device_id

↓

service
```

Example

```
xsola/device/device001/control
```

---

# 6. JSON Message Format

Every packet follows the same structure.

```json
{
  "device_id": "XSOLA-IMO-0001",
  "timestamp": "2026-07-27T14:30:00Z",
  "message_type": "telemetry",
  "payload": {}
}
```

Fields

| Field | Description |
|--------|-------------|
| device_id | Unique device identifier |
| timestamp | ISO 8601 timestamp |
| message_type | Packet type |
| payload | Message data |

---

# 7. Device Authentication

During initial connection the device sends:

```json
{
  "device_id": "XSOLA-IMO-0001",
  "firmware_version": "1.0.0",
  "hardware_version": "1.0",
  "mac_address": "A4:CF:12:34:56:78"
}
```

Backend verifies:

- Device exists
- Device is active
- Device is authorized

If valid:

```
CONNECTED
```

Otherwise:

```
REJECTED
```

---

# 8. Device Registration

Topic

```
xsola/device/{device_id}/register
```

Payload

```json
{
  "device_id":"XSOLA-IMO-0001",
  "firmware":"1.0.0",
  "hardware":"ESP32",
  "ip":"192.168.1.50"
}
```

Backend Response

```json
{
  "status":"registered"
}
```

---

# 9. Device Status

Topic

```
status
```

Payload

```json
{
  "status":"online",
  "uptime":86400,
  "wifi_signal":-58
}
```

Possible status values

- online
- offline
- maintenance
- updating
- error

---

# 10. Heartbeat

Heartbeat is sent every 30–60 seconds.

Topic

```
heartbeat
```

Payload

```json
{
  "device_id":"XSOLA-IMO-0001",
  "status":"online",
  "free_memory":178240,
  "uptime":94520
}
```

If three consecutive heartbeats are missed, the backend marks the device as offline.

---

# 11. Telemetry

Telemetry reports sensor readings.

Topic

```
telemetry
```

Payload

```json
{
  "battery_voltage":25.4,
  "battery_current":18.2,
  "solar_voltage":41.8,
  "solar_current":12.7,
  "load_power":620,
  "temperature":31.6,
  "relay":"ON",
  "wifi_signal":-61
}
```

Telemetry interval:

- Every 30 seconds (default)
- Configurable by backend

---

# 12. Remote Commands

Topic

```
control
```

Example: Turn relay ON

```json
{
  "command":"relay_on"
}
```

Turn relay OFF

```json
{
  "command":"relay_off"
}
```

Restart device

```json
{
  "command":"restart"
}
```

Sync time

```json
{
  "command":"sync_time"
}
```

Update configuration

```json
{
  "command":"update_config",
  "config":{
    "telemetry_interval":60
  }
}
```

---

# 13. Command Acknowledgement

After executing a command, the device publishes an acknowledgement.

Topic

```
ack
```

Payload

```json
{
  "command":"relay_on",
  "status":"success",
  "timestamp":"2026-07-27T14:31:00Z"
}
```

Possible status values

- success
- failed
- rejected
- timeout

---

# 14. Alerts

Critical events are published immediately.

Examples

- Low battery
- Over-voltage
- Over-current
- High temperature
- Relay failure
- Wi-Fi disconnected
- Sensor failure

Payload

```json
{
  "alert":"low_battery",
  "value":20.8,
  "severity":"high"
}
```

---

# 15. Error Messages

```json
{
  "error":"sensor_not_found",
  "sensor":"INA219"
}
```

Common errors

- authentication_failed
- invalid_command
- relay_error
- sensor_failure
- mqtt_disconnected
- wifi_disconnected

---

# 16. Firmware Updates

Topic

```
firmware
```

Backend

```json
{
  "version":"1.1.0",
  "url":"https://downloads.xsola.com/fw/device001.bin",
  "checksum":"SHA256_HASH"
}
```

Device process

```
Download

↓

Verify checksum

↓

Install

↓

Restart

↓

Publish success
```

---

# 17. QoS Levels

| Message | QoS |
|----------|-----|
| Heartbeat | 0 |
| Telemetry | 1 |
| Commands | 1 |
| Alerts | 1 |
| Firmware | 2 |

---

# 18. Retained Messages

Retain:

- Last known status
- Last configuration

Do not retain:

- Telemetry
- Alerts
- Heartbeats

---

# 19. Security

Recommendations

- MQTT over TLS (Port 8883)
- Unique Client IDs
- Strong authentication
- Rotate credentials
- Validate all payloads
- Reject malformed JSON
- Encrypt sensitive configuration
- Restrict topic access using ACLs

---

# 20. Best Practices

- Publish telemetry at fixed intervals.
- Send heartbeat regularly.
- Acknowledge every command.
- Retry failed transmissions when appropriate.
- Synchronize time using NTP.
- Log significant events.
- Handle reconnects automatically after Wi-Fi or MQTT interruptions.

---

# Protocol Workflow

```
ESP32 Boots

↓

Connect Wi-Fi

↓

Connect MQTT Broker

↓

Register Device

↓

Authentication

↓

Heartbeat

↓

Telemetry

↓

Receive Commands

↓

Execute Command

↓

Send ACK

↓

Continue Monitoring
```

---

# Conclusion

The XSOLA Device Protocol provides a standardized, secure, and scalable communication layer between cloud services and embedded hardware. By defining MQTT topics, JSON message formats, command handling, acknowledgements, telemetry, and security practices, every XSOLA device can interoperate reliably with the backend while remaining extensible for future hardware and firmware enhancements.
