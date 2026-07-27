# XSOLA Installation Guide

Version: 1.0.0

Project: XSOLA Smart Solar Energy Management Platform

Audience:
- Backend Developers
- Frontend Developers
- DevOps Engineers
- IoT Engineers
- System Administrators

---

# Table of Contents

1. Introduction
2. System Requirements
3. Project Structure
4. Clone the Repository
5. Backend Installation
6. Frontend Installation
7. PostgreSQL Setup
8. Supabase Setup
9. Environment Variables
10. Alembic Migration
11. Run the Backend
12. Run the Frontend
13. Docker Installation
14. MQTT Installation
15. ESP32 Setup
16. Paystack Configuration
17. Render Deployment
18. Production Checklist
19. Verification
20. Troubleshooting

---

# 1. Introduction

This guide explains how to install the complete XSOLA platform from scratch.

After completing this guide, you will have:

✔ Backend running

✔ Frontend running

✔ Database connected

✔ MQTT configured

✔ ESP32 connected

✔ Paystack configured

✔ Production deployment ready

---

# 2. System Requirements

## Minimum

OS

- Windows 10+
- Ubuntu 22.04+
- macOS 13+

RAM

```
8 GB
```

Storage

```
10 GB Free
```

Internet

Required

---

## Software

Python

```
3.12+
```

Node.js

```
20+
```

Git

Latest

Docker

Latest

VS Code

Recommended

Google Chrome

Recommended

---

# 3. Project Structure

```
xsola/

├── app/
├── docs/
├── frontend/
├── firmware/
├── tests/
├── docker/
├── scripts/
├── alembic/
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

# 4. Clone Repository

Clone from GitHub

```bash
git clone https://github.com/KingsagTech/xsola.git
```

Enter project

```bash
cd xsola
```

---

# 5. Backend Installation

Create virtual environment

Windows

```bash
python -m venv venv
```

Linux

```bash
python3 -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Linux

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Verify installation

```bash
pip list
```

Expected packages include

- FastAPI
- SQLAlchemy
- Alembic
- Uvicorn
- Pydantic
- psycopg2
- passlib
- python-jose
- APScheduler
- paho-mqtt

---

# 6. Frontend Installation

Go to frontend

```bash
cd frontend
```

Install dependencies (if using Node-based frontend)

```bash
npm install
```

Run development server

```bash
npm run dev
```

For the current HTML/CSS/JavaScript version, you can simply open `index.html` with a local development server such as VS Code Live Server.

---

# 7. PostgreSQL Setup

Install PostgreSQL.

Create database

```sql
CREATE DATABASE xsola;
```

Create user

```sql
CREATE USER xsola_user WITH PASSWORD 'StrongPassword';
```

Grant privileges

```sql
GRANT ALL PRIVILEGES ON DATABASE xsola TO xsola_user;
```

---

# 8. Supabase Setup

Create account

https://supabase.com

Create project

↓

Copy

- Project URL
- Database URL
- API Key

Save them inside

```
.env
```

---

# 9. Environment Variables

Create

```
.env
```

Example

```env
APP_NAME=XSOLA

DATABASE_URL=postgresql://user:password@localhost/xsola

SECRET_KEY=CHANGE_THIS_SECRET

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=60

SUPABASE_URL=https://project.supabase.co

SUPABASE_KEY=xxxxxxxx

MQTT_BROKER=broker.hivemq.com

MQTT_PORT=1883

PAYSTACK_SECRET_KEY=sk_test_xxxxx

PAYSTACK_PUBLIC_KEY=pk_test_xxxxx
```

---

# 10. Run Database Migration

Generate migrations

```bash
alembic revision --autogenerate -m "Initial migration"
```

Apply migrations

```bash
alembic upgrade head
```

Verify tables

```sql
SELECT * FROM users;
```

---

# 11. Run Backend

Development

```bash
uvicorn app.main:app --reload
```

Production

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Open

```
http://localhost:8000
```

Swagger

```
http://localhost:8000/docs
```

ReDoc

