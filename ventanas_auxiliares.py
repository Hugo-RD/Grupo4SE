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

class Ventana_Error(Ventana):
    def __init__(self, texto):
        super().__init__(350, 260, "Error")

        self.ventana.config(bg="#FF073D")
        mensaje_error = tkinter.Label(self.ventana, text=f"\n¡Se produjo un error!\n\n{texto}",
                                    font="ComicSans 20", width=30, 
                                    height=7, bg="#FF073D")
        mensaje_error.pack()
        seguir = tkinter.Button(self.ventana, text="Seguir", command=lambda: self.ventana.destroy(), bg="light grey")
        seguir.pack()
        self.ventana.mainloop()

class Ventana_Guardado(Ventana):
    def __init__(self):
        super().__init__(350, 200, "Guardado")

        mensaje = tkinter.Label(self.ventana, text="Se guardaron las variables\ncon éxito.",
                                    font="ComicSans 15", width=30, height=7)
        mensaje.pack()
        seguir = tkinter.Button(self.ventana, text="Seguir", 
                                command=lambda: self.ventana.destroy(), bg="light grey")
        seguir.pack()

        self.ventana.mainloop()

class Ventana_Conf(Ventana):#ventana de confirmación salida de la app
    def __init__(self):
        super().__init__(350, 260, "Salida de app")
        self.confirmacion = True
        
        mensaje_error = tkinter.Label(self.ventana, text="\n¿Quiere salir de la aplicación?\n\n",
                                 font="ComicSans 15", width=30, height=7)
        mensaje_error.pack()
        
        # Crear un Frame para contener los botones
        frame_botones = tkinter.Frame(self.ventana)
        frame_botones.pack()
        
        # Botón "Sí" en el frame
        seguir = tkinter.Button(frame_botones, text="Sí", 
                                command=lambda: self.ventana.destroy(),
                                bg="light grey", width=10, height=3)
        seguir.pack(side="left", padx=10)  # O utiliza anchor="w" para alineación occidental
        
        # Botón "No" en el frame
        no_seguir = tkinter.Button(frame_botones, text="No", 
                                   command=lambda: self.__seguir(), 
                                   bg="light grey", width=10, height=3)
        no_seguir.pack(side="right", padx=10)  # O utiliza anchor="e" para alineación oriental

        self.ventana.mainloop()
    
    def __seguir(self):
        self.confirmacion = False
        self.ventana.destroy()
        
    def get_confirmacion(self):
        return self.confirmacion


if __name__ == "__main__":
    pass