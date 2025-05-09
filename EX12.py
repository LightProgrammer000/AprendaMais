# Imprime uma mensagem e solicita que o usuário pressione Enter
print('Iniciando execução do programa')
input('Digite algo e pressione Enter: ')  # Espera a entrada do usuário
print('Encerrando execução do programa')

# Atribui o valor digitado a uma variável e imprime
digitado = input('\nDigite algo e pressione Enter: ')   # O dado fornecido é armazenado em 'digitado'
print('Você escreveu:', digitado)                       # Imprime o valor armazenado em 'digitado'

# Imprime diretamente o valor digitado sem armazenar em uma variável
print('Você escreveu:', input('\nDigite algo e pressione Enter: '))  # Imprime o que o usuário digitar
