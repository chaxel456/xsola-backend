# XSOLA MQTT Documentation

## Introduction

MQTT (Message Queuing Telemetry Transport) is the communication protocol used by XSOLA to enable real-time messaging between the cloud backend and ESP32 devices installed at customer locations.

Unlike HTTP, MQTT is lightweight, efficient, and designed specifically for Internet of Things (IoT) applications where devices may have limited bandwidth and processing power.

Within XSOLA, MQTT enables the backend to remotely activate or deactivate solar systems, receive telemetry from devices, monitor equipment health, and issue commands without requiring constant polling.

---

# Why MQTT?

MQTT was selected because it provides:

- Low bandwidth usage
- Low latency communication
- Reliable message delivery
- Support for unreliable network connections
- Publish/Subscribe architecture
- Scalability to thousands of devices
- Real-time communication

---

# MQTT Architecture

```text
                   XSOLA Backend
                         │
                  MQTT Client
                         │
                         ▼
                MQTT Broker
         (HiveMQ / EMQX / Mosquitto)
                         │
         ┌───────────────┼───────────────┐
         ▼               ▼               ▼
     ESP32 #1        ESP32 #2       ESP32 #3
         │               │               │
      Relay          Relay          Relay
         │               │               │
    Solar System    Solar System    Solar System
```

The broker acts as the central message hub. Devices never communicate directly with one another—they exchange messages through the broker.

---

# MQTT Components

## Publisher

A publisher sends messages to a topic.

Examples:

- XSOLA Backend
- ESP32 Device

---

## Subscriber

A subscriber receives messages from a topic.

Examples:

- ESP32
- XSOLA Backend

---

## Broker

The broker routes messages between publishers and subscribers.

Recommended brokers:

- HiveMQ
- EMQX
- Eclipse Mosquitto
- AWS IoT Core
- Azure IoT Hub

---

# MQTT Topics

Topics define communication channels.

## Device Control

```text
xsola/device/{device_id}/control
```

Example

```text
xsola/device/device001/control
```

Backend publishes commands here.

ESP32 subscribes.

---

## Device Status

```text
xsola/device/{device_id}/status
```

Example

```text
xsola/device/device001/status
```

ESP32 publishes online/offline status.

Backend subscribes.

---

## Telemetry

```text
xsola/device/{device_id}/telemetry
```

Example

```text
xsola/device/device001/telemetry
```

ESP32 publishes battery and sensor data.

Backend subscribes.

---

## Alerts

```text
xsola/device/{device_id}/alerts
```

Examples

- Low battery
- High temperature
- Relay fault
- WiFi disconnected

---

## Heartbeat

```text
xsola/device/{device_id}/heartbeat
```

Published periodically to indicate that the device is alive.

---

# Publish Example

Topic

```text
xsola/device/device001/control
```

Payload

```json
{
    "action":"ON"
}
```

---

Deactivate

```json
{
    "action":"OFF"
}
```

---

Restart

```json
{
    "action":"RESTART"
}
```

---

Firmware Update

```json
{
    "action":"UPDATE"
}
```

---

# Telemetry Example

Topic

```text
xsola/device/device001/telemetry
```

Payload

```json
{
    "device_id":"device001",
    "battery":96,
    "solar_voltage":24.7,
    "load_voltage":220,
    "temperature":33,
    "relay":"ON",
    "signal":-59,
    "timestamp":"2026-07-20T12:00:00Z"
}
```

---

# Device Status Message

```json
{
    "device_id":"device001",
    "status":"ONLINE"
}
```

---

# Heartbeat Example

```json
{
    "device_id":"device001",
    "heartbeat":"alive",
    "uptime":987654
}
```

---

# Publish Flow

```text
Administrator

↓

Dashboard

↓

FastAPI Backend

↓

MQTT Publish

↓

Broker

↓

ESP32

↓

Relay ON
```

---

# Subscribe Flow

```text
ESP32

↓

Telemetry

↓

Broker

↓

Backend

↓

Database

↓

Dashboard
```

---

# Quality of Service (QoS)

MQTT supports three delivery levels.

## QoS 0

At most once.

- Fastest
- No acknowledgement
- Suitable for non-critical telemetry

---

## QoS 1

At least once.

- Guaranteed delivery
- Duplicate messages possible

Recommended for:

- Relay commands
- Device status

---

## QoS 2

Exactly once.

Highest reliability.

Recommended for:

- Firmware updates
- Critical control operations

---

# Retained Messages

A retained message remains stored by the broker.

When a device reconnects, it immediately receives the last retained command.

Example

```json
{
    "action":"OFF"
}
```

If retained, a reconnecting ESP32 immediately knows the desired relay state.

---

# Last Will and Testament (LWT)

LWT allows the broker to notify the backend if a device disconnects unexpectedly.

Example topic

```text
xsola/device/device001/status
```

Payload

```json
{
    "status":"OFFLINE"
}
```

---

# Backend MQTT Workflow

```text
API Request

↓

Service Layer

↓

MQTT Client

↓

Broker

↓

ESP32

↓

Relay

↓

Confirmation

↓

Database Update
```

---

# ESP32 MQTT Workflow

```text
Power On

↓

Connect WiFi

↓

Connect MQTT Broker

↓

Subscribe Topics

↓

Receive Commands

↓

Execute Action

↓

Publish Telemetry

↓

Repeat
```

---

# Security

Recommended security measures:

- MQTT username/password authentication
- TLS encryption
- Topic-level access control
- Unique device credentials
- Secure broker configuration
- Certificate-based authentication (production)

---

# Error Handling

The backend should handle:

- Broker unavailable
- Device offline
- Publish timeout
- Subscription failure
- Invalid payloads
- Duplicate messages

---

# Best Practices

- Use meaningful topic names
- Keep payloads compact
- Validate all incoming data
- Reconnect automatically after network loss
- Use QoS appropriately
- Avoid unnecessary retained messages
- Monitor broker performance
- Log publish and subscribe events

---

# Future Enhancements

- Device groups
- Broadcast commands
- OTA firmware updates
- End-to-end encryption
- MQTT over WebSockets
- Multi-broker clustering
- Device provisioning
- Certificate-based authentication

---

# Conclusion

MQTT is the communication backbone of the XSOLA IoT ecosystem. It provides reliable, scalable, and low-latency messaging between the FastAPI backend and ESP32 devices, enabling real-time monitoring, remote device control, telemetry collection, and automated energy management.
