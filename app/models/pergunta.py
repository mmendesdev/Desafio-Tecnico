import enum

from sqlalchemy import Boolean, Column, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from backend.app.core.database import Base


class TipoPergunta(str, enum.Enum):
    SIM_NAO = "Sim_Não"
    MULTIPLA_ESCOLHA = "multipla_escolha"
    UNICA_ESCOLHA = "unica_escolha"
    TEXTO_LIVRE = "texto_livre"
    INTEIRO = "Inteiro"
    NUMERO_COM_DUAS_CASAS_DECIMAIS = "Numero com duas casa decimais"


class Pergunta(Base):
    __tablename__ = "pergunta"

    id = Column(Integer, primary_key=True, index=True)
    id_formulario = Column(Integer, ForeignKey("formulario.id"))  # Chave estrangeira
    titulo = Column(String, index=True)
    codigo = Column(String, unique=True, index=True)
    orientacao_resposta = Column(String)
    ordem = Column(Integer)
    obrigatoria = Column(Boolean, default=False)
    sub_pergunta = Column(Boolean, default=False)
    tipo_pergunta = Column(Enum(TipoPergunta))  # Usando o Enum definido

    formulario = relationship("Formulario", back_populates="perguntas")
    opcoes_respostas = relationship("OpcoesRespostas", back_populates="pergunta")
