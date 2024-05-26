from repository.notas import NotasRepo
from models.nota import Nota
from validations.nota_validation import NotaValidations
from decimal import Decimal

class CadastroNotas():
    def __init__(self) -> None:
        self.repo = NotasRepo()

    def inserir_notas(self, sm, av, aluno, disciplina):
        validations = NotaValidations(sm, av, aluno, disciplina)
        isvalid, message = validations.is_valid()

        if isvalid == False:
            return isvalid, message

        nota = Nota(sm1=Decimal(sm[0]), sm2=Decimal(sm[1]), av=Decimal(av[0]), avs=Decimal(av[1]), aluno=self.refinar(aluno), disciplina=self.refinar(disciplina))
        self.calcular_nota_final(nota)
        self.repo.inserir(nota)

        return True, ""

    def calcular_nota_final(self, nota):
        nota_final = nota.av
        sm_inseriu = False

        if nota.av < nota.avs:
            nota_final = nota.avs

        if nota_final < 9:
            nota_final += nota.sm1 + nota.sm2
            sm_inseriu = True
        
        if nota_final == 9 and sm_inseriu == False:
            if nota.sm1 < nota.sm2:
                nota_final += nota.sm2
            else:
                nota_final += nota.sm1
        
        if nota_final > 6:
            nota.aprovado = 'S'

        nota.nf = nota_final

    def refinar(self, value):
        return value.split('-')[0].strip()

    def buscar_notas(self, idd):
        return self.repo.buscar_alunos(idd)