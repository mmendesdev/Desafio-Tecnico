# backend/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # Importe o CORSMiddleware

from backend.app.api import formulario, pergunta
from backend.app.core.config import settings  # Importe as configurações
from backend.app.core.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,  # Usa o nome do projeto das configurações
    description="API para gerenciar formulários e perguntas dinâmicas.",
    version=settings.PROJECT_VERSION,  # Usa a versão do projeto das configurações
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "*"
    ],  # Permite todas as origens. Para produção, liste os domínios permitidos.
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Permite todos os cabeçalhos
)

app.include_router(formulario.router, prefix="/formularios", tags=["formularios"])
app.include_router(pergunta.router, prefix="/perguntas", tags=["perguntas"])


@app.get("/")
def read_root():
    return {
        "message": "API de Formulários Dinâmicos",
        "version": settings.PROJECT_VERSION,
    }
