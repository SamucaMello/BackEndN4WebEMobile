from typing import Union
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from src.dependencies import TokenManager, RouterManager
from src.models.user import *

user_router = APIRouter(prefix="/user", tags=["Rota do usuario"])

@user_router.post("/register")
@RouterManager.add_care
async def register_user(request:Request, registerUser:RegisterUserModel):
    if User.objects(email=registerUser.email).first():
        return JSONResponse({"message": "Esse e-mail já foi cadastrado."}, 400)
    
    user = User(**registerUser.model_dump()).save()
    return JSONResponse(
        {"message": f"Usuário {user.nome} registrado com sucesso."})

@user_router.post("/login")
@RouterManager.add_care
async def login_user(request:Request, loginUser:LoginUserModel):
    found_user = User.objects(email=loginUser.email).first()
    if not found_user:
        return JSONResponse({"message": "E-mail ou senha inválidos."}, 400)
    
    if not bcrypt.checkpw(loginUser.senha.encode('utf-8'),  found_user.senha.encode('utf-8')):
        return JSONResponse({"message": "E-mail ou senha inválidos."}, 400) 

    return JSONResponse({
        "message": "Usuário logado com sucesso.", 
        "user": loginUser.email, 
        "token": TokenManager.create_token(found_user.id)
          })

@user_router.get("/{id}")
@RouterManager.add_care
def get_user_by_id(id: Union[int]):
    user = User.objects(id=id).first()
    if not user:
        return JSONResponse({"message": "Usuário não encontrado."}, 404)
    
    return JSONResponse(user.to_mongo().to_dict())