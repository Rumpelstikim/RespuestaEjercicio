# Función para calcular la secuencia de Fibonacci
def fibonacci(n):
    fib = [0, 1]  # Inicializamos la lista con los primeros dos números de Fibonacci

    # Generamos la secuencia
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])

    return fib

# Imprimimos los primeros 50 números de Fibonacci
n = 50
fibonacci_sequence = fibonacci(n)
for num in fibonacci_sequence:
    print(num)