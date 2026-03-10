#Revisão Python - Desafio 2
#Funções com multiplos argumentos
def soma(a , b, c):
    return a + b + c
print(soma(1,2,3))

#args(Argumentos infinitos)
def soma_infinita(*args):
    return sum(args)
print(soma_infinita(1,2,3,4,5))

#kwargs(Argumentos nomeados)
def mostra_info(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")
mostra_info(nome="Alice", idade=30, cidade="São Paulo")
#Função Lambda
def dobro(x):
    return x * 2
print(dobro(5))
#Função Lambda simplificada
dobro_lambda = lambda x: x * 2
print(dobro_lambda(5))

#map()
numeros_m = [1,2,3,4,5]
dobros = list(map(lambda x: x * 2, numeros_m))
print(dobros)
#filter()
numeros_f = [1,2,3,4,5]
pares = list(filter(lambda x: x % 2 == 0, numeros_f))
print(pares)
pares = [x*3 for x in range(50) if x % 2 == 0]
print("Lista completa:", pares)
print("Slice:", pares[1:9])
