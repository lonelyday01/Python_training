# Ejercicio 1
frutas = {"manzana": "apple", "naranja": "orange", "platano": "banana", "limon": "lemon"}
print(frutas["naranja"])
frutas["piña"] = "pineapple"
for clave, valor in frutas.items():
    print(clave + " : " + valor)


# Ejercicio 2
nota = 4.5
trabajo_realizado = "no"
nota_final = "aprobado" if nota > 4 and trabajo_realizado == "si" else "reprobado"
print(nota_final)

# Ejercicio 3
inicio = 1
fin = 6
while inicio <= fin:
    print("Esta es la fila {}".format(inicio))
    inicio += 1