```
http://localhost:8000/redoc
```

---

# 12. Run Frontend

HTML Version

Open

```
index.html
```

or

Use VS Code Live Server

```
http://127.0.0.1:5500
```

If using React

```bash
npm run dev
```

---

# 13. Docker Installation

Build image

```bash
docker build -t xsola .
```

Run container

```bash
docker run -p 8000:8000 xsola
```

Docker Compose

```bash
docker-compose up
```

Stop

```bash
docker-compose down
```

---

# 14. MQTT Setup

Install Mosquitto

Ubuntu

```bash
sudo apt install mosquitto
```

Windows

Download

https://mosquitto.org

Start Broker

```bash
mosquitto
```

Test publish

```bash
mosquitto_pub -t test -m "Hello XSOLA"
```

Test subscribe

```bash
mosquitto_sub -t test
```

---

# 15. ESP32 Setup

Install

Arduino IDE

or

PlatformIO

Install libraries

- WiFi
- PubSubClient
- ArduinoJson

Configure

```cpp
const char* ssid="YOUR_WIFI";

const char* password="YOUR_PASSWORD";

const char* mqtt_server="broker.hivemq.com";
```

Upload firmware

↓

ESP32 connects

↓

MQTT

↓

XSOLA

---

# 16. Paystack Configuration

Login

https://paystack.com

Copy

- Public Key
- Secret Key

Add to

```
.env
```

Webhook URL

```
https://your-backend/api/v1/payments/webhook
```

---

# 17. Render Deployment

Push code

```bash
git add .

git commit -m "Deploy XSOLA"

git push origin main
```

Open

https://render.com

Create

↓

Web Service

↓

Connect GitHub

↓

Select Repository

↓

Build Command

```bash
pip install -r requirements.txt
```

Start Command

```bash
uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

Add Environment Variables

↓

Deploy

---

# 18. Production Checklist

Backend

✔ Environment variables configured

✔ Database connected

✔ HTTPS enabled

✔ JWT configured

✔ MQTT configured

✔ Logging enabled

✔ Backups configured

Frontend

✔ API URL configured

✔ HTTPS enabled

✔ Responsive UI tested

Database

✔ Migrations applied

✔ Indexes created

✔ Backups scheduled

IoT

✔ ESP32 online

✔ MQTT connected

✔ Relay tested

✔ Sensors calibrated

---

# 19. Verification

Backend

```
http://localhost:8000/docs
```

Should open Swagger UI.

Frontend

```
http://127.0.0.1:5500
```

Should display the XSOLA landing page.

Database

```sql
SELECT COUNT(*) FROM users;
```

MQTT

Receive heartbeat messages from ESP32.

Paystack

Complete a test transaction and verify the subscription updates correctly.

---

# 20. Troubleshooting

## Backend won't start

Check:

- Python version
- Installed packages
- `.env` values
- Database connection

---

## Frontend cannot connect

Verify:

- API URL
- CORS configuration
- Browser console errors

---

## Database connection error

Check:

- PostgreSQL running
- DATABASE_URL
- User permissions

---

## MQTT not working

Verify:

- Broker address
- Port
- Internet connection
- Firewall settings

---

## ESP32 Offline

Check:

- Power supply
- Wi-Fi credentials
- MQTT broker
- Firmware logs

---

## Paystack webhook not received

Verify:

- Webhook URL
- Secret key
- Public endpoint
- Backend logs

---

# Installation Workflow

```
Install Git

↓

Clone Repository

↓

Install Python

↓

Install Dependencies

↓

Configure .env

↓

Create Database

↓

Run Alembic

↓

Run FastAPI

↓

Run Frontend

↓

Configure MQTT

↓

Upload ESP32 Firmware

↓

Connect Paystack

↓

Deploy to Render

↓

Production Ready
```

---

# Conclusion

Following this guide installs the complete XSOLA ecosystem, including the backend, frontend, database, MQTT communication layer, ESP32 firmware environment, payment gateway, and deployment pipeline. After installation, the platform is ready for development, testing, and production deployment.
