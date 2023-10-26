import tkinter

class Ventana(): #centra todas las pantallas en la interfaz
    def __init__(self, ancho, alto, titulo):
        self.ventana = tkinter.Tk()
        self.ventana.title(titulo)
        # Obtén el ancho y alto de la pantalla
        ancho_pantalla = self.ventana.winfo_screenwidth()
        alto_pantalla = self.ventana.winfo_screenheight()

        x = (ancho_pantalla - ancho) // 2  # 400 es el ancho de la ventana
        y = (alto_pantalla - alto) // 2   # 300 es el alto de la ventana
        self.ventana.geometry(f"{ancho}x{alto}+{x}+{y}")