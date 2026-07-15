# app/utils/constants.py

# User Roles
ROLE_SUPER_ADMIN = "super_admin"
ROLE_ADMIN = "admin"
ROLE_MANAGER = "manager"
ROLE_TECHNICIAN = "technician"
ROLE_CUSTOMER = "customer"

# Device Status
DEVICE_ACTIVE = "active"
DEVICE_INACTIVE = "inactive"
DEVICE_OFFLINE = "offline"
DEVICE_ONLINE = "online"
DEVICE_MAINTENANCE = "maintenance"

# Subscription Status
SUB_ACTIVE = "active"
SUB_EXPIRED = "expired"
SUB_CANCELLED = "cancelled"
SUB_PENDING = "pending"

# Payment Status
PAYMENT_PENDING = "pending"
PAYMENT_SUCCESS = "successful"
PAYMENT_FAILED = "failed"

# Notification Types
NOTIFICATION_SYSTEM = "system"
NOTIFICATION_EMAIL = "email"
NOTIFICATION_SMS = "sms"
NOTIFICATION_PUSH = "push"

# MQTT Topics
MQTT_DEVICE = "xsola/device"
MQTT_COMMAND = "command"
MQTT_TELEMETRY = "telemetry"
MQTT_STATUS = "status"

# File Uploads
CUSTOMER_UPLOAD = "uploads/customers"
DEVICE_UPLOAD = "uploads/devices"
REPORT_UPLOAD = "uploads/reports"