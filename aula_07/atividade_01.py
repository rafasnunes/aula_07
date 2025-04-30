# Atividade Prática

# Uma gráfica precisa de um programa que, dado um número, calcule o dobro, o triplo e o quadrado desse número para agilizar seus orçamentos.

# O dobro da quantidade solicitada (para ofertas promocionais)
# O triplo (para grandes eventos)
# E a área total de um adesivo, considerando que o número informado é o lado do adesivo em centimetros.

#Crie uma função que faça esses cálculos e mostre os resultados na tela.

# Requisito

# Criar uma função que receba um número
# Calcular o dobro, triplo e quadrado
# Retornar estes três valores para serem apresentados no programa principal.

# Funções

def calculo(n):  
    d = n * 2
    t = n * 3
    q = n ** 2

    return d, t, q

# Início do programa

num = int(input('Insira o número para o calculo: '))

calculo1, calculo2, calculo3 = calculo(num) # Chama a função calculo enviando o valor da variavel 'num" para a função calculo e recebe de retorno 3 variaveis, por isso criacao de 3 variaveis no começo.

print(f'O dobro do número é {calculo1}. O triplo do número é {calculo2}. O número ao quadrado é {calculo3}')
