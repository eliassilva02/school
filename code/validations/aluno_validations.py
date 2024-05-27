from models.aluno import Aluno
import re

class AlunoValidations:
    def __init__(self, aluno: Aluno) -> None:
        self.aluno = aluno

    def is_valid(self):
        so_tem_numeros = re.search(r"^[0-9]+$", self.aluno.matricula) is not None

        if len(self.aluno.matricula) != 12 or so_tem_numeros == False:
            return False, "Ops! A matricula que voce digitou parece estar no formato incorreto. As matriculas em nosso sistema precisam ter exatamente 12 numeros. Por favor, revise sua matricula e tente novamente."

        if len(self.aluno.nome) < 2 or len(self.aluno.nome) > 80:
            return False, "Ops! Parece que o nome que voce digitou nao esta no formato correto."

        if len(self.aluno.disciplinas) <= 0:
            return False, "Ops! Voce nao selecionou nenhuma disciplina. Tente novamente!!"

        return True, ""