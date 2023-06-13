# Listas
lista = [1, 2, 5, 25, 33, 56, 75, 21, 56, 89, 43, 13, 62, 24]
numero = 21
print("si" if numero in lista else "no")


# Tuplas
tupla = ("Antonio, Pedro, Maria")
print(tupla)
dato = input("ingresa un dato: ")
print("si" if dato in tupla else "no")

# Conjuntos /sets
conjunto = {1, 2, 3, 4, 5}
print(conjunto)
for i in range(4,10):
    conjunto.add(i)
print(conjunto)
conjunto.remove(9)
print(conjunto)
print(type(conjunto))


# Diccionarios
diccionario = {"uno": "one", "dos": "two", "tres": "three"}
print(diccionario)
diccionario["cuatro"] = "four"
print(diccionario)
dato = input("Ingresa un dato: ")
print(diccionario[dato] if dato in diccionario else "No existe")