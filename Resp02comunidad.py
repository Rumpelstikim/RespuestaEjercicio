def fibonacci():
    n1 = 0
    n2 = 1
    for idx in range(1, 51): # “idx” simply means “index”, the position of the element you are currently accessing. 
        print(n1)
        fib = n1 + n2
        n1 = n2
        n2 = fib
fibonacci()

