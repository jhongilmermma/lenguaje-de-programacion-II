import tkinter as tk
from tkinter import messagebox

class Persona:
    def __init__(self, nombre, dia, mes):
        self.nombre = nombre
        self.dia = dia
        self.mes = mes

    def signo_zodiacal(self):
        if (self.mes == 3 and self.dia >= 21) or (self.mes == 4 and self.dia <= 19):
            return "Aries"
        elif (self.mes == 4 and self.dia >= 20) or (self.mes == 5 and self.dia <= 20):
            return "Tauro"
        elif (self.mes == 5 and self.dia >= 21) or (self.mes == 6 and self.dia <= 20):
            return "Géminis"
        elif (self.mes == 6 and self.dia >= 21) or (self.mes == 7 and self.dia <= 22):
            return "Cáncer"
        elif (self.mes == 7 and self.dia >= 23) or (self.mes == 8 and self.dia <= 22):
            return "Leo"
        elif (self.mes == 8 and self.dia >= 23) or (self.mes == 9 and self.dia <= 22):
            return "Virgo"
        elif (self.mes == 9 and self.dia >= 23) or (self.mes == 10 and self.dia <= 22):
            return "Libra"
        elif (self.mes == 10 and self.dia >= 23) or (self.mes == 11 and self.dia <= 21):
            return "Escorpio"
        elif (self.mes == 11 and self.dia >= 22) or (self.mes == 12 and self.dia <= 21):
            return "Sagitario"
        elif (self.mes == 12 and self.dia >= 22) or (self.mes == 1 and self.dia <= 19):
            return "Capricornio"
        elif (self.mes == 1 and self.dia >= 20) or (self.mes == 2 and self.dia <= 18):
            return "Acuario"
        elif (self.mes == 2 and self.dia >= 19) or (self.mes == 3 and self.dia <= 20):
            return "Piscis"
        else:
            return "Fecha no válida"

def calcular_signo():
    try:
        nombre = entry_nombre.get()
        dia = int(entry_dia.get())
        mes = int(entry_mes.get())
        persona = Persona(nombre, dia, mes)
        signo = persona.signo_zodiacal()
        messagebox.showinfo("Resultado", f"{persona.nombre}, tu signo zodiacal es: {signo}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa valores válidos.")

ventana = tk.Tk()
ventana.title("Calculadora de Signo Zodiacal")

tk.Label(ventana, text="Nombre:").grid(row=0, column=0, padx=5, pady=5)
entry_nombre = tk.Entry(ventana)
entry_nombre.grid(row=0, column=1, padx=5, pady=5)

tk.Label(ventana, text="Día de nacimiento:").grid(row=1, column=0, padx=5, pady=5)
entry_dia = tk.Entry(ventana)
entry_dia.grid(row=1, column=1, padx=5, pady=5)

tk.Label(ventana, text="Mes de nacimiento (número):").grid(row=2, column=0, padx=5, pady=5)
entry_mes = tk.Entry(ventana)
entry_mes.grid(row=2, column=1, padx=5, pady=5)

btn_calcular = tk.Button(ventana, text="Calcular signo", command=calcular_signo)
btn_calcular.grid(row=3, column=0, columnspan=2, pady=10)

ventana.mainloop()

