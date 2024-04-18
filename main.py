from Manejo_excepciones.foto import Foto

def main():
    """
    Funcion principal para demostrar el manejo de excepciones al trabajar con objetos de la clase 'Foto'.
    """
    try:
        # Crear una nueva foto con dimensiones validas
        foto_valida = Foto(800, 600, "foto1.jpg")
        print("Foto creada con éxito.")

        # Intentar modificar el ancho de la foto a un valor invalido
        print("Las dimensiones de la foto no son válidas")
        # Esto deberia lanzar una excepcion si el nuevo ancho es invalido
        foto_valida.ancho = 3000  
        print("Ancho modificado con éxito.")

    # Capturar excepcion especifica para manejar errores de dimensiones invalidas
    #la instancia de excepcion 'ValueError', se contienen en la variable 've'
    except ValueError as ve:
        print("Error al modificar las dimensiones de la foto:", ve)
    # Capturar excepcion generica para manejar otros errores en 'e'
    except Exception as e:
        print("Error general:", e)

if __name__ == "__main__":
    main()
