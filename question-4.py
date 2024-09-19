# Função da letra A soma de dois em dois
def a():
    for x in range(1, 10, 2):
        print(x)

# Função da Letra B multiplica de dois em dois
def b():
    x = 2
    while x < 128:
        x *= 2
        print(x)

# Função da letra C sequencia dos quadrados do numero
def c():
    x = 0
    while x < 8:
        print(x ** 2)
        x += 1

# Função da letra d sequencia dos quadrados, porém de dois em dois
def d():
    x = 2
    while x < 11:
        print(x ** 2)
        x += 2

# Função da letra E o anterior soma com o atual, Fibonacci
def e():
    x = 1
    y = 0
    while x <= 13:
        print(x)
        i = x
        x += y
        y = i

# Função da letra F, não possui uma lógica, apenas após o 16 todos os números ficam consecutivos, logo o proximo número é 20
def f():
    proximo_numero = 20
    sequencia = [2, 10, 12, 16, 17, 18, 19, proximo_numero]
    print(sequencia)

print('======Letra A======')
a()
print('======Letra B======')
b()
print('======Letra C======')
c()
print('======Letra D======')
d()
print('======Letra E======')
e()
print('======Letra F======')
f()