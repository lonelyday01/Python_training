cadena="Esto es un texto de ejemplo"
print(cadena[11:16])

"#########################"

longitud = len(cadena)
strLongitud = str(longitud)
mayusculas = cadena.upper()
resultado = mayusculas + " tiene longitud de " + strLongitud
print(f"{mayusculas}" + ' tiene longitud de ' + f"{strLongitud}")


"#########################"

dato1 = int(input("Introduce el primero numero: "))
dato2 = int(input("Introduce el segundo numero: "))
suma = dato1 + dato2
strSuma = str(suma)
resultado = "La suma es " + strSuma
print(f"{resultado}")


"#########################"

lista =  [1,5,4,6,8,4,6,2,7,5]
lista = list(set(lista))
print(lista)
