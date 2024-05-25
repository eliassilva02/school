from pydantic import BaseModel

class Aluno(BaseModel):
    matricula: str | None
    nome: str | None