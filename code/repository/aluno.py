from models.aluno import Aluno
from infra.database import DB

class AlunoRepo:
    def __init__(self) -> None:
        self.db = DB()
        self.db.open_connection()

    def inserir_aluno(self, aluno: Aluno) -> None:
        sql = ""

        for disciplina in aluno.disciplinas:
            sql += f"""
                INSERT INTO public.alunos
                VALUES (DEFAULT, {aluno.matricula}, '{aluno.nome}', '{disciplina}');
            """
        self.db.manipulation(sql)

    def buscar_aluno(self, matricula):
        sql = f"""
            SELECT id_disciplina
            FROM public.alunos
            WHERE matricula = '{matricula}'
            LIMIT 1
        """

        response = self.db.select(sql)

        return response

    def buscar_alunos(self):
        sql = """
            SELECT matricula || ' - ' || nome
            FROM public.alunos
            GROUP BY matricula, nome
        """

        response = self.db.select(sql)

        return response

    def buscar_disciplina(self):
        sql = """
            SELECT id_disc || ' - ' || nome
            FROM public.disciplina
            ORDER BY nome
        """
        response = self.db.select(sql)

        return response

