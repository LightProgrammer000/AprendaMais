# Solicita ao usuário para digitar o turno
turno = input('Digite m para manhã, t para tarde, ou n para noite: ')

# Verifica qual turno foi digitado e imprime a saudação correspondente
if turno == 'm':
    print('Bom dia!')  # Para o turno da manhã
else:
    if turno == 't':
        print('Boa tarde!')  # Para o turno da tarde
    else:
        if turno == 'n':
            print('Boa noite!')  # Para o turno da noite
        else:
            print('Letra inválida')  # Para qualquer entrada que não seja 'm', 't' ou 'n'
