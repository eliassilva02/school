from unicodedata import decimal
from models.nota import Nota
from decimal import Decimal

class NotaValidations:
    def __init__(self, sm, av, aluno, disciplina) -> None:
        self.sm = sm
        self.av = av
        self.aluno = aluno
        self.disciplina = disciplina

    def is_valid(self):
        errors = 0
        notas = [self.sm[0], self.sm[1], self.av[0], self.av[1]]
        for nota in notas:
            number = self.is_number(nota)
            if number == False:
                errors += 1
                break

        if errors > 0 or (Decimal(self.sm[0]) > 1 or Decimal(self.sm[1]) > 1) or (Decimal(self.av[0]) > 10 or Decimal(self.av[1]) > 10):
            return False, "Ops! Algumas das notas registradas e invalida. Tente novamente."

        if self.aluno == "" or self.disciplina == "":
            return False, "Ops! O aluno ou a disciplina nao foi selecionada. Tente novamente."

        return True, ""

    def is_number(self, number):
        try:
            Decimal(number)
            return True
        except:
            return False