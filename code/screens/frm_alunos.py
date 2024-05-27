from operator import imod
import tkinter as tk
from services.cad_aluno import CadastrarAluno
from tkinter import ACTIVE, messagebox
from screens.config import style
import customtkinter as cttk

class FrmAlunos(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.construir_forms()

    def construir_forms(self):
        self.titulo()
        self.config(bg=style["COLOR_CORPO_PRINCIPAL"])
        self.build_matricula()
        self.build_nome()
        self.build_button()
        self.build_disciplinas()
    
    def titulo(self):
        self.barra_superior = tk.Frame(self.parent, bg=style["COLOR_CORPO_PRINCIPAL"])
        self.barra_superior.pack(side=tk.TOP, fill=tk.BOTH, expand=False)

        self.labelTitulo = tk.Label(self.barra_superior, text="Cadastro de Alunos")
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
        self.label_nome_disciplina.pack(side=tk.LEFT, fill='x', expand=False)

        self.entry_nome = cttk.CTkEntry(
            master=self.barra_superior_1,
            placeholder_text="Digite o nome do aluno...",
            fg_color=style["COLOR_CORPO_PRINCIPAL"],
            border_color=style["COLOR_BORDER"],
            corner_radius=5,
            border_width=1,
            width=600,
            height=30,
            text_color = "#3f3f3f"
        )
        self.entry_nome.pack(side=tk.LEFT, fill='both', expand=False)

    def build_matricula(self):
        self.barra_superior_2 = tk.Frame(self.parent, bg=style["COLOR_CORPO_PRINCIPAL"])
        self.barra_superior_2.pack(side=tk.TOP, fill=tk.BOTH, expand=False, pady=20) 

        self.labelMatricula = tk.Label(self.barra_superior_2, text="Matrícula: ")
        self.labelMatricula.config(fg="#3f3f3f", font=("Montserrat", 15), padx=15, bg=style["COLOR_CORPO_PRINCIPAL"])
        self.labelMatricula.pack(side=tk.LEFT, fill='both', expand=False)

        self.entry_matricula = cttk.CTkEntry(
            master=self.barra_superior_2,
            placeholder_text="Digite a matrícula do aluno...",
            fg_color=style["COLOR_CORPO_PRINCIPAL"],
            border_color=style["COLOR_BORDER"],
            corner_radius=5,
            border_width=1,
            width=600,
            height=30,
            text_color = "#3f3f3f"
        ) 
        self.entry_matricula.pack(side=tk.LEFT, fill='both', expand=False)

    def build_disciplinas(self):
        self.barra_inferior_3 = tk.Frame(self.parent, bg=style["COLOR_CORPO_PRINCIPAL"])
        self.barra_inferior_3.pack(side=tk.TOP, fill=tk.BOTH, expand=False)

        yscrollbar = tk.Scrollbar(self.barra_inferior_3) 
        yscrollbar.pack(side =tk.RIGHT, fill = tk.X) 
  
        label = tk.Label(self.barra_inferior_3, text="Disciplinas: ")
        label.config(fg="#3f3f3f", font=("Montserrat", 15), padx=15, bg=style["COLOR_CORPO_PRINCIPAL"])
        label.pack(side=tk.LEFT, fill='both', expand=False)
        
        self.listbox = tk.Listbox(self.barra_inferior_3, selectmode = "multiple", yscrollcommand = yscrollbar.set, bg=style["COLOR_CORPO_PRINCIPAL"])
        self.listbox.pack(side=tk.LEFT, pady=20, expand = tk.NO, fill = "both") 
        self.add_items()
        
        yscrollbar.config(command = self.listbox.yview)

    def add_items(self):
        service = CadastrarAluno()
        x = service.buscar_disciplinas()

        for each_item in range(len(x)): 
            self.listbox.insert(tk.END, x[each_item])

    def build_button(self):
        self.barra_inferior = tk.Frame(self.parent, bg=style["COLOR_CORPO_PRINCIPAL"])
        self.barra_inferior.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=False)

        self.button = cttk.CTkButton(
            master=self.barra_inferior,
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
        disciplinas = self.get_disciplinas()
        
        service = CadastrarAluno()
        retorno = service.cadastrar(matricula, nome, disciplinas)

        if retorno[0] == False:
            messagebox.showerror("Atenção", retorno[1])
        else:
            messagebox.showinfo("Concluído", "Aluno cadastrado com sucesso!!")
            self.entry_matricula.focus()
            self.entry_matricula.delete(0, len(matricula))
            self.entry_nome.delete(0, len(nome))
            self.listbox.delete(0, tk.END)
            self.add_items()

    def get_disciplinas(self):
        disciplinas = []
        for index in self.listbox.curselection():
            item = self.listbox.get(index)
            disciplinas.append(item)

        return disciplinas
