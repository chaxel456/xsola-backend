# XSOLA Administrator Guide

Version: 1.0.0

Project: XSOLA Smart Solar Energy Management Platform

Audience: System Administrators, Operations Managers, Support Engineers

---

# Table of Contents

1. Introduction
2. Administrator Responsibilities
3. Administrator Roles
4. Logging In
5. Dashboard Overview
6. Managing Users
7. Managing Waitlist
8. Managing Customers
9. Managing Devices
10. Managing Subscriptions
11. Managing Payments
12. Monitoring Telemetry
13. Managing Notifications
14. Reports and Analytics
15. Remote Device Control
16. System Settings
17. Security Best Practices
18. Daily Operations
19. Weekly Maintenance
20. Monthly Maintenance
21. Backup Procedures
22. Incident Response
23. Troubleshooting
24. Administrator Checklist

---

# 1. Introduction

The XSOLA Administrator Guide provides instructions for managing the XSOLA platform.

Administrators are responsible for:

- Managing customers
- Registering devices
- Monitoring solar systems
- Processing subscriptions
- Reviewing payments
- Monitoring telemetry
- Generating reports
- Responding to alerts
- Maintaining system security

---

# 2. Administrator Responsibilities

An administrator is expected to:

- Monitor system health
- Ensure devices remain online
- Verify successful payments
- Activate customer subscriptions
- Resolve customer issues
- Review reports
- Monitor hardware performance
- Maintain database integrity

---

# 3. Administrator Roles

## Super Administrator

Has unrestricted access.

Permissions:

- Manage all users
- Create administrators
- Delete administrators
- Configure system settings
- Access all reports
- Manage hardware
- Manage payments
- View logs

---

## Branch Administrator

Manages a specific branch.

Permissions:

- Register customers
- Register devices
- Activate subscriptions
- View reports
- Monitor telemetry
- Process customer requests

Cannot:

- Change system settings
- Delete administrators
- Modify global configuration

---

## Support Officer

Permissions:

- View customer information
- View devices
- Monitor alerts
- Assist customers
- Create support notes

Cannot:

- Delete data
- Modify subscriptions
- Change payment records

---

# 4. Logging In

Open

```
https://admin.xsola.com
```

Enter:

- Email
- Password

Click

```
Login
```

Backend Flow

```
Login Form

↓

FastAPI

↓

JWT Generated

↓

Dashboard Opens
```

---

# 5. Dashboard Overview

The dashboard displays:

- Total Customers
- Total Devices
- Active Devices
- Offline Devices
- Total Revenue
- Active Subscriptions
- Expired Subscriptions
- Waitlist Members
- Battery Alerts
- System Notifications

Example

```
Customers

152

Devices

148

Online

146

Offline

2

Revenue

₦2,500,000
```

---

# 6. Managing Users

Navigate to

```
Administration

↓

Users
```

Available actions:

- Add User
- Edit User
- Disable User
- Reset Password
- Delete User

---

# 7. Managing Waitlist

Navigate to

```
Dashboard

↓

Waitlist
```

Available actions

- View applicants
- Search
- Export CSV
- Contact applicant
- Convert to Customer
- Delete entry

Workflow

```
Waitlist

↓

Qualified

↓

Customer

↓

Subscription
```

---

# 8. Managing Customers

Navigate

```
Customers
```

Available Operations

- Add Customer
- Edit Customer
- Delete Customer
- Suspend Customer
- Search Customer
- View History

Customer Profile

- Name
- Phone
- Email
- Address
- Branch
- Installed Device
- Subscription
- Payment History

---

# 9. Managing Devices

Navigate

```
Devices
```

Information Available

- Device ID
- Firmware Version
- Last Seen
- Battery Voltage
- Solar Voltage
- Temperature
- Wi-Fi Signal
- Relay Status
- Device Status

Actions

- Register
- Assign Customer
- Restart
- Update Firmware
- Activate
- Deactivate
- Delete

---

# 10. Managing Subscriptions

Navigate

```
Subscriptions
```

Available actions

- Create
- Renew
- Extend
- Cancel
- Suspend
- Reactivate

