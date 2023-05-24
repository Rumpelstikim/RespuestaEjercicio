# Añadir caracteres a una lista

s1 = 'hola'
s2 = "caho"

my_listA = []
my_listB = []

for c in s1:
    my_listA.append(c)

for c in s2:
    my_listB.append(c)

print(my_listA)
print(my_listB)

# contar caracteres

print(len(s1))
print(len(s2))

# comparar caracteres

for c in s1:
    print(c in s2)


# probando con while

for c in s1:
    if c in s2:
        print(c)

for c in s1:
    contador = c in s2
    
    if contador:
        print(contador)
    else:
        print("Es falso")
  


