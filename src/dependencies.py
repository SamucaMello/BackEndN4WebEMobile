from fastapi.responses import JSONResponse
import jwt
from os import getenv
from functools import wraps

class TokenManager:
    def create_token(id) -> str:
        return jwt.encode(dict(id = id), getenv("JWT_SECRET") or 'barata', algorithm='HS256')
    
    def decode_token(token: str) -> dict:
        return jwt.decode(token, getenv("JWT_SECRET") or 'barata', algorithms=['HS256'])
    

class RouterManager:
    @staticmethod
    def add_care(func):
        @wraps(func)  
        async def wrapper(*args, **kwargs):
            try:
                return await func(*args, **kwargs)
            except Exception as ex:
                print(f"Erro: {ex}") 
                return JSONResponse(
                    {"message": "Algo deu errado, verifique os campos e tente novamente."},
                    status_code=500
                )
        return wrapper