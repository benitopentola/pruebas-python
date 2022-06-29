#PRUEBAS APRENDIZAJE PYTHON.

ass = divmod(88, 99)
print(ass)


print('PRUEBA ENUMERATE')

animales = ['nutria', 'gato', 'perro']

enumerate_prime = enumerate(animales)

print(list(enumerate_prime))

print('cxxxx')

###pruebas generadores 1
def generaPares(limite):
    num=1
    while num<limite:
        yield num*2
        num=num+1
devuelvePares=generaPares(10)

print(next(devuelvePares))

print("CODIGO FALSO")

print(next(devuelvePares))

print("CODIGO FALSO")

print(next(devuelvePares))