nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))

estudando = input("Você está estudando IA? (sim/não): ").lower() == "sim"

print(f"Nome: {nome}, Idade: {idade}, Altura: {altura}, Estudando IA: {estudando}")

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")

contador = 0
while contador < 18:
    print(contador)
    contador += 1

numeros = [1,2,3,4]
numeros.append(5)

for numero in numeros:
    print(numero)

pessoa = {
    "nome": nome,
    "idade": idade
}

print(pessoa["nome"])

def saudacao(nome):
    return f"Olá, {nome}!"

print(saudacao(nome))

numeros = [x*3 for x in range(5)]
print(numeros[1:6])