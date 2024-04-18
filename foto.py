from Manejo_excepciones.error import DimensionError

class Foto:
    MAX_DIMENSION = 2500  # Define la dimensión máxima permitida para la foto

    def __init__(self, ancho: int, alto: int, ruta: str) -> None:
        """
        Constructor de la clase 'Foto'.

        Args:
            ancho (int): El ancho de la foto.
            alto (int): El alto de la foto.
            ruta (str): La ruta de la foto en el sistema de archivos.
        """
        self.__ancho = ancho  # Inicializa el ancho de la foto
        self.__alto = alto  # Inicializa el alto de la foto
        self.ruta = ruta  # Inicializa la ruta de la foto

    @property
    def ancho(self) -> int:
        """
        Getter para obtener el ancho de la foto.

        Returns:
            int: El ancho de la foto.
        """
        return self.__ancho

    @ancho.setter
    def ancho(self, ancho: int) -> None:
        """
        Setter para establecer el ancho de la foto.

        Args:
            ancho (int): El nuevo ancho de la foto.

        Raises:
            DimensionError: Si el ancho está fuera del rango permitido.
        """
        #la seccion raises indica que la función puede lanzzar una excepcion, en este caso es 'DimensionError' con el valor ingresado de ancho.
        if not 1 <= ancho <= Foto.MAX_DIMENSION:
            raise DimensionError(f"El ancho debe estar entre 1 y {Foto.MAX_DIMENSION}.", "ancho", Foto.MAX_DIMENSION)
        self.__ancho = ancho  # Actualiza el ancho de la foto

    @property
    def alto(self) -> int:
        """
        Getter para obtener el alto de la foto.

        Returns:
            int: El alto de la foto.
        """
        return self.__alto

    @alto.setter
    def alto(self, alto: int) -> None:
        """
        Setter para establecer el alto de la foto.

        Args:
            alto (int): El nuevo alto de la foto.

        Raises:
            DimensionError: Si el alto está fuera del rango permitido.
        """
        #la seccion raises indica que la función puede lanzar una excepcion, en este caso es 'DimensionError' con el valor ingresado de alto.
        if not 1 <= alto <= Foto.MAX_DIMENSION:
            raise DimensionError(f"El alto debe estar entre 1 y {Foto.MAX_DIMENSION}.", "alto", Foto.MAX_DIMENSION)
        self.__alto = alto  # Actualiza el alto de la foto
