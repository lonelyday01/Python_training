# Generador

def numeros(num):
    """
    :brief: funcion que retorna una serie de numeros multiplicados por 10
    :param num:
    :return num*10:
    """
    for i in range(1, num+1):
        yield i*10
        if i == 11:
            break

"""lista_numeros = []
for value in numeros(10000):
    lista_numeros.append(value)
    
print(lista_numeros)
    """
#Iterador
class NumerosInterador:
    def  __init__(self, num):
        self.num = num
        self.num_gen = self.numeros_generator()

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.num_gen)

    def numeros_generator(self):
        for i in range(1, self.num+1):
            yield i*10
            if i == 11:
                return


"""iterator = NumerosInterador(15)
listas = []
for value in iterator:
    listas.append(value)

print(listas)"""




# Decorador
def decorador(func):
    def wrapper(*args, **kwargs):
        for value in func(*args, **kwargs):
            yield value * 10
    return wrapper

@decorador
def numero_decorado(num):
    suma = 0
    for i in range(1, num+1):
        suma += i
        yield suma

for value in numero_decorado(5):
    print(value)

