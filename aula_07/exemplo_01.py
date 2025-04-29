# Funções em Python iniciam com a palavra reservada def.
# Funções são rotinas em seu conceito.

# def saudacao(nome, curso, turno):
#     print(f'Olá {nome}! Bem vindo ao curso de {curso} no turno da {turno}.')

# saudacao('João','Análise de Dados','Noite')

def somar (a, b):
    s = a + b
    # print(soma)
    return s

soma1 = somar (4,5)
print(f'O valor da variável é {soma1}')

soma2 = somar (7,3)
print(f'O valor da variável é {soma2}')

soma3 = somar(soma1, soma2)
print(f'O valor total é {soma3}')

def somar_numeros(x,y):
    s = x + y
    return s

for i in range(3):
    n1 = int(input('Informe o primeiro número: '))
    n2 = int(input('Informe o segundo número: '))

    soma = somar_numeros(n1, n2)
    print(soma)