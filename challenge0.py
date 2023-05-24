 #Fecha publicación enunciado: 27/12/21
 # Fecha publicación resolución: 03/01/22
 # Dificultad: FÁCIL
 # Enunciado: Escribe un programa que muestre por consola (con un print) los números de 1 a 100 (ambos incluidos y con un salto de línea entre cada impresión), sustituyendo los siguientes:
 # - Múltiplos de 3 por la palabra "fizz".
 # - Múltiplos de 5 por la palabra "buzz".

def fizzbuzz():
             
    for num in range(1,101):
         
        if num % 3 == 0 and num % 5 == 0:
            print("fizzbuzz")

        elif num % 5 == 0:
            print("buzz")
    
        elif num % 3 == 0:
            print("fizz")
        else:
            print(num)

fizzbuzz()



