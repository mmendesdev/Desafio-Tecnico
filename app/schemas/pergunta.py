from pydantic import BaseModel

from backend.app.models.pergunta import TipoPergunta


class PerguntaBase(BaseModel):
    titulo: str
    codigo: str
    orientacao_resposta: str | None = None
    ordem: int | None = None
    obrigatoria: bool = False
    sub_pergunta: bool = False
    tipo_pergunta: TipoPergunta  # Usamos o Enum aqui para validação


class PerguntaCreate(PerguntaBase):
    # Para a criação, precisamos do ID do formulário ao qual a pergunta pertence
    id_formulario: int


class Pergunta(PerguntaBase):
    # Para o modelo de retorno, incluímos o ID da pergunta e o ID do formulário
    id: int
    id_formulario: int

    class Config:
        from_attributes = True
