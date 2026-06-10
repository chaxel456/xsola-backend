print("MAIN STARTING")
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from fastapi import WebSocket


from fastapi import FastAPI

from app.modules.auth.router import router as auth_router
from app.modules.users.router import router as user_router
from app.modules.devices.router import router as device_router
from app.modules.branches.router import router as branch_router

print("ROUTERS IMPORTED")

app = FastAPI(title="XSOLA API")

app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(device_router, prefix="/devices", tags=["Devices"])
app.include_router(branch_router, prefix="/branches", tags=["Branches"])

# DB
from app.core.database import Base, engine, get_db

# ROUTER AGGREGATOR

# AUTH SERVICE (only if you still want direct endpoints)
from app.modules.auth.service import AuthService
from app.modules.auth.schema import UserCreate, UserLogin

# WEBSOCKET
from app.websocket.telemetry_ws import telemetry_websocket


auth_service = AuthService()



Base.metadata.create_all(bind=engine)




# =========================
# ROOT
# =========================
@app.get("/")
def root():
    return {
        "message": "XSOLA API running",
        "status": "healthy"
    }


# =========================
# DB TEST
# =========================
@app.get("/test/db-insert-test", tags=["Test"])
def db_insert_test(db: Session = Depends(get_db)):
    try:
        db.execute(text("""
            CREATE TABLE IF NOT EXISTS test_connection (
                id SERIAL PRIMARY KEY,
                message TEXT
            )
        """))

        db.execute(
            text("INSERT INTO test_connection (message) VALUES ('hello supabase')")
        )
        db.commit()

        result = db.execute(
            text("SELECT message FROM test_connection ORDER BY id DESC LIMIT 1")
        ).scalar()

        return {
            "status": "success",
            "last_inserted": result
        }

    except Exception as e:
        db.rollback()
        return {
            "status": "failed",
            "error": str(e)
        }



@app.get("/debug/routes")
def debug_routes():
    return [route.path for route in app.routes]



# =========================
# DB HEALTH CHECK
# =========================
@app.get("/api/v1/db-check", tags=["Health"])
def db_check():
    try:
        conn = engine.connect()
        conn.close()
        return {"status": "DB connected ✅"}
    except Exception as e:
        return {"status": "DB failed ❌", "error": str(e)}


# =========================
# WEBSOCKET
# =========================
@app.websocket("/ws/telemetry")
async def websocket_endpoint(websocket: WebSocket):
    await telemetry_websocket(websocket)