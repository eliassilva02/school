# Diagrama de Entidade-Relacionamento (ER) do Modelo de Dados
---

O diagrama ER representa as entidades do sistema e seus relacionamentos:

## Entidades:

1. Aluno:
    - Matrícula
    - Nome
    - Disciplina
    
2. Disciplina:
    - Id_disciplina
    - Nome
    - Período (semestre e ano)

3. Nota:
    - Id_nota
    - matrícula
    - Id_disciplina
    - SM 1
    - SM 2
    - AV
    - AVS
    - NF (Nota Final)
    - Aprovado

## Relacionamentos:

- Um aluno pode ter várias notas. (1:N)
- Um aluno pode ter várias disciplinas. (1:N)
- Uma disciplina pode ter várias notas. (1:N)
- Uma disciplina pode ter vários alunos. (1:N)
- Uma nota pertence a um aluno e a uma disciplina. (N:M)