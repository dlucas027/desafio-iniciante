# 5. Conexão Telnet com Python

""""
Escreva um código Python que utilize a biblioteca `telnetlib` para:

- Conectar-se ao IP `192.168.1.1` na porta **23** (Telnet).
- Enviar um comando simples (`help` ou `exit`).
- Exibir a resposta do servidor na tela.

Caso o servidor não esteja acessível, o código deve tratar a exceção e exibir uma mensagem apropriada.

Dica: O módulo `telnetlib` pode ser utilizado para fazer essa conexão.
"""



import telnetlib #biblioteca para requisição telnet 

try:  #evita que quebre no meio se der algum erro, nesse caso ele aciona o except
    tn = telnetlib.Telnet("towel.blinkenlights.nl", timeout=10) #Precisa ser em um servidor que aceita telnet - telnetlib.Telnet(Cria a conexão como o servidor específicado)
    tn.write(b"help\n")  #b, indica que os dados estão em bytes, .write escreve e envia na conexão telnet
    print("Conexão realizada")

    response = tn.read_all() #read_all() lê a resposta do dispositivo até atender a condição específica
    print(response.decode('utf-8')) #.decode() pega os bytes e os transforma em um texto legível

except Exception as erro:  #tratamento de erros (Exception as: captura os erros e armazena na variavel {erro})
    print(f"Erro: {erro}")

finally:  #fechamento, independente de erro ou não
    tn.close()