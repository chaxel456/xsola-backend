# XSOLA Project Overview

## Introduction

XSOLA is a Smart Solar Energy Management Platform designed to provide reliable, affordable, and remotely managed solar electricity to homes, businesses, schools, hostels, and rural communities. The platform combines modern web technologies, cloud computing, IoT (Internet of Things), smart metering, and digital payments into one complete ecosystem.

Unlike traditional solar installations where users purchase systems outright, XSOLA introduces a flexible subscription-based model that allows customers to pay periodically while the company remotely manages and monitors each installed solar system.

The platform consists of three major components:

- Frontend Web Application
- Backend REST API
- Smart IoT Hardware (ESP32)

These components work together to automate customer management, payment processing, device monitoring, energy control, and business reporting.

---

# Vision

To become Africa's leading intelligent solar energy platform by making clean, reliable, and affordable electricity accessible to everyone through smart technology.

---

# Mission

Our mission is to bridge the electricity gap by combining renewable energy, cloud computing, IoT, and digital payment technologies into a unified platform that delivers dependable power with seamless remote management.

---

# Core Goals

The primary goals of XSOLA include:

- Provide affordable access to solar energy.
- Reduce dependence on unstable national power grids.
- Enable remote monitoring of installed solar systems.
- Automate customer subscriptions and billing.
- Improve operational efficiency through centralized management.
- Enable real-time device communication.
- Deliver actionable business insights through analytics and reporting.
- Support scalable deployment across multiple cities and countries.

---

# Problems XSOLA Solves

Many homes and businesses experience unreliable electricity, making daily operations difficult. Traditional solar systems also come with high upfront costs and limited remote management capabilities.

XSOLA addresses these challenges by solving the following problems:

## Unstable Electricity Supply

Customers receive uninterrupted solar-powered electricity.

---

## High Installation Cost

Instead of paying the full installation cost upfront, customers can subscribe through flexible payment plans.

---

## Lack of Remote Management

Administrators can remotely monitor and control customer devices from a centralized dashboard.

---

## Manual Customer Management

The system automates customer registration, subscription management, and record keeping.

---

## Difficult Payment Tracking

Payments are processed digitally and automatically linked to customer subscriptions.

---

## Equipment Monitoring

Real-time telemetry allows administrators to monitor battery voltage, inverter status, solar performance, and device health.

---

## Delayed Fault Detection

Hardware problems can be identified immediately using telemetry data, allowing faster maintenance.

---

# Business Model

XSOLA operates as a Solar-as-a-Service (SaaS + Energy) platform.

Instead of selling solar systems outright, customers subscribe to receive continuous electricity.

Revenue sources include:

- Monthly subscriptions
- Weekly subscriptions
- Daily energy plans
- Installation fees
- Equipment maintenance
- Premium support
- Commercial energy packages
- Institutional solar deployments

---

# Target Users

XSOLA is designed for various customer categories.

## Residential Homes

Families requiring reliable electricity.

---

## Students

Hostels and student accommodations requiring uninterrupted power.

---

## Small Businesses

Shops, salons, restaurants, pharmacies, cyber cafés, and retail stores.

---

## Schools

Primary schools, secondary schools, and higher institutions.

---

## Hospitals

Clinics and healthcare facilities requiring uninterrupted electricity.

---

## Religious Organizations

Churches, mosques, and event centers.

---

## Rural Communities

Communities without reliable access to the national power grid.

---

## Corporate Organizations

Businesses requiring monitored backup energy systems.

---

# System Components

The XSOLA ecosystem consists of three major systems.

## 1. Frontend

The frontend provides the user interface.

Features include:

- Landing page
- Waitlist registration
- Administrator login
- Dashboard
- Customer management
- Device management
- Payment management
- Reports
- Notifications

Technologies:

- HTML5
- CSS3
- JavaScript

---

## 2. Backend

The backend provides the business logic and APIs.

Responsibilities include:

- Authentication
- Customer management
- Device management
- Waitlist management
- Subscription management
- Payment processing
- Telemetry storage
- Notifications
- Reports
- MQTT communication

Technologies:

- FastAPI
- SQLAlchemy
- PostgreSQL
- JWT Authentication
- MQTT
- APScheduler

---

