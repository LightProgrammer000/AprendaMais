# Variável x é igual a 10
x = 10

# Verifica se x é menor que 20 ou maior que 15
if x < 20 or x > 15:
    print('O resultado da expressão foi verdadeiro')

# A mesma verificação, repete a expressão
if x < 20 or x > 15:
    print('O resultado da expressão foi verdadeiro')

# Compara a string '7' com o número 7 (diferentes tipos)
if '7' == 7:
    print("ok")
else:
    print("Nao Ok")

# Compara a string 'Teste' com 'teste' (diferente por causa de maiúsculas/minúsculas)
if 'Teste' == 'teste':
    print("ok")
else:
    print("Nao Ok")

# Compara o número 3 com a string "3" (diferentes tipos)
a = 3
if a == "3":
    print("Ok")
else:
    print("Nao Ok")
