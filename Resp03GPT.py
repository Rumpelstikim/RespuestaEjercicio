def es_primo(numero):
    """
    Verifica si un número dado es primo.
    """
    if numero < 2:
        return False
    print(numero**0.5)
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False

    return True

# Imprimir los números primos entre 1 y 100
print("Números primos entre 1 y 100:")
for num in range(1, 101):
    if es_primo(num):
        print(num)
