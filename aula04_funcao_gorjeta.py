aula04_funcao_gorjeta.py

def calculo_gorjeta(valor_conta, porcentagem_gorjeta):
total_conta = float(input("Informa o total da conta: "))
porcentagem = float(input("Informe a porcentagem da gorjeta: "))


valor_gorjeta = calculo_gorjeta(total_conta, porcentagem)

print(f"Para uma conta de {total_conta:.2f}, a gorjeta de {porcentagem}% tem o valor de R${valor_gorjeta}")