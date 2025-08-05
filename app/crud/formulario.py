from sqlalchemy.orm import Session

from backend.app.models.formulario import Formulario
from backend.app.schemas.formulario import FormularioCreate


def get_formulario(db: Session, formulario_id: int):
    # Busca um formulário pelo ID
    return db.query(Formulario).filter(Formulario.id == formulario_id).first()


def get_formularios(db: Session, skip: int = 0, limit: int = 100):
    # Lista todos os formulários com opções de pular (skip) e limitar (limit) resultados
    return db.query(Formulario).offset(skip).limit(limit).all()


def create_formulario(db: Session, formulario: FormularioCreate):
    # Cria uma nova instância de Formulario a partir dos dados do schema Pydantic
    db_formulario = Formulario(**formulario.dict())
    db.add(db_formulario)  # Adiciona o objeto à sessão
    db.commit()  # Salva as mudanças no banco de dados
    db.refresh(db_formulario)  # Atualiza o objeto com os dados do banco (ex: ID gerado)
    return db_formulario


def update_formulario(db: Session, formulario_id: int, formulario: FormularioCreate):
    # Busca o formulário pelo ID
    db_formulario = db.query(Formulario).filter(Formulario.id == formulario_id).first()
    if db_formulario:
        # Atualiza os atributos do objeto com os novos dados
        for key, value in formulario.dict().items():
            setattr(db_formulario, key, value)
        db.commit()
        db.refresh(db_formulario)
    return db_formulario


def delete_formulario(db: Session, formulario_id: int):
    # Busca o formulário pelo ID
    db_formulario = db.query(Formulario).filter(Formulario.id == formulario_id).first()
    if db_formulario:
        db.delete(db_formulario)  # Deleta o objeto da sessão
        db.commit()
    return db_formulario
