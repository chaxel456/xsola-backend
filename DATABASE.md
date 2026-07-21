# XSOLA Database Documentation

## Introduction

The XSOLA backend uses **PostgreSQL** as its primary relational database. The database is hosted on **Supabase** and stores all application data including users, customers, waitlist registrations, devices, subscriptions, payments, notifications, reports, and telemetry.

The database follows a normalized relational design to ensure data integrity, scalability, and efficient querying.

---

# Database Information

| Property | Value |
|-----------|-------|
| Database | PostgreSQL |
| Provider | Supabase |
| ORM | SQLAlchemy |
| Migration Tool | Alembic |
| Primary Keys | UUID / Integer (depending on model) |
| Foreign Keys | Supported |
| Indexes | Yes |
| Transactions | ACID Compliant |

---

# Entity Relationship Diagram (ER Diagram)

```text
                     +----------------+
                     |     Users      |
                     +-------+--------+
                             |
                             |
               +-------------+-------------+
               |                           |
               ▼                           ▼
        +-------------+             +--------------+
        | Customers   |             | Waitlist     |
        +------+------+             +--------------+
               |
               |
        +------+------+ 
        | Devices      |
        +------+------+ 
               |
      +--------+---------+
      |                  |
      ▼                  ▼
Subscriptions      Telemetry
      |
      ▼
 Payments
      |
      ▼
Notifications

                Reports
```

---

# Tables Overview

| Table | Description |
|---------|-------------|
| users | Administrator accounts |
| waitlist | Prospective customer registrations |
| customers | Approved customers |
| devices | Installed IoT devices |
| subscriptions | Customer energy plans |
| payments | Payment records |
| telemetry | Device monitoring data |
| notifications | System notifications |
| reports | Dashboard statistics (generated) |

---

# Users Table

Stores administrator accounts.

| Column | Type | Description |
|--------|------|-------------|
| id | UUID | Primary Key |
| name | VARCHAR | Full Name |
| email | VARCHAR | Unique Email |
| password | VARCHAR | Hashed Password |
| created_at | TIMESTAMP | Account creation |

Indexes

- Primary Key(id)
- Unique(email)

---

# Waitlist Table

Stores people interested in XSOLA.

| Column | Type |
|--------|------|
| id | UUID |
| full_name | TEXT |
| email | VARCHAR |
| phone | VARCHAR |
| created_at | TIMESTAMP |

Indexes

- Primary Key(id)
- Index(email)

---

# Customers Table

Stores approved customers.

| Column | Type |
|--------|------|
| id | UUID |
| full_name | TEXT |
| email | VARCHAR |
| phone | VARCHAR |
| address | TEXT |
| status | VARCHAR |
| created_at | TIMESTAMP |

Indexes

- Primary Key(id)
- Index(email)

---

# Devices Table

Each installed ESP32 controller.

| Column | Type |
|--------|------|
| id | UUID |
| serial_number | VARCHAR |
| customer_id | UUID |
| relay_status | BOOLEAN |
| battery_level | INTEGER |
| status | VARCHAR |
| created_at | TIMESTAMP |

Relationship

```
Customer

1

↓

Many

Devices
```

Indexes

- Primary Key(id)
- Index(customer_id)
- Index(serial_number)

---

# Subscriptions Table

Stores energy plans.

| Column | Type |
|--------|------|
| id | UUID |
| customer_id | UUID |
| plan | VARCHAR |
| amount | DECIMAL |
| start_date | DATE |
| end_date | DATE |
| status | VARCHAR |

Relationship

```
Customer

1

↓

Many

Subscriptions
```

Indexes

- customer_id
- status

---

# Payments Table

Stores payment history.

| Column | Type |
|--------|------|
| id | UUID |
| customer_id | UUID |
| subscription_id | UUID |
| amount | DECIMAL |
| reference | VARCHAR |
| status | VARCHAR |
| payment_date | TIMESTAMP |

Relationship

```
Customer

↓

Payments

↓

Subscription
```

Indexes

- customer_id
- reference
- status

---

# Notifications Table

Stores dashboard notifications.

| Column | Type |
|--------|------|
| id | UUID |
| customer_id | UUID |
| title | VARCHAR |
| message | TEXT |
| read | BOOLEAN |
| created_at | TIMESTAMP |

Indexes

- customer_id
- read

---

# Telemetry Table

Stores live device information.

| Column | Type |
|--------|------|
| id | UUID |
| device_id | UUID |
| battery | INTEGER |
| solar_voltage | FLOAT |
| load_voltage | FLOAT |
| relay | BOOLEAN |
| created_at | TIMESTAMP |

Relationship

```
Device

1

↓

Many

Telemetry
```

Indexes

- device_id
- created_at

---

# Reports

Reports are generated dynamically from other tables.

Examples

- Total Customers
- Total Devices
- Active Subscriptions
- Revenue
- Waitlist Count

---

# Database Relationships

```text
Users
    │
    │
Customers ───── Devices ───── Telemetry
      │
      │
Subscriptions
      │
      │
Payments
      │
      │
Notifications

Waitlist (Independent)
```

---

# Index Strategy

Indexes are created on frequently queried fields.

Examples

- email
- customer_id
- device_id
- reference
- serial_number
- created_at
- status

These indexes improve query performance and dashboard responsiveness.

---

# Backup Strategy

- Daily PostgreSQL backups
- Supabase automatic backups
- Point-in-time recovery (where supported)
- Off-site backups for production

---

# Database Security

- Password-protected access
- SSL encrypted connections
- ORM-based query execution
- SQL injection protection
- Role-based database permissions

---

# Conclusion

The XSOLA database is designed to provide reliable, scalable, and secure storage for all application data. Its relational structure supports customer management, subscription billing, IoT telemetry, and reporting while maintaining high performance and data integrity.
