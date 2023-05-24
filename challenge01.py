 # Reto 1
 #* ¿ES UN ANAGRAMA?
 #* Fecha publicación enunciado: 03/01/22
 #* Fecha publicación resolución: 10/01/22
 #* Dificultad: MEDIA
 #*
 #* Enunciado: Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Boolean) según sean o no anagramas.
 #* Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
 #* NO hace falta comprobar que ambas palabras existan.
 #* Dos palabras exactamente iguales no son anagrama.
 #*
 #* Información adicional:
 #* - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
 #* - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 #* - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 # * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.

print('Introduce primera palabra')
s1 = input()
#if not s1:    print("no ha introducido nada")

print("Introduce segunda palabra")
s2 = input()
#if not s2:    print("tampoco ha introducido nada")
s1 = s1.lower()
s2 = s2.lower()

a=len(s1)
b=len(s2)
x = a + b
lst = []

if s1.isalpha() and s2.isalpha():
    for c in s1:
        lst.append(c in s2)
    for c in s2:
        lst.append(c in s1)
        i=lst.count(True)
    if s1==s2:
        print("Es la misma palabra;No es un anagrama")
    elif (a!=b):
        print ("Tienen longitud diferente; No es un anagrama")
    elif i == x:
        print("son anagramas")
    else:
        print("no son anagramas")
else:
    print("no debe introducir números")
    


