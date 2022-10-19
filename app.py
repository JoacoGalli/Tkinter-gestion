from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
from form_login import FormLoginDesigner
from PostgreDB import PostgreDB

class Proveedores:
    def __init__(self, window):
        # Inicializo variables
        self.wind = window
        self.wind.title('Aplicacion de proveedores')

        self.wind.geometry("500x333")
        # agrego imagen
        image = Image.open("campo.jpeg")
        photo = ImageTk.PhotoImage(image)
        pic_label = Label(image=photo)
        pic_label.grid()

        #creo un contenedor de proveedor
        frame = LabelFrame(self.wind, text = 'Registre nuevo proveedor')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)
        
        #Ingreso del nombre del proveedor
        Label(frame, text = 'Nombre: ').grid(row = 1, column = 0)
        self.name = Entry(frame)
        self.name.focus()
        self.name.grid(row = 1, column = 1)

        #ingreso valor de factura
        Label(frame, text = 'Valor: ').grid(row = 2, column = 0)
        self.value = Entry(frame)
        self.value.grid(row = 2, column = 1)

        # boton agregar proveedor
        ttk.Button(frame, text = 'Guardar proveedor', command = self.add_proveedor).grid(row = 3, columnspan = 2, sticky = W + E)

    def add_proveedor(self):
        pass

if __name__ == '__main__':
    cursor = PostgreDB()
    #window = Tk()
    applicacion = FormLoginDesigner(cursor)
    #window.mainloop()
