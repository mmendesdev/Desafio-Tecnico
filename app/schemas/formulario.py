from pydantic import BaseModel


class FormularioBase(BaseModel):
    titulo: str
    descricao: str | None = None
    ordem: int | None = None


class FormularioCreate(FormularioBase):
    pass


class Formulario(FormularioBase):
    id: int

    class Config:
        from_attributes = True
