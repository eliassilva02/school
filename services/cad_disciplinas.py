from models.disciplina import Disciplina
from repository.disciplina import DisciplinaRepo
from validations.disc_validations import DisciplinaValidations

class CadastrarDisciplina():
    def __init__(self) -> None:
        self.repo = DisciplinaRepo()

    def cadastrar(self, nome, ano, semestre):
        disc = Disciplina(nome=nome, ano=ano, semestre=semestre)
        validations = DisciplinaValidations(disc)
        isvalid, message = validations.is_valid()

        if isvalid == False:
            return isvalid, message
        
        self.repo.inserir_disciplina(disc)
        return True, ""



