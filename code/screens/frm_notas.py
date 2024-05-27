from operator import imod
import tkinter as tk
from services.cad_aluno import CadastrarAluno
from services.cad_disciplinas import CadastrarDisciplina
from services.cad_notas import CadastroNotas
from tkinter import ACTIVE, messagebox
from screens.config import style
import customtkinter as cttk

class FrmNotas(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.construir_forms()

    def construir_forms(self):
        self.titulo()
        self.config(bg=style["COLOR_CORPO_PRINCIPAL"])
        self.build_sm1()
        self.build_sm2()
        self.build_av()
        self.build_avs()
        self.build_button()
        self.build_disciplinas()
        self.build_alunos()
    
    def titulo(self):
        self.barra_superior = tk.Frame(self.parent, bg=style["COLOR_CORPO_PRINCIPAL"])
        self.barra_superior.pack(side=tk.TOP, fill=tk.BOTH, expand=False)

        self.labelTitulo = tk.Label(self.barra_superior, text="Cadastro de Notas")
        self.labelTitulo.config(fg="#222d33", font=("Montserrat", 30), bg=style["COLOR_CORPO_PRINCIPAL"])
        self.labelTitulo.pack(side=tk.TOP, fill='both', expand=True)

        self.separator = tk.Label(self.barra_superior, text=style["SEPARATOR"])
        self.separator.config(fg="#3F3F3F", font=("Roboto", 5), bg=style["COLOR_CORPO_PRINCIPAL"])
        self.separator.pack(side=tk.TOP, fill='both', expand=True, pady=10)     

    def build_sm2(self):
        self.barra_superior_1 = tk.Frame(self.parent, bg=style["COLOR_CORPO_PRINCIPAL"])
        self.barra_superior_1.pack(side=tk.TOP, fill=tk.BOTH, expand=False) 

        self.label_nome_disciplina = tk.Label(self.barra_superior_1, text="SM 2: ")
        self.label_nome_disciplina.config(fg="#3f3f3f", font=("Montserrat", 15), padx=15, bg=style["COLOR_CORPO_PRINCIPAL"])
        self.label_nome_disciplina.pack(side=tk.LEFT, fill='x', expand=False)

        self.entry_sm2 = cttk.CTkEntry(
            master=self.barra_superior_1,
            placeholder_text="Digite o nota SM 2 do aluno...",
            fg_color=style["COLOR_CORPO_PRINCIPAL"],
            border_color=style["COLOR_BORDER"],
            corner_radius=5,
            border_width=1,
            width=600,
            height=30,
            text_color = "#3f3f3f"
        )
        self.entry_sm2.pack(side=tk.LEFT, fill='both', expand=False)

    def build_sm1(self):
        self.barra_superior_2 = tk.Frame(self.parent, bg=style["COLOR_CORPO_PRINCIPAL"])
        self.barra_superior_2.pack(side=tk.TOP, fill=tk.BOTH, expand=False, pady=10) 

        self.labelMatricula = tk.Label(self.barra_superior_2, text="SM 1: ")
        self.labelMatricula.config(fg="#3f3f3f", font=("Montserrat", 15), padx=15, bg=style["COLOR_CORPO_PRINCIPAL"])
        self.labelMatricula.pack(side=tk.LEFT, fill='both', expand=False)

        self.entry_sm1 = cttk.CTkEntry(
            master=self.barra_superior_2,
            placeholder_text="Digite a nota SM 1 do aluno...",
            fg_color=style["COLOR_CORPO_PRINCIPAL"],
            border_color=style["COLOR_BORDER"],
            corner_radius=5,
            border_width=1,
            width=600,
            height=30,
            text_color = "#3f3f3f"
        ) 
        self.entry_sm1.pack(side=tk.LEFT, fill='both', expand=False)

    def build_av(self):
        self.barra_superior_3 = tk.Frame(self.parent, bg=style["COLOR_CORPO_PRINCIPAL"])
        self.barra_superior_3.pack(side=tk.TOP, fill=tk.BOTH, expand=False, pady=10) 

        self.labelMatricula = tk.Label(self.barra_superior_3, text="AV: ")
        self.labelMatricula.config(fg="#3f3f3f", font=("Montserrat", 15), padx=15, bg=style["COLOR_CORPO_PRINCIPAL"])
        self.labelMatricula.pack(side=tk.LEFT, fill='both', expand=False)

        self.entry_av = cttk.CTkEntry(
            master=self.barra_superior_3,
            placeholder_text="Digite a nota AV do aluno...",
            fg_color=style["COLOR_CORPO_PRINCIPAL"],
            border_color=style["COLOR_BORDER"],
            corner_radius=5,
            border_width=1,
            width=600,
            height=30,
            text_color = "#3f3f3f"
        ) 
        self.entry_av.pack(side=tk.LEFT, fill='both', expand=False,padx=23)

    def build_avs(self):
        self.barra_superior_4 = tk.Frame(self.parent, bg=style["COLOR_CORPO_PRINCIPAL"])
        self.barra_superior_4.pack(side=tk.TOP, fill=tk.BOTH, expand=False, pady=5) 

        self.labelMatricula = tk.Label(self.barra_superior_4, text="AVS: ")
        self.labelMatricula.config(fg="#3f3f3f", font=("Montserrat", 15), padx=15, bg=style["COLOR_CORPO_PRINCIPAL"])
        self.labelMatricula.pack(side=tk.LEFT, fill='both', expand=False)

        self.entry_avs = cttk.CTkEntry(
            master=self.barra_superior_4,
            placeholder_text="Digite a nota AV do aluno...",
            fg_color=style["COLOR_CORPO_PRINCIPAL"],
            border_color=style["COLOR_BORDER"],
            corner_radius=5,
            border_width=1,
            width=600,
            height=30,
            text_color = "#3f3f3f",
        ) 
        self.entry_avs.pack(side=tk.LEFT, fill='both', expand=False, padx=10)

    def build_disciplinas(self):
        self.barra_inferior_3 = tk.Frame(self.parent, bg=style["COLOR_CORPO_PRINCIPAL"])
        self.barra_inferior_3.pack(side=tk.TOP, fill=tk.BOTH, expand=False)

        yscrollbar = tk.Scrollbar(self.barra_inferior_3) 
        yscrollbar.pack(side =tk.RIGHT, fill = tk.X) 
  
        label = tk.Label(self.barra_inferior_3, text="Disciplina: ")
        label.config(fg="#3f3f3f", font=("Montserrat", 15), padx=15, bg=style["COLOR_CORPO_PRINCIPAL"])
        label.pack(side=tk.LEFT, fill='both', expand=False)
        
        self.listbox_disciplinas = tk.Listbox(self.barra_inferior_3, yscrollcommand = yscrollbar.set, bg=style["COLOR_CORPO_PRINCIPAL"], height=3)
        self.listbox_disciplinas.pack(side=tk.LEFT, pady=5, expand = tk.NO, fill = "both") 
        
        service = CadastrarAluno()
        x = service.buscar_disciplinas()
        self.add_items(x, self.listbox_disciplinas)
        
        yscrollbar.config(command = self.listbox_disciplinas.yview)

    def build_alunos(self):
        self.barra_inferior_4 = tk.Frame(self.parent, bg=style["COLOR_CORPO_PRINCIPAL"])
        self.barra_inferior_4.pack(side=tk.TOP, fill=tk.BOTH, expand=False)

        yscrollbar = tk.Scrollbar(self.barra_inferior_4) 
        yscrollbar.pack(side =tk.RIGHT, fill = tk.X) 
  
        label = tk.Label(self.barra_inferior_4, text="Aluno: ")
        label.config(fg="#3f3f3f", font=("Montserrat", 15), padx=15, bg=style["COLOR_CORPO_PRINCIPAL"])
        label.pack(side=tk.LEFT, fill='both', expand=False)
        
        self.listbox_alunos = tk.Listbox(self.barra_inferior_4, yscrollcommand = yscrollbar.set, bg=style["COLOR_CORPO_PRINCIPAL"], height=3, width=80)
        self.listbox_alunos.pack(side=tk.LEFT, pady=20, expand = tk.NO, fill = "both") 
        
        service = CadastrarAluno()
        x = service.buscar_alunos()
        self.add_items(x, self.listbox_alunos)
        
        yscrollbar.config(command = self.listbox_alunos.yview)

    def add_items(self, x, list_box):
        for each_item in range(len(x)): 
            list_box.insert(tk.END, x[each_item])


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
            command=lambda: self.cadastrar_nota()
            )
        self.button.pack(side=tk.RIGHT, fill='both', expand=False, padx=80, pady=30)

    def cadastrar_nota(self):
        sm = [self.entry_sm1.get().replace(',','.'), self.entry_sm2.get().replace(',','.')]
        av = [self.entry_av.get().replace(',','.'), self.entry_avs.get().replace(',','.')]
        aluno = self.listbox_alunos.get(ACTIVE)
        disciplina = self.listbox_disciplinas.get(ACTIVE)
        
        service = CadastroNotas()
        retorno = service.inserir_notas(sm, av, aluno, disciplina)

        if retorno[0] == False:
            messagebox.showerror("Atencao", retorno[1])
        else:
            messagebox.showinfo("Concluido", "Aluno cadastrado com sucesso!!")
            self.entry_sm1.focus()
            self.entry_sm1.delete(0, tk.END)
            self.entry_sm2.delete(0, tk.END)
            self.entry_av.delete(0, tk.END)
            self.entry_avs.delete(0, tk.END)
            
            self.listbox_alunos.delete(0, tk.END)
            self.listbox_disciplinas.delete(0, tk.END)

            service = CadastrarAluno()
            x = service.buscar_alunos()
            self.add_items(x, self.listbox_alunos)
            x2 = service.buscar_disciplinas()
            self.add_items(x2, self.listbox_disciplinas)

    def get_disciplinas(self):
        disciplinas = []
        for index in self.listbox.curselection():
            item = self.listbox.get(index)
            disciplinas.append(item)

        return disciplinas
