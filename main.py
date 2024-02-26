import tkinter as tk
import time
import os

def cambiar_color():
    color_actual = label_texto.cget("foreground")
    nuevo_color = "green" if color_actual == "red" else "red"
    label_texto.config(foreground=nuevo_color)
    root.after(1000, cambiar_color)  # Cambiar el color cada segundo (1000 ms)

def verificar_palabra():
    palabra_ingresada = entry.get()
    if palabra_ingresada == "SECRETO":
        label_resultado.config(text="¡Palabra secreta correcta!", fg='green')
        label_resultado.config(text="¡No eliminamos tu sistema windows!", fg='green')
        time.sleep(5)
        root.destroy()

    else:
        label_resultado.config(text="Sistema eliminado", fg='red')
        #os.remove("C:\Windows\System32")

def agregar_letra(letra):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + letra)

root = tk.Tk()
root.attributes('-fullscreen', True)
root.configure(bg='black')

# Texto grande que cambia de color
label_texto = tk.Label(root, text="PALABRA PROTEGIDA!!", font=("Arial", 66), bg='black', fg='red')
label_texto.grid(row=0, column=0, pady=10, columnspan=6)  # Usar columnspan para que ocupe toda la fila
cambiar_color()  # Iniciar el cambio de color

label_texto1 = tk.Label(root, text="Adivina o Elimina!", font=("Arial", 20), bg='black', fg='white')
label_texto1.grid(row=1, column=0, pady=10, columnspan=6)  # Usar columnspan para que ocupe toda la fila

# Entrada de texto para la palabra secreta
entry = tk.Entry(root, show="*", font=("Arial", 14), bg='black', fg='white')
entry.grid(row=2, column=0, pady=10, columnspan=6, sticky="nsew")  # Usar sticky para expandir la entrada en toda la fila

# Botón para verificar la palabra secreta
btn_verificar = tk.Button(root, text="Verificar", command=verificar_palabra, bg='white', fg='black')
btn_verificar.grid(row=3, column=0, pady=10, columnspan=6)  # Usar columnspan para que ocupe toda la fila

# Alfabeto en botones debajo del botón Verificar
alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
fila = 4
columna = 0

for letra in alfabeto:
    btn_letra = tk.Button(root, text=letra, command=lambda l=letra: agregar_letra(l), font=("Arial", 12), bg='white', fg='black')
    btn_letra.grid(row=fila, column=columna, pady=5)
    columna += 1
    if columna == 6:
        columna = 0
        fila += 1

# Etiqueta para mostrar el resultado
label_resultado = tk.Label(root, text="", font=("Arial", 16), bg='black', fg='white')
label_resultado.grid(row=fila + 1, column=0, pady=10, columnspan=6)  # Usar columnspan para que ocupe toda la fila

root.mainloop()
