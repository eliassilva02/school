from models.nota import Nota
from infra.database import DB

class NotasRepo:
    def __init__(self) -> None:
        self.db = DB()
        self.db.open_connection()

    def inserir(self, nota: Nota):
        sql = f"""
            INSERT INTO public.notas
            VALUES (DEFAULT, '{nota.aluno}', '{nota.disciplina}','{nota.sm1}','{nota.sm2}','{nota.av}','{nota.avs}','{nota.nf}', '{nota.aprovado}')
        """
        self.db.manipulation(sql)

    def buscar_alunos(self, aluno):
        sql = f"""
            SELECT split_part(a.nome, ' ', 1), split_part(d.nome, ' ', 1), sm1, sm2, av, avs, nf, aprovado
            FROM public.notas as n
            INNER JOIN public.alunos as a
                ON a.matricula = n.aluno
            INNER JOIN public.disciplina as d
                ON d.id_disc = n.disciplina
            WHERE disciplina = '{aluno}'
        """

        response = self.db.select(sql)

        return response