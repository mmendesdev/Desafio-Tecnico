from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from backend.app.core.database import Base

class OpcoesRespostaPergunta(Base):
    __tablename__ = "opcoes_resposta_pergunta"

    id = Column(Integer, primary_key=True, index=True)
    id_opcao_resposta = Column(Integer, ForeignKey("opcoes_respostas.id"))
    id_pergunta = Column(Integer, ForeignKey("pergunta.id"))

    opcao_resposta = relationship("OpcoesRespostas", back_populates="opcoes_resposta_pergunta")
    pergunta = relationship("Pergunta") # Não precisa de back_populates aqui se o relacionamento for unidirecional
