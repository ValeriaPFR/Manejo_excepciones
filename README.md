# Manejo_excepciones
Se solicita colaborar en una aplicación de galería de fotos, para lo cual se tienen las siguientes condiciones: 

1. Que no sea posible modificar el alto o ancho de la foto creada, usar atributo de clase MAX', en la clase 'Foto', para verificar que el rango de la foto
2. solicitan además hacer este control mediante una excepción propia, ya que se desea utilizar la misma excepción en otro sector del programa que recibe los valores de ancho y 
alto, y desea validarlos antes de crear nuevas fotos.
3. En el archivo apoyo_desafio.py se proporciona el código para crear instancias de la 'Foto', se debe agregar l lanzamiento de la excepción en os métodos setter de ancho y alto, según las condiciones indicadas.

- Modularización-
Los requerimientos presentados en el desafío fueron abordados con la implementación de 3 módulos. El módulo foto, contiene atributos encapsulados de ancho y alto, y utiliza excepciones personalizadas para manejar errores cuando se intenta establecer valores fuera del rango permitido. El módulo errores, define una clase de excepción personalizada llamada 'DimensionError' para manejar errores de dimensiones, proporcionando un mensaje de error específico y mostrando la dimensión afectada y su valor máximo permitido en caso de estar fuera del rango. Finalmente se agregó un módulo main, que demuestra el manejo de excepciones, trabajando con los objetos de la clase 'Foto'.






