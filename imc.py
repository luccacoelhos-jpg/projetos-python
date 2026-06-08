#etapa 1 - calculo do imc
def calc_imc(imc):
    imc = peso /(altura*altura)
    return imc


#etapa 2 - classificação do imc
def classificar_imc(resultados):
    if resultados >= 25:
        return "ACIMA DO PESO"
    else:
        return "PESO NORMAL"


#etapa 3 - mensagem de retorno
def mensagem(status):
    if status == "ACIMA DO PESO"
       return "⚠️Atenção! Procure um médico!"
    else:
        return "👌Seu peso está normal! Continue assim!"
#etapa 4 - integração do código
valor_peso = float(input("Digite o seu peso:"))
valor_altura = float(input("Digite sua altura:"))

valor_imc = calc_imc(valor_peso,valor_altura)
resultado_imc = classificar_imc(valor_imc)
saida = mensagem(resultado_imc)

print("="*50)
print("RESULTADO DO SEU IMC")
print(f\n"Seu IMC é: (valor_imc)")
print(f\n "{saída}")