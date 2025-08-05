from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.app.core.database import get_db
from backend.app.crud import formulario as crud_formulario  # Importa as funções CRUD
from backend.app.schemas.formulario import Formulario, FormularioCreate

router = APIRouter()  # Cria um roteador FastAPI


@router.post("/", response_model=Formulario)
def create_formulario(formulario: FormularioCreate, db: Session = Depends(get_db)):
    # Endpoint para criar um novo formulário
    return crud_formulario.create_formulario(db=db, formulario=formulario)


@router.get("/", response_model=List[Formulario])
def read_formularios(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    # Endpoint para listar todos os formulários com paginação
    formularios = crud_formulario.get_formularios(db, skip=skip, limit=limit)
    return formularios


@router.get("/{formulario_id}", response_model=Formulario)
def read_formulario(formulario_id: int, db: Session = Depends(get_db)):
    # Endpoint para buscar um formulário por ID
    db_formulario = crud_formulario.get_formulario(db, formulario_id=formulario_id)
    if db_formulario is None:
        raise HTTPException(status_code=404, detail="Formulário não encontrado")
    return db_formulario


@router.put("/{formulario_id}", response_model=Formulario)
def update_formulario(
    formulario_id: int, formulario: FormularioCreate, db: Session = Depends(get_db)
):
    # Endpoint para atualizar um formulário existente
    db_formulario = crud_formulario.update_formulario(
        db, formulario_id=formulario_id, formulario=formulario
    )
    if db_formulario is None:
        raise HTTPException(status_code=404, detail="Formulário não encontrado")
    return db_formulario


@router.delete("/{formulario_id}", response_model=Formulario)
def delete_formulario(formulario_id: int, db: Session = Depends(get_db)):
    # Endpoint para deletar um formulário
    db_formulario = crud_formulario.delete_formulario(db, formulario_id=formulario_id)
    if db_formulario is None:
        raise HTTPException(status_code=404, detail="Formulário não encontrado")
    return db_formulario
