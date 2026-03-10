#Revisão Python - Desafio 1
#Comando de Entrada
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
#Comando de Entrada Binário
estudando = input("Você está estudando IA? (sim/não): ").lower() == "sim"
#Comando de Saída
print(f"Nome: {nome}, Idade: {idade}, Altura: {altura}, Estudando IA: {estudando}")
#Comando de Decisão
if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")
#Comando de Repetição
contador = 0
while contador < 18:
    print(contador)
    contador += 1
#Comando de Listas
numeros = [1,2,3,4]
numeros.append(5)
#Iteração
for numero in numeros:
    print(numero)
#Comando de Dicionário
pessoa = {
    "nome": nome,
    "idade": idade
}
#Acessando valor do dicionário
print(pessoa["nome"])
#Função
def saudacao(nome):
    return f"Olá, {nome}!"
#Chamando a função
print(saudacao(nome))
#Comando de Fatiamento
numeros = [x*3 for x in range(5)]
print(numeros[1:6])