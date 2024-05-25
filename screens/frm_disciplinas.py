from operator import imod
import tkinter as tk
from services.cad_aluno import CadastrarAluno
from tkinter import messagebox
from screens.config import style
import customtkinter as cttk

class FrmDisciplina(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.construir_forms()

    def construir_forms(self):
        self.titulo()
        self.config(bg=style["COLOR_CORPO_PRINCIPAL"])
        self.build_nome()
        self.build_semestre()
        self.build_ano()
        self.build_button()
        
    def titulo(self):
        self.barra_superior = tk.Frame(self.parent, bg=style["COLOR_CORPO_PRINCIPAL"])
        self.barra_superior.pack(side=tk.TOP, fill=tk.BOTH, expand=False)

        self.labelTitulo = tk.Label(self.barra_superior, text="Cadastro de Disciplinas")
        self.labelTitulo.config(fg="#222d33", font=("Montserrat", 30), bg=style["COLOR_CORPO_PRINCIPAL"])
        self.labelTitulo.pack(side=tk.TOP, fill='both', expand=True)

        self.separator = tk.Label(self.barra_superior, text=style["SEPARATOR"])
        self.separator.config(fg="#3F3F3F", font=("Roboto", 5), bg=style["COLOR_CORPO_PRINCIPAL"])
        self.separator.pack(side=tk.TOP, fill='both', expand=True, pady=20)
        

    def build_nome(self):
        self.barra_superior_1 = tk.Frame(self.parent, bg=style["COLOR_CORPO_PRINCIPAL"])
        self.barra_superior_1.pack(side=tk.TOP, fill=tk.BOTH, expand=False) 

        self.label_nome_disciplina = tk.Label(self.barra_superior_1, text="Nome: ")
        self.label_nome_disciplina.config(fg="#3f3f3f", font=("Montserrat", 15), padx=30, bg=style["COLOR_CORPO_PRINCIPAL"])
        self.label_nome_disciplina.pack(side=tk.LEFT, fill='both', expand=False)

        self.entry_nome = cttk.CTkEntry(
            master=self.barra_superior_1,
            placeholder_text="Digite o nome da disciplina...",
            fg_color=style["COLOR_CORPO_PRINCIPAL"],
            border_color=style["COLOR_BORDER"],
            corner_radius=5,
            border_width=1,
            width=500,
            height=30,
            text_color = "#3f3f3f"
        )
        self.entry_nome.pack(side=tk.LEFT, fill='both', expand=False)

    def build_semestre(self):
        self.barra_superior_2 = tk.Frame(self.parent, bg=style["COLOR_CORPO_PRINCIPAL"])
        self.barra_superior_2.pack(side=tk.TOP, fill=tk.BOTH, expand=False, pady=20) 

        self.label_semetre = tk.Label(self.barra_superior_2, text="Semestre: ")
        self.label_semetre.config(fg="#3f3f3f", font=("Montserrat", 15), padx=15, bg=style["COLOR_CORPO_PRINCIPAL"])
        self.label_semetre.pack(side=tk.LEFT, fill='both', expand=False)

        self.entry_semestre = cttk.CTkEntry(
            master=self.barra_superior_2,
            placeholder_text="Digite o semestre...",
            fg_color=style["COLOR_CORPO_PRINCIPAL"],
            border_color=style["COLOR_BORDER"],
            corner_radius=5,
            border_width=1,
            width=150,
            height=30,
            text_color = "#3f3f3f"
        ) 
        self.entry_semestre.pack(side=tk.LEFT, fill='both', expand=False)

    def build_ano(self):
        self.barra_inferior = tk.Frame(self.parent, bg=style["COLOR_CORPO_PRINCIPAL"])
        self.barra_inferior.pack(side=tk.TOP, fill=tk.BOTH, expand=False) 

        self.label_ano = tk.Label(self.barra_inferior, text="Ano: ")
        self.label_ano.config(fg="#3f3f3f", font=("Montserrat", 15), padx=40, bg=style["COLOR_CORPO_PRINCIPAL"])
        self.label_ano.pack(side=tk.LEFT, fill='both', expand=False)

        self.entry_ano = cttk.CTkEntry(
            master=self.barra_inferior,
            placeholder_text="Digite o ano...",
            fg_color=style["COLOR_CORPO_PRINCIPAL"],
            border_color=style["COLOR_BORDER"],
            corner_radius=5,
            border_width=1,
            width=150,
            height=30,
            text_color = "#3f3f3f"
        ) 
        self.entry_ano.pack(side=tk.LEFT, fill='both', expand=False)

    def build_button(self):
        self.barra_inferior_2 = tk.Frame(self.parent, bg=style["COLOR_CORPO_PRINCIPAL"])
        self.barra_inferior_2.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=False)

        self.button = cttk.CTkButton(
            master=self.barra_inferior_2,
            width=150,
            height=42,
            border_width=0,
            corner_radius=8,
            text="Cadastrar",
            text_color=style["COLOR_LABEL"],
            fg_color = style["COLOR_BUTTON"],
            command=lambda: self.cadastrar_aluno()
            )
        self.button.pack(side=tk.RIGHT, fill='both', expand=False, padx=80, pady=90)

    def cadastrar_aluno(self):
        matricula = self.entry_matricula.get()
        nome = self.entry_nome.get()
        service = CadastrarAluno()
        retorno = service.cadastrar(matricula, nome)

        if retorno[0] == False:
            messagebox.showerror("Atenção", retorno[1])
        else:
            messagebox.showinfo("Concluído", "Aluno cadastrado com sucesso!!")
            self.entry_matricula.delete(0, len(matricula))
            self.entry_nome.delete(0, len(nome))