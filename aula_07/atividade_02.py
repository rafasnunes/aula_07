# Atividade 02

# O pescador João, que atua na região costeira de Santa Catarina, procurou sua
# empresa de tecnologia para resolver uma necessidade que ele enfrenta no dia
# a dia. De acordo com o regulamento de pesca do estado, a quantidade máxima
# permitida de peixes por dia é de 100 quilos.

# Quando esse limite é ultrapassado, o pescador deve pagar uma multa de R$ 4,00
# por quilo excedente.
# João precisa de um programa simples que ele possa usar no celular para
# informar o peso total de peixes pescados no dia, e assim verificar se
# haverá multa ou não. Caso ultrapasse o limite, o sistema deve calcular o
# valor da multa automaticamente.

# Requisito:
# Crie uma função que:
# * Receba o peso total de peixes pescados no dia
# * Verifique se houve excesso
# * Calcule e retorne o valor da multa, se houver
# * Mostre a mensagem correspondente na tela

LIMITE_PESO = 100  # Limite em Kg do peso máximo permitido sem multa.
TARIFA_MULTA = 4  # Valor em R$ por cada Kg excedente.


def calc_multa(num):
    multa = (num - LIMITE_PESO) * TARIFA_MULTA
    return multa


peso = float(input('Digite o peso pescado: '))

if peso > LIMITE_PESO:
    multa = calc_multa(peso)
    print(f'O valor da multa é: R$ {multa}')
else:
    print(f'Não há valor a ser pago.')
