# XSOLA Payment System Documentation

## Introduction

The XSOLA payment system is responsible for handling all financial transactions within the platform. It enables customers to subscribe to solar energy plans, securely process payments through Paystack, verify transactions, activate subscriptions, and automatically control customer devices after successful payment.

The payment module is designed to be secure, scalable, and extensible, allowing additional payment gateways to be integrated in the future.

---

# Objectives

The payment system is responsible for:

- Accept customer payments
- Initialize payment sessions
- Verify completed transactions
- Store payment history
- Activate subscriptions
- Trigger device activation
- Generate payment reports
- Handle failed transactions
- Receive webhook notifications
- Prevent duplicate payments

---

# Payment Architecture

```text
                Customer

                    │

                    ▼

            XSOLA Frontend

                    │

                    ▼

            FastAPI Backend

                    │

        Initialize Payment

                    │

                    ▼

               Paystack

                    │

      Customer Pays Online

                    │

                    ▼

         Paystack Verification

                    │

                    ▼

            FastAPI Backend

                    │

      Update Database

                    │

                    ▼

      Activate Subscription

                    │

                    ▼

           Publish MQTT Command

                    │

                    ▼

                ESP32

                    │

                    ▼

               Relay ON

                    │

                    ▼

        Customer Gets Electricity
```

---

# Payment Workflow

The complete payment lifecycle is shown below.

```text
Customer

↓

Choose Subscription

↓

Click Pay

↓

Backend

↓

Initialize Payment

↓

Paystack Checkout

↓

Customer Pays

↓

Paystack Verifies

↓

Backend Confirms Payment

↓

Save Payment Record

↓

Activate Subscription

↓

MQTT Publish

↓

ESP32

↓

Relay ON

↓

Electricity Available
```

---

# Payment Methods

Currently Supported

- Debit Card
- Credit Card
- Bank Transfer
- USSD
- Bank Account
- Mobile Money (where supported by Paystack)

Future Support

- Flutterwave
- Moniepoint
- Stripe
- PayPal
- Crypto Payments

---

# Subscription Plans

Example plans

| Plan | Duration |
|-------|----------|
| Daily | 24 Hours |
| Weekly | 7 Days |
| Monthly | 30 Days |
| Quarterly | 90 Days |
| Yearly | 365 Days |

Each subscription creates a payment record.

---

# Initialize Payment

Before a customer pays, the backend requests an authorization URL from Paystack.

Endpoint

```http
POST /api/v1/payments/payments/initialize
```

Example Request

```json
{
    "customer_id": 10,
    "amount": 50000
}
```

Example Response

```json
{
    "authorization_url":"https://checkout.paystack.com/xxxxx",
    "reference":"PSK_839283923"
}
```

The frontend redirects the customer to the Paystack checkout page.

---

# Customer Checkout

```text
Frontend

↓

Paystack Checkout

↓

Card Details

↓

OTP

↓

Payment Processing

↓

Success
```

Paystack securely handles sensitive payment information. Card details never pass through the XSOLA backend.

---

# Payment Verification

After payment, the backend verifies the transaction before activating the subscription.

Endpoint

```http
GET /api/v1/payments/payments/verify/{reference}
```

Example

```http
GET /verify/PSK_839283923
```

Example Response

```json
{
    "status":"success",
    "amount":50000,
    "reference":"PSK_839283923"
}
```

---

# Verification Process

```text
Backend

↓

Receive Reference

↓

Call Paystack API

↓

Check Status

↓

Successful?

↓

YES

↓

Update Database

↓

Activate Subscription

↓

Publish MQTT Command
```

---

# Payment Webhook

Paystack notifies the backend automatically when a payment event occurs.

Endpoint

```http
POST /api/v1/payments/payments/webhook
```

Events include:

- charge.success
- transfer.success
- refund.processed
- invoice.paid

Example Payload

```json
{
    "event":"charge.success",
    "data":{
        "reference":"PSK_839283923",
        "amount":50000
    }
}
```

The backend validates the webhook signature before processing the event.

---

# Subscription Activation

Once payment is confirmed:

```text
Payment Verified

↓

Subscription Status

↓

Active

↓

Database Updated

↓

MQTT Publish

↓

ESP32

↓

Relay ON
```

The customer immediately gains access to electricity.

---

# Automatic Device Activation

Example MQTT Topic

```text
xsola/device/device001/control
```

Payload

```json
{
    "action":"ON"
}
```

---

# Subscription Expiry

When a subscription expires:

```text
Scheduler

↓

Expired Subscription

↓

MQTT Publish

↓

ESP32

↓

Relay OFF

↓

Electricity Disabled
```

---

# Payment Database Flow

```text
Payment

↓

payments Table

↓

Reference

↓

Status

↓

Customer

↓

Subscription
```

---

# Payment Status

Possible statuses:

| Status | Meaning |
|----------|---------|
| Pending | Awaiting payment |
| Successful | Payment completed |
| Failed | Payment unsuccessful |
| Cancelled | User cancelled |
| Refunded | Payment refunded |

---

# Database Tables

Payments

```text
payments
```

Subscriptions

```text
subscriptions
```

Customers

```text
customers
```

---

# Duplicate Payment Protection

The backend checks:

- Payment reference uniqueness
- Existing successful transactions
- Subscription status
- Customer identity

This prevents duplicate billing.

---

# Error Handling

Possible errors include:

- Invalid payment reference
- Payment failed
- Network timeout
- Duplicate transaction
- Invalid webhook signature
- Subscription not found

Example Response

```json
{
    "success":false,
    "message":"Payment verification failed."
}
```

---

# Security

The payment system follows industry best practices.

Measures include:

- HTTPS
- Paystack Signature Verification
- Secret Keys stored in Environment Variables
- JWT Authentication
- SQLAlchemy ORM
- Input Validation
- Audit Logging

Sensitive information such as card numbers and CVVs are never stored by XSOLA.

---

# Environment Variables

Required variables include:

```env
PAYSTACK_SECRET_KEY=
PAYSTACK_PUBLIC_KEY=
PAYSTACK_CALLBACK_URL=
```

---

# API Endpoints

| Endpoint | Description |
|------------|-------------|
| POST /payments/initialize | Initialize payment |
| GET /payments/verify/{reference} | Verify payment |
| POST /payments/webhook | Receive Paystack webhook |
| GET /payments | List payments |
| POST /payments | Create payment |
| DELETE /payments/{id} | Delete payment |

---

# Reports

The payment module provides statistics such as:

- Total Revenue
- Monthly Revenue
- Daily Revenue
- Successful Payments
- Failed Payments
- Active Subscriptions
- Expired Subscriptions

These values are displayed on the administrator dashboard.

---

# Future Improvements

Future versions of the payment system will include:

- Multiple payment gateways
- Automatic recurring billing
- Wallet system
- Coupon and discount support
- Invoice generation
- Tax calculation
- Refund processing
- Partial payments
- Offline payment reconciliation
- Multi-currency support

---

# Complete Payment Flow

```text
Customer

↓

Frontend

↓

FastAPI

↓

Paystack Initialize

↓

Checkout

↓

Payment

↓

Paystack Verify

↓

Backend

↓

Save Payment

↓

Activate Subscription

↓

MQTT Publish

↓

ESP32

↓

Relay ON

↓

Customer Receives Electricity
```

---

# Conclusion

The XSOLA payment system provides a secure and automated mechanism for managing subscription-based solar energy services. By integrating with Paystack, verifying transactions, activating subscriptions, and communicating with IoT devices through MQTT, the platform ensures that electricity delivery is directly tied to successful payments while maintaining security, reliability, and scalability.
