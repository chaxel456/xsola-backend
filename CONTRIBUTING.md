# Contributing to XSOLA

## Welcome

Thank you for your interest in contributing to the XSOLA project.

XSOLA is an open, modular, and scalable Smart Solar Energy Management Platform. Contributions from developers, designers, testers, technical writers, IoT engineers, and security researchers are welcome.

This document explains the standards and workflow for contributing to the project.

---

# Table of Contents

- Code of Conduct
- Ways to Contribute
- Development Workflow
- Repository Structure
- Branch Naming
- Commit Messages
- Pull Requests
- Code Review
- Coding Standards
- Testing Requirements
- Documentation
- Reporting Bugs
- Requesting Features
- Security Issues
- Release Process

---

# Code of Conduct

All contributors are expected to:

- Be respectful
- Communicate professionally
- Welcome constructive feedback
- Focus on solving problems
- Respect different experience levels
- Avoid offensive language
- Keep discussions productive

---

# Ways to Contribute

You can contribute by:

- Writing backend code
- Building frontend features
- Improving UI/UX
- Writing documentation
- Fixing bugs
- Improving security
- Writing tests
- Reviewing pull requests
- Developing ESP32 firmware
- Improving MQTT integration
- Optimizing database queries

---

# Repository Structure

```
xsola/

├── app/
├── docs/
├── tests/
├── scripts/
├── docker/
├── firmware/
├── frontend/
├── .github/
├── README.md
└── requirements.txt
```

---

# Development Workflow

Every new feature follows this process.

```
Issue

↓

Create Branch

↓

Develop Feature

↓

Run Tests

↓

Commit

↓

Push

↓

Pull Request

↓

Code Review

↓

Merge
```

---

# Branch Naming Convention

Use descriptive branch names.

### Features

```
feature/customer-management
```

```
feature/payment-module
```

```
feature/dashboard
```

---

### Bug Fixes

```
fix/login-error
```

```
fix/payment-verification
```

---

### Documentation

```
docs/api-update
```

```
docs/database
```

---

### Refactoring

```
refactor/auth-service
```

---

### Hotfixes

```
hotfix/security-patch
```

---

# Commit Message Convention

Write clear and concise commit messages.

Examples:

```
Add customer CRUD endpoints
```

```
Fix JWT authentication bug
```

```
Update API documentation
```

```
Improve payment verification
```

```
Add MQTT device monitoring
```

---

# Recommended Commit Format

```
<type>: <short description>
```

Examples

```
feat: add customer search

fix: resolve login issue

docs: update README

refactor: improve auth service

test: add authentication tests

style: improve dashboard layout

perf: optimize database query

chore: update dependencies
```

---

# Pull Request Process

Every Pull Request should include:

- Clear title
- Description of changes
- Related issue number
- Testing evidence
- Screenshots (if UI changes)
- Updated documentation (if required)

Example

```
Title:

Add customer search functionality

Description:

Implemented search endpoint
Added frontend search
Updated documentation
Added tests
```

---

# Code Review Checklist

Reviewers should verify:

- Code follows project standards
- No unnecessary complexity
- Security considerations
- Performance impact
- Proper documentation
- Tests included
- No sensitive data committed
- API consistency

---

# Coding Standards

General principles:

- Keep functions small
- Use meaningful names
- Avoid duplicate code
- Write readable code
- Add comments where necessary
- Handle exceptions properly
- Validate user input
- Follow PEP 8 for Python

Example

Good

```python
def get_customer(customer_id: int):
    return repository.get(customer_id)
```

Avoid

```python
def g(x):
    ...
```

---

# Python Style Guide

Use:

- Black (formatter)
- isort (import sorting)
- Ruff or Flake8 (linting)

Example

```
black app/

isort app/

ruff check app/
```

---

# Frontend Standards

Use:

- Semantic HTML
- Responsive CSS
- Modular JavaScript
- Consistent naming
- Accessible components

Avoid:

- Inline styles
- Global variables
- Duplicate CSS

---

# API Development Standards

Every endpoint should:

- Validate requests
- Return appropriate status codes
- Handle exceptions
- Include documentation
- Require authentication where necessary

Example

```
GET /customers
```

Response

```json
[
  {
    "id":1,
    "name":"John Doe"
  }
]
```

---

# Database Standards

- Use migrations
- Never modify production tables manually
- Add indexes where needed
- Maintain relationships
- Use transactions for critical operations

---

# Documentation Requirements

Every feature should update documentation if it changes:

- API
- Database
- Configuration
- Installation
- User Guide

---

# Testing Requirements

Every new feature should include tests.

Required tests:

- Unit Tests
- Integration Tests
- API Tests
- Authentication Tests

Example

```
tests/

test_auth.py

test_customers.py

test_devices.py
```

---

# Reporting Bugs

Create an issue containing:

- Bug description
- Expected behavior
- Actual behavior
- Steps to reproduce
- Screenshots
- Environment
- Logs

Example

```
Bug:

Login fails after password reset.

Steps:

1. Reset password
2. Login
3. Receive 500 error
```

---

# Feature Requests

Include:

- Problem statement
- Proposed solution
- Benefits
- Alternatives considered

---

# Security Issues

Do **not** create a public issue for security vulnerabilities.

Instead:

- Contact the project maintainers privately.
- Provide reproduction steps.
- Include impact assessment.
- Allow time for a fix before public disclosure.

---

# Continuous Integration (Future)

Every Pull Request should automatically run:

- Linting
- Unit tests
- Integration tests
- Security scans
- Build validation

Example workflow

```
Push

↓

GitHub Actions

↓

Run Tests

↓

Build

↓

Deploy Preview

↓

Merge
```

---

# Release Workflow

```
Development

↓

Testing

↓

Review

↓

Merge

↓

Version Tag

↓

Release Notes

↓

Production Deployment
```

---

# Recognition

Contributors may be recognized in:

- Release Notes
- Contributors List
- Project Website
- Documentation

---

# Getting Help

If you need assistance:

- Read the documentation
- Search existing issues
- Open a discussion
- Contact project maintainers

---

# Thank You

Every contribution—whether it's code, documentation, design, testing, or ideas—helps improve XSOLA and supports the mission of building a reliable, intelligent solar energy management platform.
