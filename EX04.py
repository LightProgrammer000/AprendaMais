# Definição da função com dois parâmetros
def exemplo(a, b):
    print(a, b)

# Chamada com argumentos posicionais
exemplo(10, 20)  # Correto

# Chamada com argumentos nomeados
exemplo(a=10, b=20)  # Correto

# Mistura de posicional e nomeado (posicionais primeiro)
exemplo(10, b=20)  # Correto

# Erro: argumento nomeado não pode vir antes de um posicional
# exemplo(a=10, 20)  # ERRO!
