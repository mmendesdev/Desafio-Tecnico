from sqlalchemy import and_
from sqlalchemy.orm import Session

from backend.app.models.pergunta import Pergunta, TipoPergunta
from backend.app.schemas.pergunta import PerguntaCreate


def get_pergunta(db: Session, pergunta_id: int):
    # Busca uma pergunta pelo ID
    return db.query(Pergunta).filter(Pergunta.id == pergunta_id).first()


def get_perguntas(db: Session, skip: int = 0, limit: int = 100):
    # Lista todas as perguntas com opções de pular (skip) e limitar (limit) resultados
    return db.query(Pergunta).offset(skip).limit(limit).all()


def get_perguntas_by_formulario(
    db: Session,
    formulario_id: int,
    tipo_pergunta: TipoPergunta = None,  # Filtro opcional por tipo de pergunta
    obrigatoria: bool = None,  # Filtro opcional por obrigatoriedade
    order_by: str = "ordem",  # Campo para ordenação
    skip: int = 0,
    limit: int = 100,
):
    # Constrói a query base filtrando pelo ID do formulário
    query = db.query(Pergunta).filter(Pergunta.id_formulario == formulario_id)

    # Aplica filtros condicionais
    if tipo_pergunta:
        query = query.filter(Pergunta.tipo_pergunta == tipo_pergunta)

    if obrigatoria is not None:
        query = query.filter(Pergunta.obrigatoria == obrigatoria)

    # Aplica ordenação
    if order_by == "ordem":
        query = query.order_by(Pergunta.ordem)
    elif order_by == "titulo":
        query = query.order_by(Pergunta.titulo)
    elif order_by == "id":
        query = query.order_by(Pergunta.id)

    # Aplica paginação e retorna os resultados
    return query.offset(skip).limit(limit).all()


def create_pergunta(db: Session, pergunta: PerguntaCreate):
    # Cria uma nova instância de Pergunta a partir dos dados do schema Pydantic
    db_pergunta = Pergunta(**pergunta.dict())
    db.add(db_pergunta)
    db.commit()
    db.refresh(db_pergunta)
    return db_pergunta


def update_pergunta(db: Session, pergunta_id: int, pergunta: PerguntaCreate):
    # Busca a pergunta pelo ID
    db_pergunta = db.query(Pergunta).filter(Pergunta.id == pergunta_id).first()
    if db_pergunta:
        # Atualiza os atributos do objeto com os novos dados
        for key, value in pergunta.dict().items():
            setattr(db_pergunta, key, value)
        db.commit()
        db.refresh(db_pergunta)
    return db_pergunta


def delete_pergunta(db: Session, pergunta_id: int):
    # Busca a pergunta pelo ID
    db_pergunta = db.query(Pergunta).filter(Pergunta.id == pergunta_id).first()
    if db_pergunta:
        db.delete(db_pergunta)
        db.commit()
    return db_pergunta
