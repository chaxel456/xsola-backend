# XSOLA Environment Variables Documentation

## Introduction

Environment variables store configuration values that the XSOLA backend needs to run. They keep sensitive information such as database credentials, API keys, and secret tokens out of the source code.

Using environment variables improves:

- Security
- Portability
- Deployment flexibility
- Configuration management
- Scalability

Never commit `.env` files to GitHub.

---

# Environment Architecture

```text
Developer

↓

.env File

↓

FastAPI Settings

↓

Application

↓

Database
MQTT
Paystack
Supabase
JWT
```

---

# Environment File

Create a file named:

```text
.env
```

Example:

```env
# =====================================
# APPLICATION
# =====================================

APP_NAME=XSOLA
APP_ENV=development
APP_VERSION=1.0.0
DEBUG=True

# =====================================
# SERVER
# =====================================

HOST=0.0.0.0
PORT=8000

# =====================================
# SECURITY
# =====================================

SECRET_KEY=your_super_secret_key_here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60

# =====================================
# DATABASE
# =====================================

DATABASE_URL=postgresql://username:password@host:5432/xsola

# =====================================
# SUPABASE
# =====================================

SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your_supabase_anon_key

# =====================================
# MQTT
# =====================================

MQTT_BROKER=broker.hivemq.com
MQTT_PORT=1883
MQTT_USERNAME=
MQTT_PASSWORD=
MQTT_CLIENT_ID=xsola_backend

# =====================================
# PAYSTACK
# =====================================

PAYSTACK_PUBLIC_KEY=pk_test_xxxxxxxxxxxxxxxxx
PAYSTACK_SECRET_KEY=sk_test_xxxxxxxxxxxxxxxxx
PAYSTACK_WEBHOOK_SECRET=xxxxxxxxxxxxxxxx

# =====================================
# EMAIL (Future)
# =====================================

SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=
SMTP_PASSWORD=

# =====================================
# REDIS (Future)
# =====================================

REDIS_URL=redis://localhost:6379

# =====================================
# LOGGING
# =====================================

LOG_LEVEL=INFO

# =====================================
# CORS
# =====================================

ALLOWED_ORIGINS=http://localhost:5500,https://xsola.com
```

---

# Variable Reference

## APP_NAME

Purpose

Application name.

Example

```env
APP_NAME=XSOLA
```

---

## APP_ENV

Determines the running environment.

Values

```text
development

testing

staging

production
```

---

## APP_VERSION

Application version.

Example

```env
APP_VERSION=1.0.0
```

---

## DEBUG

Enables debugging.

Development

```env
DEBUG=True
```

Production

```env
DEBUG=False
```

---

# HOST

Server IP address.

Example

```env
HOST=0.0.0.0
```

---

# PORT

Application port.

Development

```env
PORT=8000
```

Production

Render automatically provides:

```text
PORT
```

---

# SECRET_KEY

Used for signing JWT tokens.

Example

```env
SECRET_KEY=VeryLongRandomSecretKey
```

Never expose this value.

---

# ALGORITHM

JWT encryption algorithm.

Example

```env
ALGORITHM=HS256
```

---

# ACCESS_TOKEN_EXPIRE_MINUTES

JWT expiration.

Example

```env
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

---

# DATABASE_URL

Complete PostgreSQL connection string.

Example

```env
DATABASE_URL=postgresql://postgres:password@db.supabase.co:5432/postgres
```

Used by SQLAlchemy.

---

# SUPABASE_URL

Supabase project URL.

Example

```env
SUPABASE_URL=https://abcdefgh.supabase.co
```

---

# SUPABASE_KEY

API key for Supabase services.

Never expose this key publicly.

---

# MQTT_BROKER

Broker hostname.

Example

```env
MQTT_BROKER=broker.hivemq.com
```

Production may use:

- EMQX
- Mosquitto
- HiveMQ Cloud

---

# MQTT_PORT

Default values:

```text
1883
```

Without TLS

or

```text
8883
```

With TLS

---

# MQTT_USERNAME

Broker username.

Optional for public brokers.

Required for production.

---

# MQTT_PASSWORD

Broker password.

Keep secret.

---

# MQTT_CLIENT_ID

Unique backend client ID.

Example

```env
MQTT_CLIENT_ID=xsola_backend
```

---

# PAYSTACK_PUBLIC_KEY

Used by frontend.

Example

```env
PAYSTACK_PUBLIC_KEY=pk_live_xxxxxxxxx
```

---

# PAYSTACK_SECRET_KEY

Used only by backend.

Never expose it.

Example

```env
PAYSTACK_SECRET_KEY=sk_live_xxxxxxxxx
```

---

# PAYSTACK_WEBHOOK_SECRET

Validates incoming webhook requests.

Protects against fake payment notifications.

---

# SMTP Variables

Future email support.

```env
SMTP_SERVER=smtp.gmail.com

SMTP_PORT=587

SMTP_USERNAME=...

SMTP_PASSWORD=...
```

---

# REDIS_URL

Future caching and background jobs.

Example

```env
REDIS_URL=redis://localhost:6379
```

---

# LOG_LEVEL

Controls application logging.

Available values:

```text
DEBUG

INFO

WARNING

ERROR

CRITICAL
```

---

# ALLOWED_ORIGINS

Defines which frontends may access the API.

Example

```env
ALLOWED_ORIGINS=http://localhost:5500,https://xsola.com
```

---

# Loading Environment Variables

Using Pydantic Settings:

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str

    class Config:
        env_file = ".env"

settings = Settings()
```

---

# Render Configuration

Environment variables are configured in the Render dashboard.

```text
Render Dashboard

↓

Environment

↓

Add Variable

↓

Deploy
```

---

# Local Development

Install dependencies.

Create `.env`.

Run:

```bash
uvicorn app.main:app --reload
```

---

# Security Best Practices

- Never commit `.env`
- Rotate secrets periodically
- Use strong random keys
- Separate development and production values
- Restrict access to deployment dashboards
- Store secrets in Render Environment Variables

---

# .gitignore

Always ignore environment files.

```gitignore
.env
.env.local
.env.production
```

---

# Future Environment Variables

Future releases may include:

```env
SENTRY_DSN=

AWS_ACCESS_KEY=

AWS_SECRET_KEY=

MINIO_ENDPOINT=

OPENAI_API_KEY=

TWILIO_API_KEY=

FCM_SERVER_KEY=

CELERY_BROKER_URL=
```

---

# Deployment Checklist

Before deployment verify:

- SECRET_KEY configured
- DATABASE_URL configured
- MQTT credentials configured
- Paystack keys configured
- CORS origins configured
- Debug disabled
- Log level appropriate
- Environment variables stored securely

---

# Conclusion

Environment variables provide a secure and flexible configuration system for XSOLA. By separating sensitive values from source code, the platform can be deployed safely across development, testing, staging, and production environments while protecting secrets and simplifying configuration management.
