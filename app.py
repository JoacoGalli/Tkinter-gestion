from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk

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

        #ingreso precio
        Label(frame, text = 'Precio: ').grid(row = 2, column = 0)
        self.price = Entry(frame)
        self.price.grid(row = 2, column = 1)

        # boton agregar proveedor
        ttk.Button(frame, text = 'Guardar proveedor', command = self.add_proveedor).grid(row = 3, columnspan = 2, sticky = W + E)

    def add_proveedor(self):
        pass

if __name__ == '__main__':
    window = Tk()
    applicacion = Proveedores(window)
    window.mainloop()
