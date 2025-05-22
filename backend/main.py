"""PonyExpress backend API application.

Args:
    app (FastAPI): The FastAPI application
"""

from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from backend.dependencies import create_db_tables
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from backend.routers import equipment
from backend.exceptions import ClientErrorException


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_tables()
    yield

app = FastAPI(
    title="BBstats",
    summary="Provides functions to retrieve bowling ball stats",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(equipment.router)

@app.get("/status", response_model=None, status_code=204)
def status():
    pass

@app.get("/")
def template():
    return True

@app.exception_handler(ClientErrorException)
def handle_client_error(request: Request, exc: ClientErrorException):
    return exc.response()

