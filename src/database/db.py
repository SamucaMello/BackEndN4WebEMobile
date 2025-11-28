from dotenv import load_dotenv; load_dotenv()
from mongoengine import connect
from os import getenv   


try:
    connect(db="ProjetoWebMobile", host=getenv("MONGO_URI") or "mongodb://localhost:27017/ProjetoWebMobile")
except Exception as ex:
    print(f"Erro ao conectar ao banco de dados: {str(ex)}")
    exit(1)
