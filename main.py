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

@app.get("/")
def read_root():
    return {"Hello": "World"}

# Nessa rota - executa função home
@ app.post("/gorjeta")
def home(servico: int, comida: int):  # Faz a validação da variavel
    
    return {"gorjeta": gorjeta_Fuzzy.gorjeta(servico, comida)}

# Para rodar o servidor
# uvicorn main:app --reload