from fastapi import FastAPI
from src.routes.user_route import user_router
import src.database.db


app = FastAPI()

app.include_router(user_router)