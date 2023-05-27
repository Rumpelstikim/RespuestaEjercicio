#* Reto #3
# * ¿ES UN NÚMERO PRIMO?
# * Fecha publicación enunciado: 17/01/22
# * Fecha publicación resolución: 24/01/22
# * Dificultad: MEDIA
# *
# * Enunciado: Escribe un programa que se encargue de comprobar si un número es o no primo.
# * Hecho esto, imprime los números primos entre 1 y 100.
# *
# * Información adicional:
# * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
# * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
# * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
# * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.

def num_primo():
    primo = True
    lst = [2,3,5,7]
    for n in range (2,100):
        if n%2 ==0 or n%3 == 0 or n%5 == 0 or n%7== 0:
            primo = False 
            #determina los primos
        else:
            lst.append(n)
    for element in lst:
        print(element)
num_primo()