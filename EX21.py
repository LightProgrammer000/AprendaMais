# Solicita ao usuário um número
valor = float(input('Digite um número: '))

# Solicita ao usuário uma escolha: 1 para calcular o dobro ou outro valor para calcular a metade
escolha = float(input('Digite 1 para calcular o dobro, ou outra coisa para calcular a metade:'))

# Verifica se a escolha é 1 (para calcular o dobro)
if escolha == 1:
    # Calcula o dobro do valor
    dobro = 2 * valor
    print(f'O dobro de {valor} é {dobro}')

else:
    # Caso a escolha não seja 1, calcula a metade do valor
    metade = valor / 2
    print(f'A metade de {valor} é {metade}')

# Finaliza o programa
print('Fim do programa')
