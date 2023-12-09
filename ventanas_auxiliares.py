import tkinter

class Ventana():
    """
    Clase base para crear ventanas en la interfaz gráfica.

    Attributes:
        ventana (tkinter.Tk): Objeto Tkinter para la ventana.
    """
    def __init__(self, ancho, alto, titulo):
        """
        Inicializa la ventana con el ancho, alto y título dados.

        Args:
            ancho (int): Ancho de la ventana.
            alto (int): Alto de la ventana.
            titulo (str): Título de la ventana.
        """
        self.ventana = tkinter.Tk()
        self.ventana.title(titulo)
        # Obtén el ancho y alto de la pantalla
        ancho_pantalla = self.ventana.winfo_screenwidth()
        alto_pantalla = self.ventana.winfo_screenheight()

        x = (ancho_pantalla - ancho) // 2
        y = (alto_pantalla - alto) // 2
        self.ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

class Ventana_Error(Ventana):
    """
    Clase que representa la ventana de error.

    Attributes:
        confirmacion (bool): Variable booleana que indica si se confirma la salida de la aplicación.
    """
    def __init__(self, texto):
        """
        Inicializa la ventana de error con un mensaje específico.

        Args:
            texto (str): Mensaje de error.
        """
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
    """
    Clase que representa la ventana de éxito al guardar.

    Attributes:
        confirmacion (bool): Variable booleana que indica si se confirma la salida de la aplicación.
    """
    def __init__(self):
        """
        Inicializa la ventana de guardado con un mensaje específico.
        """
        super().__init__(350, 200, "Guardado")

        mensaje = tkinter.Label(self.ventana, text="Se guardaron las variables\ncon éxito.",
                                    font="ComicSans 15", width=30, height=7)
        mensaje.pack()
        seguir = tkinter.Button(self.ventana, text="Seguir", 
                                command=lambda: self.ventana.destroy(), bg="light grey")
        seguir.pack()

        self.ventana.mainloop()

class Ventana_Conf(Ventana):
    """
    Clase que representa la ventana de confirmación.

    Attributes:
        confirmacion (bool): Variable booleana que indica si se confirma la salida de la aplicación.
    """
    def __init__(self):
        """
        Inicializa la ventana de confirmación con opciones "Sí" y "No".
        """
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
        seguir.pack(side="left", padx=10)
        
        # Botón "No" en el frame
        no_seguir = tkinter.Button(frame_botones, text="No", 
                                   command=lambda: self.__seguir(), 
                                   bg="light grey", width=10, height=3)
        no_seguir.pack(side="right", padx=10)

        self.ventana.mainloop()
    
    def __seguir(self):
        """
        Establece la confirmación como False.
        """
        self.confirmacion = False
        self.ventana.destroy()
        
    def get_confirmacion(self):
        """
        Obtiene el estado de confirmación.

        Returns:
            bool: Estado de confirmación.
        """
        return self.confirmacion

if __name__ == "__main__":
    pass