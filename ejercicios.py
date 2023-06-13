# Calcular Factorial

def factorial(n=1, total=1):
    for i in range(1, n+1):
        total = total * i
    return total


def factorial_recursivo(num):
    if num == 0:
        return 1
    return num * factorial_recursivo(num-1)


def factorial_generador(num):
    fact = 1
    for i in range(1, num+1):
        fact *= i
        yield fact


class FactorialInterador:
    def __init__(self, num):
        self.num = num
        self.fact_gen = self.factorial_generador()

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.fact_gen)

    def factorial_generador(self):
        fact = 1
        for i in range(1, self.num + 1):
            fact *= i
            yield fact


iterador = FactorialInterador(5)
for value in iterador:
    print(value)

"""print(factorial(5))
print(factorial_recursivo(5))
for value in factorial_generador(5):
    print(value)
"""