### **3. Operações com Dicionários**
""""
Crie um dicionário chamado `usuarios` contendo os seguintes dados:

```python
usuarios = {
    "joao": "joao@email.com",
    "maria": "maria@email.com",
    "carlos": "carlos@email.com"
}

Agora, escreva um código que:

- Peça ao usuário para digitar um nome.
- Se o nome existir no dicionário, exiba o e-mail correspondente.
- Caso contrário, exiba a mensagem `"Usuário não encontrado"`.
"""

#Resposta

usuarios = {
    "joao": "joao@email.com",
    "maria": "maria@email.com",
    "carlos": "carlos@email.com"
}

nomes = input("Digite um nome válido: ")  # Armazena a entrada de nomes

if nomes in usuarios:  # Verifica se o nome digitado está no dicionário
    print(f"Usuário {nomes} encontrado, e-mail: {usuarios[nomes]}")  #{} dentro das chaves estão os valores respectivos do dicionário
else:
    print("Erro: Usuário não encontrado.")