from models.disciplina import Disciplina
from infra.database import DB

class DisciplinaRepo:
    def __init__(self) -> None:
        self.db = DB()
        self.db.open_connection()

    def inserir_disciplina(self, disciplina: Disciplina) -> None:
        sql = f"""
            INSERT INTO public.disciplina
            VALUES (DEFAULT, '{disciplina.nome}', '{str(disciplina.semestre).zfill(2)}.{disciplina.ano}')
        """
        self.db.manipulation(sql)