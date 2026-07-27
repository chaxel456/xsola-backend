# XSOLA Coding Standards

Version: 1.0.0

Project: XSOLA Smart Solar Energy Management Platform

Audience:
- Backend Developers
- Frontend Developers
- IoT Developers
- DevOps Engineers

---

# Table of Contents

1. Introduction
2. General Principles
3. Project Structure
4. Python Coding Standards
5. FastAPI Standards
6. SQLAlchemy Standards
7. Pydantic Standards
8. Frontend Standards
9. ESP32/Firmware Standards
10. API Design Standards
11. Database Standards
12. Git Standards
13. Documentation Standards
14. Testing Standards
15. Logging Standards
16. Security Standards
17. Code Review Checklist
18. Best Practices

---

# 1. Introduction

This document defines the coding standards used throughout the XSOLA project.

Goals:

- Consistency
- Readability
- Maintainability
- Scalability
- Security
- Collaboration

Every contributor should follow these standards before submitting code.

---

# 2. General Principles

Every piece of code should be:

- Simple
- Readable
- Reusable
- Secure
- Well documented
- Easy to test

Avoid:

- Duplicate code
- Hardcoded values
- Unused variables
- Large functions
- Magic numbers
- Unnecessary comments

---

# 3. Project Structure

Backend

```

app/
api/
core/
models/
schemas/
services/
utils/
middleware/
dependencies/
tests/

```

Frontend

```

frontend/
css/
js/
images/
pages/

```

Firmware

```

firmware/
src/
include/
lib/

```

---

# 4. Python Coding Standards

Follow **PEP 8**.

Indentation

```

4 spaces

```

Maximum Line Length

```

88–100 characters

```

Use meaningful variable names.

Good

```python
customer_name
subscription_status
battery_voltage
```

Bad

```python
x
a
temp
```

---

## Naming Conventions

Classes

```python
CustomerService
PaymentManager
DeviceController
```

Functions

```python
create_customer()

verify_payment()

publish_command()
```

Variables

```python
device_id

customer_email

battery_level
```

Constants

```python
MQTT_PORT

JWT_SECRET

MAX_RETRY_COUNT
```

---

# 5. FastAPI Standards

Every route should include:

- Type hints
- Response model
- Status code
- Docstring
- Authentication (where required)

Example

```python
@router.get(
    "/customers",
    response_model=list[CustomerResponse]
)
async def get_customers():
    """Return all customers."""
```

---

# 6. SQLAlchemy Standards

One model per file.

Always define:

- Primary Key
- Relationships
- Indexes (where appropriate)
- Constraints

Example

```python
class Customer(Base):
    __tablename__ = "customers"

    id = Column(UUID, primary_key=True)
    email = Column(String, unique=True)
```

Use relationships instead of writing unnecessary joins manually.

---

# 7. Pydantic Standards

Separate request and response schemas.

Example

```python
CustomerCreate
```

```python
CustomerUpdate
```

```python
CustomerResponse
```

Never expose internal database fields unless required.

---

# 8. Frontend Standards

Use:

- Semantic HTML
- Responsive CSS
- Modular JavaScript

File names

```
dashboard.js

login.js

customers.js
```

CSS

Use classes instead of inline styles.

Good

```css
.customer-card {}
```

Avoid

```html
<div style="color:red">
```

JavaScript

Use async/await.

Good

```javascript
const response = await fetch(API.customers);
```

Avoid nested callbacks where possible.

---

# 9. ESP32/Firmware Standards

Organize firmware into modules.

Example

```
wifi.cpp
mqtt.cpp
relay.cpp
telemetry.cpp
config.cpp
main.cpp
```

Never hardcode:

- Wi-Fi credentials
- MQTT credentials
- API keys

Store configuration securely or load from configuration storage where applicable.

---

# 10. API Design Standards

Use RESTful endpoints.

Good

```
GET /customers

POST /customers

PUT /customers/{id}

DELETE /customers/{id}
```

Return consistent JSON.

Example

```json
{
  "success": true,
  "message": "Customer created.",
  "data": {}
}
```

Use appropriate HTTP status codes.

| Status | Meaning |
|---------|---------|
| 200 | Success |
| 201 | Created |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 409 | Conflict |
| 422 | Validation Error |
| 500 | Internal Server Error |

---

# 11. Database Standards

Use:

- Foreign Keys
- Constraints
- Indexes
- Transactions

Table names

```
customers

payments

subscriptions
```

Avoid singular table names.

---

# 12. Git Standards

Branch naming

```
feature/customer-module

feature/payment-api

bugfix/login-error

hotfix/payment-webhook

docs/api-documentation
```

Commit messages

Good

```
Add customer CRUD endpoints

Fix MQTT reconnect logic

Update deployment documentation
```

Avoid

```
fix

update

changes

misc
```

---

# 13. Documentation Standards

Every module should include:

- Purpose
- Inputs
- Outputs
- Exceptions
- Examples (where useful)

Use Markdown for project documentation.

Keep documentation synchronized with code changes.

---

# 14. Testing Standards

Write tests for:

- API endpoints
- Services
- Utilities
- Authentication
- Payment verification
- Device communication

Target

```
Minimum 80% code coverage
```

Use

- pytest
- FastAPI TestClient

Example

```python
def test_create_customer():
    ...
```

---

# 15. Logging Standards

Log:

- Authentication events
- Payment processing
- MQTT messages
- Device registration
- Errors
- Warnings

Avoid logging:

- Passwords
- JWT tokens
- Secret keys
- Payment card details

Example

```python
logger.info("Customer created: %s", customer.id)
```

---

# 16. Security Standards

Always:

- Validate input
- Hash passwords
- Use HTTPS in production
- Store secrets in environment variables
- Verify JWT tokens
- Sanitize user input
- Apply least-privilege access

Never:

- Commit `.env` files
- Hardcode credentials
- Expose stack traces in production
- Trust client-side validation alone

---

# 17. Code Review Checklist

Before merging:

- Code builds successfully
- Tests pass
- Documentation updated
- No secrets committed
- No unused imports
- No debug statements
- Error handling implemented
- Logging added where appropriate
- Naming conventions followed
- Performance considered

---

# 18. Best Practices

- Keep functions focused on one responsibility.
- Use dependency injection where appropriate.
- Prefer configuration over hardcoded values.
- Handle exceptions gracefully.
- Write self-explanatory code.
- Optimize only after measuring performance.
- Refactor when complexity increases.
- Review pull requests carefully.
- Keep dependencies up to date.
- Continuously improve documentation.

---

# Recommended Development Workflow

```
Create Feature Branch

↓

Implement Feature

↓

Run Tests

↓

Run Linter

↓

Update Documentation

↓

Commit Changes

↓

Open Pull Request

↓

Code Review

↓

Merge into Main

↓

Deploy
```

---

# Tools Used in XSOLA

| Purpose | Tool |
|----------|------|
| Backend | FastAPI |
| ORM | SQLAlchemy |
| Validation | Pydantic |
| Database | PostgreSQL |
| Migrations | Alembic |
| MQTT | Eclipse Mosquitto / HiveMQ |
| Payments | Paystack |
| Testing | pytest |
| Version Control | Git |
| CI/CD | GitHub Actions (planned) |
| Deployment | Render |
| Containerization | Docker |

---

# Conclusion

Following these coding standards ensures that the XSOLA codebase remains clean, secure, maintainable, and scalable. Consistent practices reduce bugs, simplify onboarding for new developers, and support the long-term evolution of the platform.