Subscription Status

- Active
- Pending
- Expired
- Cancelled
- Suspended

---

# 11. Managing Payments

Navigate

```
Payments
```

Functions

- Verify Payment
- View Transactions
- Export Reports
- Download Receipts
- Confirm Webhook
- Search Payments

Payment Status

- Successful
- Pending
- Failed
- Refunded

---

# 12. Monitoring Telemetry

Navigate

```
Telemetry
```

Live Information

- Battery Voltage
- Battery Current
- Solar Voltage
- Solar Current
- Load Power
- Temperature
- Wi-Fi Strength
- Relay State

Update Frequency

30–60 seconds

---

# 13. Managing Notifications

Notification Types

- Payment Success
- Subscription Expired
- Device Offline
- Low Battery
- Over Temperature
- Firmware Update Available
- Customer Registration

Actions

- View
- Mark Read
- Delete
- Filter
- Export

---

# 14. Reports and Analytics

Available Reports

Customer Reports

Device Reports

Revenue Reports

Subscription Reports

Telemetry Reports

Branch Reports

Monthly Reports

Annual Reports

Export Formats

- PDF
- Excel
- CSV

---

# 15. Remote Device Control

Administrators may remotely control supported devices.

Commands

Relay ON

Relay OFF

Restart Device

Sync Time

Update Configuration

Firmware Upgrade

Workflow

```
Dashboard

↓

Backend

↓

MQTT

↓

ESP32

↓

Relay

↓

Acknowledgement
```

Always verify acknowledgement before assuming a command was executed successfully.

---

# 16. System Settings

Only Super Administrators can modify:

- MQTT Configuration
- API Keys
- JWT Settings
- Environment Variables
- Branch Information
- User Roles
- Email Settings
- Payment Gateway Settings

---

# 17. Security Best Practices

Administrators should:

- Use strong passwords
- Enable Multi-Factor Authentication (when available)
- Never share accounts
- Log out after use
- Review login history
- Rotate passwords periodically
- Limit access based on roles

---

# 18. Daily Operations

Recommended daily tasks:

- Review dashboard
- Check offline devices
- Verify new payments
- Review alerts
- Respond to support requests
- Confirm scheduled jobs completed
- Check system logs

---

# 19. Weekly Maintenance

- Review telemetry trends
- Update customer records
- Inspect failed payments
- Check database backups
- Test notification delivery
- Review device health

---

# 20. Monthly Maintenance

- Generate management reports
- Archive old logs
- Update firmware (if required)
- Review user accounts
- Audit permissions
- Review system performance

---

# 21. Backup Procedures

Recommended backup schedule

Database

Daily

Configuration Files

Weekly

Firmware

Monthly

Documentation

Monthly

Store backups in secure off-site storage or cloud storage.

---

# 22. Incident Response

If a critical issue occurs:

1. Identify affected systems.
2. Review application and MQTT logs.
3. Determine the root cause.
4. Restore services if possible.
5. Notify affected users if required.
6. Document the incident.
7. Implement preventive measures.

---

# 23. Troubleshooting

Problem

Device Offline

Possible Causes

- No power
- Wi-Fi disconnected
- MQTT unavailable

Actions

- Check device power
- Verify internet connection
- Restart the device
- Review logs

---

Problem

Payment Not Verified

Actions

- Verify Paystack webhook
- Confirm transaction reference
- Check backend logs

---

Problem

Telemetry Missing

Actions

- Confirm ESP32 is connected
- Verify MQTT broker
- Check sensor status

---

# 24. Administrator Checklist

Daily

- Dashboard reviewed
- Alerts resolved
- Payments verified
- Offline devices investigated
- Customer requests handled

Weekly

- Reports generated
- Backups verified
- Device health reviewed
- Logs inspected

Monthly

- Firmware reviewed
- Permissions audited
- Documentation updated
- Security review completed

---

# Conclusion

The XSOLA Administrator Guide provides the operational procedures required to manage the platform effectively. By following these practices, administrators can ensure reliable system performance, accurate customer management, secure operations, and timely response to hardware and software events across the XSOLA ecosystem.
