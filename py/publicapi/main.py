from fastapi import FastAPI
import uvicorn
from motor.motor_asyncio import AsyncIOMotorClient
from config import Api, Database

from .routers import ip_router 
from .routers import ip_list_router

app = FastAPI()

@app.on_event("startup")
async def startup_db_client():
    app.mongodb_client = AsyncIOMotorClient(Database.DB_URL)
    app.mongodb = app.mongodb_client[Database.DB_NAME]

@app.on_event("shutdown")
async def shutdown_db_client():
    app.mongodb_client.close()

app.include_router(ip_router, tags=["ip"], prefix="/ip")
app.include_router(ip_list_router, tags=["iplist"], prefix="/iplist")
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=General.HOST,
        reload=General.DEBUG_MODE,
        port=General.PORT,
    )
