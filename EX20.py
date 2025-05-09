# Solicita ao usuário um número e o converte para float
valor = float(input('Digite um número: '))

# Verifica se o número é negativo
if valor < 0:
    # Parte que executa se a condição for verdadeira (número negativo)
    print('O número que você digitou é negativo')
    print('e eu sei disso pois ele é menor que zero')

else:
    # Parte que executa se a condição for falsa (número não-negativo)
    print('O número que você digitou é positivo')
    print('ou é igual a zero, não tenho certeza')

# Imprime "Fim do programa" independentemente do que aconteça
print('Fim do programa')
