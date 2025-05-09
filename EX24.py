# Solicita ao usuário para digitar o turno
turno = input('Digite m para manhã, t para tarde, ou n para noite: ')

# Verifica o turno digitado e imprime a saudação correspondente
if turno == 'm':
    print('Bom dia!')  # Para o turno da manhã

elif turno == 't':
    print('Boa tarde!')  # Para o turno da tarde

elif turno == 'n':
    print('Boa noite!')  # Para o turno da noite

else:
    print('Letra inválida')  # Caso a entrada não seja 'm', 't' ou 'n'
