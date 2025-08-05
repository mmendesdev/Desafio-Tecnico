from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from backend.app.core.database import get_db
from backend.app.crud import pergunta as crud_pergunta
from backend.app.models.pergunta import TipoPergunta  # Importa o Enum para os filtros
from backend.app.schemas.pergunta import Pergunta, PerguntaCreate

router = APIRouter()


@router.post("/", response_model=Pergunta)
def create_pergunta(pergunta: PerguntaCreate, db: Session = Depends(get_db)):
    # Endpoint para criar uma nova pergunta
    return crud_pergunta.create_pergunta(db=db, pergunta=pergunta)


@router.get("/", response_model=List[Pergunta])
def read_perguntas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    # Endpoint para listar todas as perguntas com paginação
    perguntas = crud_pergunta.get_perguntas(db, skip=skip, limit=limit)
    return perguntas


@router.get("/formulario/{formulario_id}", response_model=List[Pergunta])
def read_perguntas_by_formulario(
    formulario_id: int,
    tipo_pergunta: Optional[TipoPergunta] = Query(
        None, description="Filtrar por tipo de pergunta"
    ),
    obrigatoria: Optional[bool] = Query(
        None, description="Filtrar por obrigatoriedade"
    ),
    order_by: str = Query("ordem", description="Ordenar por: ordem, titulo, id"),
    skip: int = Query(0, description="Número de registros para pular"),
    limit: int = Query(100, description="Número máximo de registros"),
    db: Session = Depends(get_db),
):
    # Endpoint para listar perguntas de um formulário com filtros, ordenação e paginação
    perguntas = crud_pergunta.get_perguntas_by_formulario(
        db,
        formulario_id=formulario_id,
        tipo_pergunta=tipo_pergunta,
        obrigatoria=obrigatoria,
        order_by=order_by,
        skip=skip,
        limit=limit,
    )
    return perguntas


@router.get("/{pergunta_id}", response_model=Pergunta)
def read_pergunta(pergunta_id: int, db: Session = Depends(get_db)):
    # Endpoint para buscar uma pergunta por ID
    db_pergunta = crud_pergunta.get_pergunta(db, pergunta_id=pergunta_id)
    if db_pergunta is None:
        raise HTTPException(status_code=404, detail="Pergunta não encontrada")
    return db_pergunta


@router.put("/{pergunta_id}", response_model=Pergunta)
def update_pergunta(
    pergunta_id: int, pergunta: PerguntaCreate, db: Session = Depends(get_db)
):
    # Endpoint para atualizar uma pergunta existente
    db_pergunta = crud_pergunta.update_pergunta(
        db, pergunta_id=pergunta_id, pergunta=pergunta
    )
    if db_pergunta is None:
        raise HTTPException(status_code=404, detail="Pergunta não encontrada")
    return db_pergunta


@router.delete("/{pergunta_id}", response_model=Pergunta)
def delete_pergunta(pergunta_id: int, db: Session = Depends(get_db)):
    # Endpoint para deletar uma pergunta
    db_pergunta = crud_pergunta.delete_pergunta(db, pergunta_id=pergunta_id)
    if db_pergunta is None:
        raise HTTPException(status_code=404, detail="Pergunta não encontrada")
    return db_pergunta
