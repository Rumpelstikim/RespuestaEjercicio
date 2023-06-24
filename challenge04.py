 #* Enunciado: Crea UNA ÚNICA FUNCIÓN (importante que sólo sea una) que sea capaz de calcular y retornar el área de un polígono.
 #* - La función recibirá por parámetro sólo UN polígono a la vez.
 #* - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 #* - Imprime el cálculo del área de un polígono de cada tipo.

def area_poligon():
    while True:
        try:
            poligon = input("Para calcular el área de su polígono, pulse: 1 para triángulo; 2 para rectángulo, 3 para cuadrado: ")
            if poligon not in ["1", "2", "3"]:
                raise ValueError("Opción inválida. Por favor, ingrese una opción válida.")
            break
        except ValueError as e:
            print(e)

    if poligon == "1":
        a = float(input("¿Cuál es la altura del triángulo? "))
        b = float(input("¿Cuánto mide la base del triángulo? "))            
                
        print(f"El área del triángulo es: {b * a / 2}")

    elif poligon == "2":
        a = float(input("¿Cuánto mide un lado del rectángulo? "))
        b = float(input("¿Cuánto mide el otro lado del rectángulo? "))
                
        print(f"El área del rectángulo es: {b * a}")

    elif poligon == "3":
        a = float(input("¿Cuánto miden los lados del cuadrado? "))
                
        print(f"El área del cuadrado es: {a ** 2}")

area_poligon()