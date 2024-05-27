from models.aluno import Aluno
from repository.aluno import AlunoRepo
from validations.aluno_validations import AlunoValidations
from itertools import chain

class CadastrarAluno():
    def __init__(self) -> None:
        self.repo = AlunoRepo()

    def cadastrar(self, matricula, nome, disciplinas):
        disciplinas = self.refinar_disciplinas(disciplinas)
        aluno = Aluno(matricula=matricula, nome=nome, disciplinas=disciplinas)
        validation = AlunoValidations(aluno)

        aluno_existe = self.buscar_aluno(matricula)
        if len(aluno_existe) > 0:
            return False, "Ops! Este aluno ja existe. Tente novamente."

        isvalid, message = validation.is_valid()
        if isvalid == False:
            return isvalid, message

        self.repo.inserir_aluno(aluno)
        return True, ""

    def buscar_disciplinas(self):
        response = self.repo.buscar_disciplina()

        return list(chain(*response))

    def buscar_aluno(self, matricula):
        response = self.repo.buscar_aluno(matricula)

        return response

    def buscar_alunos(self):
        response = self.repo.buscar_alunos()

        return list(chain(*response))

    def refinar_disciplinas(self, disciplinas):
        for i in range(len(disciplinas)):
            disciplina = disciplinas[i].split()
            disciplinas[i] = disciplina[0].strip()

        return disciplinas
            
