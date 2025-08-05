from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from backend.app.core.database import Base


class OpcoesRespostas(Base):
    __tablename__ = "opcoes_respostas"

    id = Column(Integer, primary_key=True, index=True)
    id_pergunta = Column(Integer, ForeignKey("pergunta.id"))
    resposta = Column(String)
    ordem = Column(Integer)
    resposta_aberta = Column(Boolean, default=False)
    pergunta = relationship("Pergunta", back_populates="opcoes_respostas")
    opcoes_resposta_pergunta = relationship(
        "OpcoesRespostaPergunta", back_populates="opcao_resposta"
    )
