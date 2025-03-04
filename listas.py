#1. Manipulação de Listas

"""
Escreva um código em Python que:
Peça ao usuário para digitar cinco números inteiros.
Armazene esses números em uma lista.
Exiba o maior e o menor número da lista.
Exemplo:
Entrada: 10, 5, 8, 2, 7
Saída: Maior número: 10, Menor número: 2
"""

#Resposta

n1 = int(input("Digite 5 números, tecle ENTER a cada número inserido: "))  #Define um inpute e informa que vai ser inteiro
n2 = int(input("Mais um número por gentileza: "))
n3 = int(input("Estamos quase lá, digite mais um número: "))
n4 = int(input("Outro: "))
n5 = int(input("Amém, último número: "))

numeros = [n1, n2, n3, n4, n5] #Armazena numa lista

print("menor nmr dos 3: ", min(n1, n2, n3, n4, n5)) #Imprime o menor e maior
print("maior nmr dos 3: ", max(n1, n2, n3, n4, n5))




#Opção mais completa
entrada = input("Digite 5 números separados por espaço: ")# Solicita os números ao usuário e os separa corretamente

# Converte a entrada em uma lista de inteiros
numeros = list(map(int, entrada.split()))

# Encontra o menor e o maior número na lista
menor = min(numeros)
maior = max(numeros)

# Exibe os resultados
print("Menor número:", menor)
print("Maior número:", maior)
