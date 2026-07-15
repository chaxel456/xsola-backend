# app/api/v1/router.py

from fastapi import APIRouter
from app.api.v1.auth import router as auth_router
from app.api.v1.users import router as users_router
from app.api.v1.waitlist import router as waitlist_router
from app.api.v1.customers import router as customers_router
from app.api.v1.devices import router as devices_router
from app.api.v1.subscriptions import router as subscriptions_router
from app.api.v1.payments import router as payments_router
from app.api.v1.telemetry import router as telemetry_router
from app.modules.notification.routes import router as notification_router
from app.modules.reports.routes import router as reports_router



api_router = APIRouter()

api_router.include_router(auth_router)


api_router = APIRouter(prefix="/api/v1")


api_router.include_router(auth_router, prefix="/auth", tags=["Auth"])
api_router.include_router(users_router, prefix="/users", tags=["Users"])
api_router.include_router(customers_router, prefix="/customers", tags=["Customers"])
api_router.include_router(devices_router, prefix="/devices", tags=["Devices"])
api_router.include_router(payments_router, prefix="/payments", tags=["Payments"])
api_router.include_router(reports_router, prefix="/reports", tags=["Reports"])
api_router.include_router(subscriptions_router, prefix="/subscriptions", tags=["Subscriptions"])
api_router.include_router(notification_router, prefix="/notifications", tags=["Notifications"])
api_router.include_router(waitlist_router, prefix="/waitlist", tags=["Waitlist"])
api_router.include_router(customers_router, prefix="/customers", tags=["Customers"])
api_router.include_router(telemetry_router, prefix="/telemetry", tags=["Telemetry"])
api_router.include_router(reports_router, prefix="/reports", tags=["reports"])


