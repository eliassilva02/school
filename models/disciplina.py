from pydantic import BaseModel

class Disciplina(BaseModel):
    nome: str
    ano: int
    semestre: int