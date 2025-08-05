# backend/main.py
from fastapi import FastAPI

from backend.app.api import formulario, pergunta  # Importe os roteadores
from backend.app.core.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API de Formulários Dinâmicos",
    description="API para gerenciar formulários e perguntas dinâmicas.",
    version="0.0.1",
)

# Inclua os roteadores da API
app.include_router(formulario.router, prefix="/formularios", tags=["formularios"])
app.include_router(pergunta.router, prefix="/perguntas", tags=["perguntas"])


@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API de Formulários Dinâmicos!"}
