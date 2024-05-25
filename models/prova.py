from pydantic import BaseModel
from decimal import Decimal

class Prova(BaseModel):
    sm1: Decimal
    sm2: Decimal
    av: Decimal
    avs: Decimal
    nf: Decimal | None