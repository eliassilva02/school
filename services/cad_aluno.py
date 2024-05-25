from models.aluno import Aluno
from repository.aluno import AlunoRepo
from validations.aluno_validations import AlunoValidations

class CadastrarAluno():
    def __init__(self) -> None:
        self.repo = AlunoRepo()

    def cadastrar(self, matricula, nome):
        aluno = Aluno(matricula=matricula, nome=nome)
        validation = AlunoValidations(aluno)

        isvalid, message = validation.is_valid()

        if isvalid == False:
            return isvalid, message

        self.repo.inserir_aluno(aluno)
        return True, ""
