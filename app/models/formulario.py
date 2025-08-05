from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from backend.app.core.database import Base


class Formulario(Base):
    __tablename__ = "formulario"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True)
    descricao = Column(String)
    ordem = Column(Integer)

    # Relacionamento com a tabela Pergunta
    perguntas = relationship("Pergunta", back_populates="formulario")
