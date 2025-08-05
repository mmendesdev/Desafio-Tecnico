from fastapi import FastAPI
from backend.app.core.database import engine, Base # Adicione Base e engine aqui

Base.metadata.create_all(bind=engine) # Adicione esta linha

app = FastAPI(
    title="API de Formulários Dinâmicos",
    description="API para gerenciar formulários e perguntas dinâmicas.",
    version="0.0.1",
)

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API de Formulários Dinâmicos!"}
