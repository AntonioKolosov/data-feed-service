"""
Set webhooks/unset webhooks
"""

from typing import Dict

from fastapi import FastAPI
from dotenv import load_dotenv

from .description import description, title, version, license, contact
from src import router

app = FastAPI(
    title=title,
    description=description,
    version=version,
    contact=contact,
    license=license
)

load_dotenv()

app.include_router(router.router)


@app.get("/", tags=["ROOT"])
def read_root() -> Dict:
    return {"pong": "Data feed service is live"}


@app.on_event("startup")
async def startup():
    """Startup"""
    print("Startup")


@app.on_event("shutdown")
async def shutdown():
    """Shutdown"""
    print("Shutdown")
