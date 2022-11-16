from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import gorjeta_Fuzzy

app = FastAPI()  # uvicorn app:app --reload

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

# Nessa rota - executa função home
@ app.post("/gorjeta")
def home(servico: int, qualidade: int):  # Faz a validação da variavel
    
    return {"gorjeta": gorjeta_Fuzzy.gorjeta(servico, qualidade)}

# Para rodar o servidor
# uvicorn main:app --reload