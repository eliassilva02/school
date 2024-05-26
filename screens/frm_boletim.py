from operator import imod
import tkinter as tk
from services.cad_aluno import CadastrarAluno
from services.cad_notas import CadastroNotas
from tkinter import ACTIVE, messagebox
from screens.config import style
import customtkinter as cttk
from screens.util import Table

class FrmBoletim(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.construir_forms()

    def construir_forms(self):
        self.titulo()
        self.config(bg=style["COLOR_CORPO_PRINCIPAL"])
        self.build_parameters()

    def titulo(self):
        self.barra_superior = tk.Frame(self.parent, bg=style["COLOR_CORPO_PRINCIPAL"])
        self.barra_superior.pack(side=tk.TOP, fill=tk.BOTH, expand=False)

        self.labelTitulo = tk.Label(self.barra_superior, text="Cadastro de Alunos")
        self.labelTitulo.config(fg="#222d33", font=("Montserrat", 30), bg=style["COLOR_CORPO_PRINCIPAL"])
        self.labelTitulo.pack(side=tk.TOP, fill='both', expand=True)

        self.separator = tk.Label(self.barra_superior, text=style["SEPARATOR"])
        self.separator.config(fg="#3F3F3F", font=("Roboto", 5), bg=style["COLOR_CORPO_PRINCIPAL"])
        self.separator.pack(side=tk.TOP, fill='both', expand=True, pady=20)

    def build_parameters(self):
        self.barra_inferior_3 = tk.Frame(self.parent, bg=style["COLOR_CORPO_PRINCIPAL"])
        self.barra_inferior_3.pack(side=tk.TOP, fill=tk.BOTH, expand=False)

        yscrollbar = tk.Scrollbar(self.barra_inferior_3) 
        yscrollbar.pack(side =tk.RIGHT, fill = tk.X) 
  
        label = tk.Label(self.barra_inferior_3, text="Disciplinas: ")
        label.config(fg="#3f3f3f", font=("Montserrat", 15), padx=15, bg=style["COLOR_CORPO_PRINCIPAL"])
        label.pack(side=tk.LEFT, fill='both', expand=False)
        
        self.listbox = tk.Listbox(self.barra_inferior_3, selectmode = "multiple", yscrollcommand = yscrollbar.set, bg=style["COLOR_CORPO_PRINCIPAL"], height=1, width=80)
        self.listbox.pack(side=tk.LEFT, pady=20, expand = tk.NO, fill = "both") 
        self.add_items()
        
        yscrollbar.config(command = self.listbox.yview)

        self.button = cttk.CTkButton(
            master=self.barra_inferior_3,
            width=100,
            height=10,
            border_width=0,
            corner_radius=8,
            text="Buscar",
            text_color=style["COLOR_LABEL"],
            fg_color = style["COLOR_BUTTON"],
            command=lambda: self.buscar_notas()
            )
        self.button.pack(side=tk.RIGHT, fill='both', expand=False)

    def add_items(self):
        service = CadastrarAluno()
        x = service.buscar_disciplinas()

        for each_item in range(len(x)): 
            self.listbox.insert(tk.END, x[each_item])

    def buscar_notas(self):
        self.barra_inferior = tk.Frame(self.parent, bg=style["COLOR_CORPO_PRINCIPAL"], padx=20)
        self.barra_inferior.pack(side=tk.LEFT, fill=tk.BOTH, expand=False)
        disciplina = self.listbox.get(ACTIVE).split('-')[0].strip()

        nota = CadastroNotas()
        data = nota.buscar_notas(disciplina)

        if len(data) <= 0:
            messagebox.showerror("Atencao", "Nao ha nenhuma registro nessa disciplina")
        else:
            table = Table(self.barra_inferior, data)
