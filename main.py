from fastapi import FastAPI
import gorjeta_Fuzzy

app = FastAPI() #uvicorn main:app --reload

#Nessa rota - executa função home
@app.post("/gorjeta")
def home(servico: int, qualidade: int): #Faz a validação da variavel

    return {"Gorjeta": gorjeta_Fuzzy.gorjeta(servico, qualidade)}