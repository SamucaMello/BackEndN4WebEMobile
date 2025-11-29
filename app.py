from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes.user_route import user_router
import src.database.db


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],  # Allows all HTTP methods (GET, POST, PUT, DELETE, etc.)
        allow_headers=["*"],  # Allows all headers in the request
    )

app.include_router(user_router)