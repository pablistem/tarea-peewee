from peewee import *
import datetime
from tkinter.messagebox import *

def crearbd():
    try:
        db = SqliteDatabase('nivel_avanzado.db')

        class BaseModel(Model):
            class Meta:
                database = db

        class Noticia(BaseModel):
            titulo = CharField(unique = True)
            descripcion = TextField()
            fecha = DateTimeField(default=datetime.datetime.now)
            estado_de_publicacion = BooleanField(default=True)
        db.connect()
        db.create_tables([Noticia])
        showinfo('-', 'Base de datos con tabla creada')

    except:
        print("mmmm")
        showinfo('-', 'Ya existe la base de datos')

def miconexion():
        
    #mibase = mysql.connector.connect(host="localhost", user="root", passwd="", database="baseprueba3")
    db = SqliteDatabase('nivel_avanzado.db')
    #print(db)
    mibase = db
    #print(mibase)
    return mibase