## 3. IoT Hardware

The IoT hardware controls physical solar installations.

Components include:

- ESP32
- Relay Module
- Battery Monitoring
- Solar Charge Controller
- Inverter
- Smart Sensors

---

# How the System Works

The complete workflow begins when a customer visits the XSOLA website.

## Step 1

Customer opens the website.

↓

## Step 2

Customer joins the waitlist.

↓

## Step 3

Administrator reviews registrations.

↓

## Step 4

Customer is contacted.

↓

## Step 5

Solar system is installed.

↓

## Step 6

ESP32 device is configured.

↓

## Step 7

Device connects to the internet.

↓

## Step 8

Device connects to MQTT Broker.

↓

## Step 9

Backend begins monitoring telemetry.

↓

## Step 10

Customer subscribes to an energy plan.

↓

## Step 11

Payment is completed.

↓

## Step 12

Backend verifies payment.

↓

## Step 13

Subscription becomes active.

↓

## Step 14

Backend sends activation command.

↓

## Step 15

ESP32 receives command.

↓

## Step 16

Relay turns electricity ON.

↓

## Step 17

Customer receives electricity.

---

# Subscription Workflow

Customer

↓

Select Plan

↓

Payment

↓

Paystack

↓

Payment Verification

↓

Subscription Created

↓

MQTT Activation

↓

ESP32

↓

Relay ON

↓

Electricity Available

---

# Remote Device Management

Administrators can remotely:

- Activate devices
- Deactivate devices
- View battery levels
- Monitor solar charging
- View inverter status
- View customer subscriptions
- Detect offline devices
- Receive alerts
- Monitor telemetry
- Generate reports

---

# Key Features

Current implemented features include:

- User Authentication
- JWT Authorization
- Waitlist Management
- Customer Management
- Device Management
- Payment Module
- Subscription Management
- Telemetry Module
- Notification Module
- Dashboard Reports
- Health Monitoring
- API Documentation (Swagger)
- PostgreSQL Integration
- MQTT Client Integration
- Render Deployment
- Supabase PostgreSQL Database

---

# Technology Stack

## Frontend

- HTML5
- CSS3
- JavaScript

## Backend

- FastAPI
- Python
- SQLAlchemy
- Pydantic

## Database

- PostgreSQL
- Supabase

## Authentication

- JWT
- OAuth2 Password Flow
- Bcrypt Password Hashing

## Cloud

- Render
- GitHub

## Payments

- Paystack

## IoT

- ESP32
- MQTT

## Scheduling

- APScheduler

---

# Current Project Status

Completed:

- Backend API
- Database Integration
- Authentication System
- Waitlist Module
- Customer Module
- Device Module
- Payment Module
- Subscription Module
- Notification Module
- Reports Module
- Telemetry Module
- MQTT Client Setup
- Render Deployment
- API Documentation
- Supabase Database Integration

In Progress:

- Frontend Dashboard
- Waitlist Landing Page
- Admin Panel
- ESP32 Firmware
- MQTT Device Commands
- Automated Testing

Planned:

- Mobile Application
- AI Energy Analytics
- Smart Meter Integration
- SMS Notifications
- Email Notifications
- Offline Synchronization
- Multi-Branch Management
- Multi-Tenant Architecture
- Carbon Footprint Reporting

---

# Future Vision

The long-term vision for XSOLA is to become a complete Smart Energy Operating System capable of managing thousands of distributed solar installations across Africa.

Future capabilities will include:

- AI-powered energy optimization
- Predictive maintenance using machine learning
- Mobile applications for Android and iOS
- Smart prepaid metering
- Fleet management for field engineers
- GIS-based installation tracking
- Energy usage analytics
- Multi-country deployment
- Integration with additional payment providers
- Carbon credit and sustainability reporting
- Smart home integration
- Electric vehicle charging support

---

# Conclusion

XSOLA is more than a solar management application—it is an integrated renewable energy ecosystem that combines cloud computing, Internet of Things (IoT), secure payment processing, and intelligent device management into a single platform. By providing remote monitoring, automated subscriptions, digital payments, and real-time control of solar installations, XSOLA aims to improve access to reliable electricity while enabling scalable, efficient, and sustainable energy services across Africa.
