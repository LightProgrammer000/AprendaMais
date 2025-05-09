# Solicita ao usuário para digitar um número entre 0 e 10
valor = float(input('Digite um número entre 0 e 10: '))

# Verifica se o valor está entre 0 e 10 (inclusive)
if 0 <= valor <= 10:
    print('Obrigado! Você digitou:', valor) # Se o número estiver no intervalo correto
else:
    print('Valor inválido')                 # Se o número estiver fora do intervalo
