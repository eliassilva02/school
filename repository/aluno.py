from models.aluno import Aluno
from infra.database import DB

class AlunoRepo:
    def __init__(self) -> None:
        self.db = DB()
        self.db.open_connection()

    def inserir_aluno(self, aluno: Aluno) -> None:
        sql = f"""
            INSERT INTO public.alunos
            VALUES ({aluno.matricula}, '{aluno.nome}')
        """
        self.db.manipulation(sql)

