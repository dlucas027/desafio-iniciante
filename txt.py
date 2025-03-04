#2. Leitura de Arquivo TXT

"""
Crie um arquivo chamado nomes.txt com os seguintes nomes:
Ana
Bruno
Carlos
Daniela
Eduardo

Agora, escreva um código Python que:

- Leia o conteúdo do arquivo.
- Exiba os nomes na tela, um por linha.
"""

#Resposta

nomes = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo"]
#comando open permite ler e escrever um arquivo, dependendo de como foi aberto
with open('nomes.txt','w') as arquivo: # "as" dá nome á um objeto
    for nome in nomes: #loop, cada repetição recebe um nome diferente na lista
        arquivo.write(nome + "\n") #"arquivo" é o objeto criado com o comando open()
        print(nome)  #se vc imprimir a lista, ele vai mostrar a lista inteira e cada iteração repetida, por isso se imprime a variável