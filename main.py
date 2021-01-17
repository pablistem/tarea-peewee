from tkinter import *
from tkinter.messagebox import *
from tkinter import ttk
from temas.opcion_temas import eleccion_tema
from guardar_modal import *
from eliminar_modal import *
from modificar_modal import *
import base_datos
import val

class Noticia:

    def __init__(self, window):
    
        # Ventana principal 
        self.root = window
        self.root.title("Tarea Peewee")

        titulo = Label(self.root, text="Ingrese sus datos", bg="DarkOrchid3", fg="thistle1", height=1, width=60)
        titulo.grid(row=0, column=0, columnspan=4, padx=1, pady=1, sticky=W+E)

        Label(self.root, text="Título").grid(row=1, column=0, sticky=W)
        Label(self.root, text="Descripción").grid(row=2, column=0, sticky=W)       


        # Defino variables para tomar valores de campos de entrada
        self.a_val, self.b_val = StringVar(), StringVar()
        w_ancho = 20


        self.entrada_nombre = Entry(self.root, textvariable = self.a_val, width = w_ancho) 
        self.entrada_nombre.grid(row = 1, column = 1)
        self.entrada_descripcion = Entry(self.root, textvariable = self.b_val, width = w_ancho) 
        self.entrada_descripcion.grid(row = 2, column = 1)


        self.tree = ttk.Treeview(height = 10, columns = 3)
        self.tree["columns"]=("one","two","three","four")
        self.tree.grid(row = 7, column = 0, columnspan = 3)
        self.tree.heading("#0",text="ID",anchor=CENTER)
        self.tree.heading("one", text = 'Título', anchor = CENTER)
        self.tree.heading("two", text = 'Fecha', anchor = CENTER)
        self.tree.heading("three", text = 'Descripción', anchor = CENTER)
        self.tree.heading("four", text = 'Estado', anchor = CENTER)
        #self.tree.heading("five", text = 'Título', anchor = CENTER)
        # Boton Agregar Noticia 
        ttk.Button(self.root, text = 'Mostrar registros existentes',  command = lambda:self.mostrar()).grid( row = 5, columnspan = 3, sticky = W + E)

        Button(self.root, text="Crear bd", command=lambda:base_datos.crearbd()).grid(row=6, column=0)
        Button(self.root, text="Alta", command=lambda:self.alta()).grid(row=6, column=1)

        Button(self.root, text='Guardar', command=lambda:self.pasar_objeto_guardar()).grid(row=11, column=0)
        Button(self.root, text='Eliminar', command=lambda:self.pasar_objeto_eliminar()).grid(row=11, column=1)
        Button(self.root, text='Modificar', command=lambda:self.pasar_objeto_modificar()).grid(row=11, column=2)

        # #####################################################
        # ################ TEMAS #############3#################
        # #####################################################3
        self.temas_opciones = Frame(self.root, bg="red", borderwidth=2, relief=RAISED)
        self.temas_opciones.grid(row=12, column=0, columnspan=4, padx=1, pady=1, sticky=W+E)
 

        ancho_boton = 10
        self.temas = StringVar()
        self.temas.set("tema1")
        # Agrego variables de control para elección de tema
        self.tema_option = IntVar(value=0)

        Label(self.temas_opciones, borderwidth=4, relief=RAISED, text="Temas", bg="#222", fg="OrangeRed").pack(fill=X)
        temas = ["tema1", "tema2", "tema3"]
        for opcion in temas:
            boton = Radiobutton(self.temas_opciones,
            text=str(opcion), indicatoron=1, value=int(opcion[-1])-1, variable =self.tema_option,
            bg="#222",fg="OrangeRed", command=self.bg_fg_option)
            boton["width"] = ancho_boton
            boton.pack(side=TOP)
        
    def bg_fg_option(self):
        print(self.tema_option.get())
        print(eleccion_tema(self.tema_option.get()))
        #print(OpcionTemas.EleccionTema(self.tema_option.get()))
        self.temas_opciones["bg"] = eleccion_tema(self.tema_option.get())
        self.root["bg"] = eleccion_tema(self.tema_option.get())

 
    # #####################################################
    # ################ FIN DE TEMAS #######################
    # #####################################################

    def pasar_objeto_guardar(self,):
        print(self)
        guardar(self)

    def pasar_objeto_eliminar(self,):
        print(self)
        eliminar(self)

    def pasar_objeto_modificar(self,):
        print(self)
        modificar(self)

    # obteniendo las noticias
    def mostrar(self,):
        # limpieza de tabla 
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        # Consiguiendo datos
        sql = 'SELECT * FROM noticia ORDER BY id ASC'

        mibase = base_datos.miconexion()
        print(base_datos.miconexion())
        print(mibase)
        micursor = mibase.cursor()
        
        micursor.execute(sql)
        resultado = micursor.fetchall()

        for fila in resultado:
            print(fila)
            self.tree.insert('', 0, text = fila[0], values = (fila[1],fila[2]))


    def alta(self,):
        print("Nueva alta de datos")

        cadena=self.a_val.get() # obtenemos la cadena del campo de texto
        if(val.validar(cadena)==True):
            print("validado") 
            mibase = base_datos.miconexion()
            print(mibase)
            micursor = mibase.cursor()
            sql = "INSERT INTO noticia (titulo, descripcion) VALUES (%s, %s)"
            datos = (self.a_val.get(), self.b_val.get())
            micursor.execute(sql, datos)
            mibase.commit()
            showinfo('Validado', 'El registro se ha agregado correctamente')
        else:
            showinfo('No Validado', 'El campo de título no cumple los requisitos, ingrese datos alfabéticos')  
        self.mostrar()




if __name__ == '__main__':
    window = Tk()
    application = Noticia(window)
    application.mostrar()
    window.mainloop()
