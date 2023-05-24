
s1 = input("Introduce primera palabra:")
s2 = input("Introduce segunda palabra:")


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