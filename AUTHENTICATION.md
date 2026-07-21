# XSOLA Authentication & Authorization

## Introduction

The XSOLA platform uses **JWT (JSON Web Tokens)** for secure authentication and authorization.

Only authenticated administrators can access protected endpoints such as customer management, device control, reports, and payments.

---

# Authentication Flow

```text
Administrator

↓

Login Page

↓

Email + Password

↓

FastAPI

↓

Password Verification

↓

JWT Generated

↓

Access Token Returned

↓

Browser Stores Token

↓

Authenticated Requests
```

---

# Registration

Endpoint

```http
POST /api/v1/auth/auth/register
```

Example Request

```json
{
    "name":"Admin User",
    "email":"admin@xsola.com",
    "password":"StrongPassword123"
}
```

Example Response

```json
{
    "id":1,
    "email":"admin@xsola.com",
    "access_token":"eyJhbGc...",
    "token_type":"bearer"
}
```

---

# Login

Endpoint

```http
POST /api/v1/auth/auth/login
```

Example Request

```json
{
    "email":"admin@xsola.com",
    "password":"StrongPassword123"
}
```

Example Response

```json
{
    "access_token":"eyJhbGc...",
    "token_type":"bearer"
}
```

---

# JWT (JSON Web Token)

JWT is a secure token that proves the identity of an authenticated user.

A token contains three parts:

```text
HEADER

.

PAYLOAD

.

SIGNATURE
```

Example

```text
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

The token is digitally signed using the backend secret key, preventing unauthorized modification.

---

# Bearer Token

After login, the frontend stores the access token (typically in localStorage or a secure storage mechanism).

Every request to a protected endpoint must include the token in the HTTP Authorization header.

Example:

```http
Authorization: Bearer eyJhbGcOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

If the token is missing, invalid, or expired, the backend returns **401 Unauthorized**.

---

# Password Hashing

Passwords are **never stored as plain text**.

Before saving a password, the backend hashes it using **bcrypt**.

```text
User Password

↓

bcrypt Hash

↓

Database
```

Example Hash

```text
$2b$12$YQvTjPj7rP4...
```

During login:

```text
Entered Password

↓

bcrypt Verify

↓

Stored Hash

↓

Match?

↓

Login Successful
```

---

# Authorization

Authentication verifies **who the user is**.

Authorization determines **what the user is allowed to access**.

Only authenticated users with a valid JWT can access protected endpoints.

Protected examples:

- Customer Management
- Device Management
- Payments
- Reports
- Notifications
- Telemetry

---

# Current User Endpoint

```http
GET /api/v1/auth/auth/me
```

Headers

```http
Authorization: Bearer <JWT_TOKEN>
```

Example Response

```json
{
    "id":1,
    "name":"Admin User",
    "email":"admin@xsola.com"
}
```

---

# Authentication Workflow

```text
User

↓

Login

↓

Backend

↓

Validate Credentials

↓

Generate JWT

↓

Return Token

↓

Store Token

↓

Access Protected APIs
```

---

# Token Validation

For every protected request:

```text
Frontend

↓

Authorization Header

↓

Backend

↓

Verify Signature

↓

Verify Expiration

↓

Load User

↓

Grant Access
```

---

# Security Best Practices

- Passwords hashed with bcrypt
- JWT signed using a secret key
- HTTPS for all production traffic
- Strong password requirements
- Input validation with Pydantic
- Protected API routes
- Environment variables for secrets
- CORS configuration
- SQL injection protection through SQLAlchemy

---

# Authentication Errors

| HTTP Code | Description |
|-----------|-------------|
| 200 | Success |
| 201 | Resource Created |
| 400 | Bad Request |
| 401 | Invalid Credentials / Token |
| 403 | Forbidden |
| 422 | Validation Error |

---

# Conclusion

The XSOLA authentication system is built on industry-standard practices using FastAPI, JWT, bcrypt, and secure authorization headers. This approach provides a scalable and secure mechanism for protecting administrative resources and ensuring that only authorized users can access sensitive operations such as customer management, device control, payments, and reporting.
