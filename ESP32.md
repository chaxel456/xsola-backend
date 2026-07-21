# XSOLA ESP32 Firmware & Hardware Documentation

## Introduction

The ESP32 is the intelligent controller installed inside every XSOLA solar installation. It serves as the bridge between the XSOLA cloud platform and the physical solar hardware, enabling remote monitoring, control, and automation.

The ESP32 continuously communicates with the XSOLA backend through MQTT over Wi-Fi, allowing administrators to remotely activate or deactivate power, collect telemetry, detect faults, and monitor system health.

---

# Role of the ESP32

The ESP32 is responsible for:

- Connecting to Wi-Fi
- Connecting to the MQTT Broker
- Receiving commands from the backend
- Controlling relay modules
- Reading sensors
- Monitoring battery voltage
- Monitoring solar charging
- Monitoring inverter status
- Sending telemetry
- Reporting faults
- Reporting device status
- Receiving firmware updates (future)

---

# System Overview

```text
                    XSOLA Backend
                           │
                     MQTT Broker
                           │
                     Internet (Wi-Fi)
                           │
                      ESP32 Controller
         ┌───────────┬───────────┬────────────┐
         ▼           ▼           ▼            ▼
      Relay      Sensors     Battery     Inverter
         │
         ▼
   Customer Electricity
```

---

# Hardware Components

A complete XSOLA IoT controller consists of:

| Component | Purpose |
|------------|----------|
| ESP32 Dev Board | Main controller |
| Relay Module | Controls power output |
| Battery Sensor | Battery monitoring |
| Voltage Sensor | Solar voltage measurement |
| Current Sensor | Power consumption |
| Temperature Sensor | Equipment temperature |
| Wi-Fi Antenna | Internet communication |
| Status LEDs | Device indicators |
| DC Power Supply | ESP32 power source |

---

# Recommended Hardware

## ESP32

Recommended board

```
ESP32-WROOM-32
```

Specifications

- Dual-core CPU
- Wi-Fi
- Bluetooth
- 520 KB RAM
- Multiple GPIO Pins
- ADC Inputs
- PWM Outputs
- Low Power Consumption

---

# Relay Module

The relay physically controls electricity.

```
Backend

↓

MQTT

↓

ESP32

↓

Relay

↓

Electricity ON/OFF
```

Relay Types

- 5V Relay
- Solid State Relay (Recommended)
- Industrial Contactors

---

# Sensors

## Battery Sensor

Measures:

- Battery Voltage
- Battery Percentage

Example

```
Battery

↓

Voltage Divider

↓

ADC Pin

↓

ESP32
```

---

## Solar Panel Voltage

Measures

- Solar Voltage
- Charging Voltage

---

## Current Sensor

Examples

- ACS712
- INA219

Measures

- Charging Current
- Load Current

---

## Temperature Sensor

Recommended

```
DS18B20

or

DHT22
```

Used to detect overheating.

---

# GPIO Connections

Example

| ESP32 Pin | Device |
|------------|---------|
| GPIO26 | Relay |
| GPIO34 | Battery Sensor |
| GPIO35 | Solar Voltage |
| GPIO32 | Current Sensor |
| GPIO4 | Status LED |
| GPIO2 | Wi-Fi LED |

---

# Wi-Fi Connection

The ESP32 connects to the customer's Wi-Fi.

Workflow

```text
Power On

↓

Load Wi-Fi Credentials

↓

Connect Router

↓

Receive IP Address

↓

Connect Internet

↓

Connect MQTT
```

---

# MQTT Connection

Broker

```
broker.xsola.com
```

Example

```cpp
client.connect("device001");
```

After connecting:

Subscribe

```
xsola/device/device001/control
```

Publish

```
xsola/device/device001/telemetry
```

---

# Firmware Architecture

The firmware follows a modular design.

```text
main.cpp

│

├── WiFi Manager

├── MQTT Client

├── Relay Controller

├── Sensor Manager

├── Telemetry Manager

├── Device Manager

├── OTA Manager

└── Logger
```

