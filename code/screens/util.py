from PIL import ImageTk, Image
import tkinter as tk

def leer_imagen( path, size): 
        return ImageTk.PhotoImage(Image.open(path).resize(size,  Image.ADAPTIVE)) 

def centrar_ventana(ventana,aplicacion_ancho,aplicacion_largo):    
    pantall_ancho = ventana.winfo_screenwidth()
    pantall_largo = ventana.winfo_screenheight()
    x = int((pantall_ancho/2) - (aplicacion_ancho/2))
    y = int((pantall_largo/2) - (aplicacion_largo/2))
    return ventana.geometry(f"{aplicacion_ancho}x{aplicacion_largo}+{x}+{y}")

class Table:
    def __init__(self,root, data):
        total_rows = len(data)
        total_columns = len(data[0])
        columns = ["Aluno", "Disciplina", "SM1", "SM2", "AV", "AVS", "NF", "Aprovado"]

        for i in range(total_columns):
            self.e = tk.Entry(root, width=16, fg="#3f3f3f",
                               font=('Arial',8,'bold'))
                 
            self.e.grid(row=0, column=i)
            self.e.insert(tk.END, columns[i])

        for i in range(total_rows):
            for j in range(total_columns):
                 
                self.e = tk.Entry(root, width=16, fg="#3f3f3f",
                               font=('Arial',8,'bold'))
                 
                self.e.grid(row=i+1, column=j)
                self.e.insert(tk.END, data[i][j])