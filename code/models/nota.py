from pydantic import BaseModel
from decimal import Decimal

class Nota(BaseModel):
    sm1: Decimal
    sm2: Decimal
    av: Decimal
    avs: Decimal
    nf: Decimal | None
    aluno: str
    disciplina: str
    aprovado: str  = 'N'
