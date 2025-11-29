from mongoengine import Document, EmailField, StringField,SequenceField
from pydantic import BaseModel, EmailStr
import bcrypt


class User(Document):
    nome    = StringField(required=True)
    email   = EmailField(required=True, unique=True)
    senha   = StringField(required=True)
    id      =   SequenceField(primary_key=True)
    
    def save(self, *args, **kwargs):
        self.senha = bcrypt.hashpw(self.senha.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        return super().save(*args, **kwargs)
    

class RegisterUserModel(BaseModel):
    nome: str
    email: str
    senha: str

class LoginUserModel(BaseModel):
    email: EmailStr
    senha: str
