# 4. Requisição Simples à API ViaCEP

""""
Escreva um código em Python que utilize a API pública do ViaCEP para buscar informações sobre o CEP **01001-000**. O programa deve:

- Fazer a requisição na URL: `https://viacep.com.br/ws/01001000/json/`
- Exibir na tela o **logradouro** e a **cidade**.
"""


#Resposta

import requests    #biblioteca requests   
#import json? caso precise manipular os dados diretamente
cep = requests.get("https://viacep.com.br/ws/01001000/json/") #método get -requests.get- (api de cep grátis)
dados = cep.json()  #armazena a requisição na variavel dados \\ cep.json() cep é o objeto que resposta de requests, *.json* transforma do formato json pra dicionário

logradouro = dados["logradouro"]
bairro = dados["bairro"]
cidade = dados["localidade"]
regiao = dados["regiao"]
complemento = dados["complemento"]
estado = dados["uf"]
#só tratar como um dicionário comum
#dá pra fazer a requisição puxando primeiro os "dados" antes de montar as variaveis que você vai usar
print(f" Estado: {cidade}\n Cidade: {cidade}\n Região: {regiao}\n Bairro: {bairro}\n Logradouro: {logradouro}\n Complemento: {complemento}.")



