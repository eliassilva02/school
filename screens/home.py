import tkinter as tk
from tkinter import font
from screens.config import style
import screens.util as util
from screens.frm_alunos import FrmAlunos
from screens.frm_disciplinas import FrmDisciplina

class FrmMenu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.logo = util.leer_imagen("screens/imagens/logo.png", (560, 136))
        self.perfil = util.leer_imagen("screens/imagens/Perfil.png", (100, 100))
        self.img = util.leer_imagen("screens/imagens/sitio_construccion.png", (200, 200))
        self.config_window()
        self.paineis()
        self.controles_barra_superior()        
        self.controles_menu_lateral()
        self.controls_body()
    
    def config_window(self):
        self.title('Easy School')
        self.geometry("1280x720+510+70")
        self.iconbitmap("screens/imagens/logo.ico")
        w, h = 1024, 600        
        util.centrar_ventana(self, w, h)        

    def paineis(self):        
        self.barra_superior = tk.Frame(self, bg=style["COLOR_BARRA_SUPERIOR"], height=50)
        self.barra_superior.pack(side=tk.TOP, fill='both')      

        self.menu_lateral = tk.Frame(self, bg=style["COLOR_MENU_LATERAL"], width=120)
        self.menu_lateral.pack(side=tk.LEFT, fill='both', expand=False) 
        
        self.body = tk.Frame(self, bg=style["COLOR_CORPO_PRINCIPAL"])
        self.body.pack(side=tk.RIGHT, fill='both', expand=True)

    
    def controles_barra_superior(self):
        font_awesome = font.Font(family='FontAwesome', size=12)

        self.labelTitulo = tk.Label(self.barra_superior, text="Autodidacta")
        self.labelTitulo.config(fg="#fff", font=("Roboto", 15), bg=style["COLOR_BARRA_SUPERIOR"], pady=10, width=16)
        self.labelTitulo.pack(side=tk.LEFT)

        self.buttonMenuLateral = tk.Button(self.barra_superior, text="\uf0c9", font=font_awesome, command=self.toggle_painel, bd=0, bg=style["COLOR_BARRA_SUPERIOR"], fg="white")
        self.buttonMenuLateral.pack(side=tk.LEFT)

        self.labelTitulo = tk.Label(self.barra_superior, text="servicio@autodidacta.mx")
        self.labelTitulo.config(fg="#fff", font=("Roboto", 10), bg=style["COLOR_BARRA_SUPERIOR"], padx=10, width=20)
        self.labelTitulo.pack(side=tk.RIGHT)
    
    def controles_menu_lateral(self):
        ancho_menu = 20
        alto_menu = 2
        font_awesome = font.Font(family='FontAwesome', size=15)

        self.buttonAlunos = tk.Button(self.menu_lateral)        
        self.buttonDisciplinas = tk.Button(self.menu_lateral)        
        self.buttonBoletim = tk.Button(self.menu_lateral)
        self.buttonProvas = tk.Button(self.menu_lateral)        
        self.buttonSettings = tk.Button(self.menu_lateral)

        buttons_info = [
            ("Alunos", "\uf109", self.buttonAlunos,self.abrir_cad_alunos),
            ("Disciplinas", "\uf129", self.buttonBoletim,self.abrir_cad_disciplina),
            ("Boletim", "\uf007", self.buttonDisciplinas,self.abrir_painel_en_construccion),
            ("Provas", "\uf03e", self.buttonProvas,self.abrir_painel_en_construccion),    
        ]

        for text, icon, button, comando in buttons_info:
            self.config_button_menu(button, text, icon, font_awesome, ancho_menu, alto_menu,comando)                    
    
    def controls_body(self):
        label = tk.Label(self.body, image=self.logo,bg=style["COLOR_CORPO_PRINCIPAL"])
        label.place(x=0, y=0, relwidth=1, relheight=1)        
  
    def config_button_menu(self, button, text, icon, font_awesome, ancho_menu, alto_menu, comando):
        button.config(text=f"  {icon}    {text}", anchor="w", font=font_awesome,
                      bd=0, bg=style["COLOR_MENU_LATERAL"], fg="white", width=ancho_menu, height=alto_menu, 
                      command = comando)
        button.pack(side=tk.TOP)
        self.bind_hover_events(button)

    def bind_hover_events(self, button):
        button.bind("<Enter>", lambda event: self.on_enter(event, button))
        button.bind("<Leave>", lambda event: self.on_leave(event, button))

    def on_enter(self, event, button):
        button.config(bg=style["COLOR_BUTTON"], fg='white')

    def on_leave(self, event, button):
        button.config(bg=style["COLOR_MENU_LATERAL"], fg='white')

    def toggle_painel(self):
        if self.menu_lateral.winfo_ismapped():
            self.menu_lateral.pack_forget()
        else:
            self.menu_lateral.pack(side=tk.LEFT, fill='y')

    def abrir_cad_alunos(self):   
        self.limpar_painel(self.body)     
        alunos = FrmAlunos(self.body)
        alunos.pack()

    def abrir_cad_disciplina(self):
        self.limpar_painel(self.body)
        disciplina = FrmDisciplina(self.body)
        disciplina.pack()
    
    def abrir_painel_info(self):           
        print('chama')

    def abrir_painel_en_construccion(self):
        print('array')

    def limpar_painel(self,painel):
        for widget in painel.winfo_children():
            widget.destroy()