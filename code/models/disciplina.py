from pydantic import BaseModel

class Disciplina(BaseModel):
    nome: str
    ano: str
    semestre: str