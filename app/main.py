from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.database import Base, engine

from app.api.v1.router import api_router

from app.modules.auth import router as auth_router
from app.modules.users import router as users_router
from app.modules.branches import router as branches_router
from app.modules.customers import router as customers_router
from app.modules.devices import router as devices_router
from app.modules.inventory import router as inventory_router
from app.modules.maintenance import router as maintenance_router
from app.modules.notifications import router as notifications_router
from app.modules.payments import router as payments_router
from app.modules.reports import router as reports_router
from app.modules.subscriptions import router as subscriptions_router
from app.modules.telemetry import router as telemetry_router
from app.modules.waitlist import router as waitlist_router
from app.modules.tasks import router as tasks_router

from app.websocket.telemetry_ws import telemetry_websocket


@asynccontextmanager
async def lifespan(app: FastAPI):

    Base.metadata.create_all(bind=engine)

    yield


app = FastAPI(
    title="XSOLA API",
    version="1.0.0",
    description="XSOLA Branch Management System API",
    lifespan=lifespan
)


# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# API VERSION ROUTER
app.include_router(
    api_router,
    prefix="/api/v1"
)


# MODULE ROUTERS
app.include_router(auth_router)
app.include_router(users_router)
app.include_router(branches_router)
app.include_router(customers_router)
app.include_router(devices_router)
app.include_router(inventory_router)
app.include_router(maintenance_router)
app.include_router(notifications_router)
app.include_router(payments_router)
app.include_router(reports_router)
app.include_router(subscriptions_router)
app.include_router(telemetry_router)
app.include_router(waitlist_router)
app.include_router(tasks_router)


# ROOT
@app.get(
    "/",
    tags=["Health"]
)
async def root():
    return {
        "success": True,
        "message": "XSOLA API is running",
        "version": "1.0.0"
    }


# HEALTH CHECK
@app.get(
    "/health",
    tags=["Health"]
)
async def health_check():
    return {
        "success": True,
        "status": "healthy"
    }


# WEBSOCKET
@app.websocket("/ws/telemetry")
async def websocket_endpoint(websocket):
    await telemetry_websocket(websocket)