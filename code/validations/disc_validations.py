from models.disciplina import Disciplina
from datetime import datetime

class DisciplinaValidations:
    def __init__(self, disciplina: Disciplina) -> None:
        self.disciplina = disciplina

    def is_valid(self):
        ano_valido = self.year_is_valid()
        semestre_valido = self.convert()

        if ano_valido == False:
            return False, "Ops! O ano que a disciplina foi colocada e invalido. Por favor, revise o ano e tente novamente."
        
        if semestre_valido == True:
            if int(self.disciplina.semestre) < 1 and int(self.disciplina.semestre) > 4:
                return False, "Ops! O semestre que voce colocou e invalido. Por favor, revise o ano e tente novamente."

        if len(self.disciplina.nome) < 2 or len(self.disciplina.nome) > 80:
            return False, "Ops! Parece que o nome que voce digitou nao esta no formato correto."

        return True, ""

    def year_is_valid(self):
        try:
            datetime.strptime(f"01/01/{self.disciplina.ano}", "%d/%m/%Y")
            return True
        except:
            return False
    
    def convert(self):
        try:
            num = int(self.disciplina.semestre)

            return True
        except:
            return False