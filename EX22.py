# Solicita ao usuário um número entre 0 e 10
valor = float(input('Digite um número entre 0 e 10: '))

# Verifica se o valor está entre 0 e 10
if valor >= 0:

    # Verifica se o valor não ultrapassa 10
    if valor <= 10:
        print('Obrigado! Você digitou:', valor)
    else:
        print('Valor inválido')
else:
    print('Valor inválido')
