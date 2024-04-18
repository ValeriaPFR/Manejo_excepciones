class DimensionError(Exception):
    """
    Clase de excepcion para manejar errores relacionados con dimensiones.
    """

    def __init__(self, mensaje, dimension=None, maximo=None):
        """
        Constructor de la clase 'DimensionError'.

        Args:
            mensaje (str): Mensaje de error que describe la naturaleza del problema.
            dimension (int, opcional): La dimension que causo el error.
            maximo (int, opcional): El valor maximo permitido para la dimension.
        """
        super().__init__(mensaje)  # Llama al constructor de la clase base 'Exception'
        self.dimension = dimension  # Almacena la dimension que causo el error
        self.maximo = maximo  # Almacena el valor maximo permitido para la dimension

    def __str__(self):
        """
        Devuelve una representacion de cadena de la excepcion.

        Returns:
            str: La representacion de cadena del error.
        """
        if self.dimension is not None and self.maximo is not None: #condiciones 'if'
            # Si se proporciona la dimension y el maximo, devuelve un mensaje personalizado
            return f"Error: {self.dimension} debe estar entre 1 y {self.maximo}"
        else:
            # Si no, devuelve la representacion de cadena predeterminada de la clase base 'Exception'
            return super().__str__()
