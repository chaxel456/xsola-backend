# app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text
from fastapi import Depends
from fastapi import WebSocket


from app.core.database import get_db
from app.core.dependencies import get_current_user
from app.core.database import engine
from app.core.config import settings
from app.core.exceptions import register_exception_handlers
from app.api.v1.router import api_router
from app.core.database import Base, engine
from app.modules.auth.model import User
from app.modules.customers.model import Customer
from app.modules.devices.model import Device
from app.modules.payments.model import Payment
from app.modules.notification.model import Notification
from app.services.mqtt_service import MQTTService
from app.websocket.telemetry_ws import (
    manager
)

from apscheduler.schedulers.background import (
    BackgroundScheduler
)

from app.tasks.subscriptions import (
    expire_subscriptions
)

from app.tasks.telemetry import (
    check_offline_devices
)

from app.tasks.notifications import (
    send_pending_notifications
)

from app.tasks.reports import (
    generate_daily_report
)


from app.middleware.logging import LoggingMiddleware
from app.middleware.rate_limit import RateLimitMiddleware



mqtt_service = MQTTService()
scheduler = BackgroundScheduler()


mqtt_service = MQTTService()
scheduler = BackgroundScheduler()

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    debug=settings.DEBUG,
)

app.add_middleware(
    LoggingMiddleware
)

app.add_middleware(
    RateLimitMiddleware
)

mqtt_service = MQTTService()

scheduler = BackgroundScheduler()


# Exception Handlers
register_exception_handlers(app)

# API Routers
app.include_router(api_router)

Base.metadata.create_all(bind=engine)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        settings.FRONTEND_URL,
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["Health"])
def health_check():
    return {
        "status": "success",
        "message": "XSOLA Backend Running",
        "version": settings.APP_VERSION,
    }


@app.get("/health", tags=["Health"])
def health():
    return {
        "status": "healthy"
    }


@app.get("/db-test")
def db_test():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT NOW()"))
        return {"db_time": str(result.scalar())}
    


@app.get("/me")
def me(
    current_user=Depends(get_current_user)
):
    return current_user
    

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)



@app.get("/users-test")
def users_test(db=Depends(get_db)):
    from app.modules.auth.model import User

    return db.query(User).all()

@app.on_event("startup")
async def startup_event():

    mqtt_service.connect()

    scheduler.start()

    print("Scheduler Started")

@app.on_event("shutdown")
async def shutdown_event():

    mqtt_service.disconnect()

    scheduler.shutdown()

    print("Scheduler Stopped")


@app.websocket("/ws/telemetry")
async def telemetry_websocket(
    websocket: WebSocket
):

    await manager.connect(
        websocket
    )

    try:

        while True:

            await websocket.receive_text()

    except Exception:

        manager.disconnect(
            websocket
        )


scheduler.add_job(
    expire_subscriptions,
    "interval",
    hours=1
)

scheduler.add_job(
    check_offline_devices,
    "interval",
    minutes=5
)

scheduler.add_job(
    send_pending_notifications,
    "interval",
    minutes=2
)

scheduler.add_job(
    generate_daily_report,
    "cron",
    hour=0
)




# API Routers
# app.include_router(api_router, prefix="/api/v1")