Each module performs a dedicated function.

---

# Firmware Workflow

```text
Power ON

↓

Initialize Hardware

↓

Connect Wi-Fi

↓

Connect MQTT Broker

↓

Subscribe Topics

↓

Read Sensors

↓

Publish Telemetry

↓

Listen for Commands

↓

Execute Commands

↓

Repeat Forever
```

---

# Command Processing

The backend publishes commands.

Example Topic

```
xsola/device/device001/control
```

Payload

```json
{
    "action":"ON"
}
```

ESP32

↓

Receive Message

↓

Parse JSON

↓

Switch Relay

↓

Publish Confirmation

---

# Relay Control

Example

```cpp
if(action=="ON")
{
    digitalWrite(RELAY_PIN,HIGH);
}
```

OFF

```cpp
digitalWrite(RELAY_PIN,LOW);
```

---

# Telemetry

Telemetry is published periodically.

Topic

```
xsola/device/device001/telemetry
```

Example

```json
{
    "device_id":"device001",
    "battery":94,
    "solar_voltage":24.6,
    "current":5.2,
    "temperature":31,
    "relay":"ON",
    "signal":-62
}
```

---

# Heartbeat

Every device periodically announces that it is online.

Topic

```
xsola/device/device001/heartbeat
```

Payload

```json
{
    "status":"alive",
    "uptime":3600
}
```

---

# Device Status

Topic

```
xsola/device/device001/status
```

Payload

```json
{
    "status":"ONLINE"
}
```

Offline

```json
{
    "status":"OFFLINE"
}
```

---

# Fault Detection

The ESP32 detects:

- Low Battery
- High Temperature
- Sensor Failure
- Wi-Fi Loss
- MQTT Disconnect
- Relay Failure
- Low Solar Voltage

Example Alert

```json
{
    "alert":"LOW_BATTERY",
    "battery":18
}
```

---

# Automatic Recovery

If Wi-Fi disconnects

```text
Lost Wi-Fi

↓

Retry Connection

↓

Reconnect MQTT

↓

Resume Telemetry
```

If MQTT disconnects

```text
Retry

↓

Reconnect

↓

Resubscribe Topics
```

---

# Over-the-Air (OTA) Updates

Future versions will support OTA firmware updates.

Workflow

```text
Administrator

↓

Upload Firmware

↓

Backend

↓

MQTT Notification

↓

ESP32 Downloads Firmware

↓

Verify

↓

Install

↓

Restart
```

---

# Security

Each ESP32 should use:

- Unique Device ID
- MQTT Username
- MQTT Password
- TLS Encryption
- Secure Firmware
- Flash Encryption (optional)
- Secure Boot (optional)

---

# Power Supply

Recommended

- 5V DC Regulated Supply
- Battery Backup
- Surge Protection

---

# Installation Workflow

```text
Install Solar Panels

↓

Install Battery

↓

Install Inverter

↓

Install Relay

↓

Install ESP32

↓

Connect Sensors

↓

Power Device

↓

Configure Wi-Fi

↓

Connect MQTT

↓

Activate Device

↓

Ready
```

---

# Maintenance

Regular maintenance should include:

- Firmware updates
- Wi-Fi signal check
- Relay inspection
- Battery calibration
- Sensor verification
- MQTT connectivity test
- Power supply inspection

---

# Future Enhancements

- GSM Backup Communication
- LoRaWAN Support
- LTE Module
- GPS Tracking
- AI Fault Detection
- Smart Meter Integration
- Bluetooth Provisioning
- Edge Computing
- Local Data Caching

---

# Conclusion

The ESP32 is the core IoT controller within the XSOLA platform. By combining Wi-Fi connectivity, MQTT messaging, relay control, sensor monitoring, and modular firmware, it enables real-time remote management of solar installations. This architecture provides a scalable, secure, and reliable foundation for intelligent energy delivery, monitoring, and automation across residential, commercial, and institutional deployments.
