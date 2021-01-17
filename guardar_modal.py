from tkinter import *
from guardar import *
from base_datos import *

def show(variables, popupGuardar):
    popupGuardar.destroy()
    imprimir(variables)

def guarda(variables, popupGuardar, elobjeto):

    popupGuardar.destroy()
    lista = []
    for variable in variables:
        lista.append(variable.get())
    noticia = Noticia()
    noticia.titulo = lista[0]
    noticia.descripcion = lista[1]
    noticia.save()
    elobjeto.mostrar()

def guardar(objeto):
    print("------- ver objeto -----------")
    print(objeto)
    print("------- visto objeto -----------")
    popupGuardar = Toplevel()
    vars_guardar = CrearFormGuardar(popupGuardar, campos)
    
    Button(popupGuardar, text='OK', command=lambda: show(vars_guardar, popupGuardar)).pack()
    Button(popupGuardar, text='guardar', command=lambda: guarda(vars_guardar, popupGuardar, objeto)).pack()

    popupGuardar.grab_set()
    popupGuardar.focus_set()
    popupGuardar.wait_window()
