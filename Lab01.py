
renda_anual = float(input())
despesas = float(input())
imposto_ja_pago = float(input())
#-----------------------------------------------------------
def calculo_de_resultado(renda_ajustada):
    if renda_ajustada <= 22847.76:
        imposto_a_pagar = 0
        
    elif 22847.76 < renda_ajustada <= 33919.80:
        imposto_a_pagar = renda_ajustada*0.075 - 1713.58
        
    elif 33919.81 < renda_ajustada <= 45012.60:
        imposto_a_pagar = renda_ajustada*0.15 - 4257.57
        
    elif 45012.61 < renda_ajustada <= 55976.16:
        imposto_a_pagar = renda_ajustada*0.225 - 7633.51
        
    else:
        imposto_a_pagar = renda_ajustada*0.275 - 10432.32

    return ('{:.2f}'.format(imposto_a_pagar - imposto_ja_pago))
#-----------------------------------------------------------
def calculo_completo(renda_c):
    nova_renda_c = renda_c - despesas
    return calculo_de_resultado(nova_renda_c)    
#-----------------------------------------------------------
def calculo_simples(renda_s):
    if renda_s*0.2 > 16754.34:
        nova_renda_s = renda_s - 16754.34
    else:
        nova_renda_s = renda_s - renda_s*0.2
    return calculo_de_resultado(nova_renda_s)
#-----------------------------------------------------------
resultado_c = float(calculo_completo(renda_anual))
resultado_s = float(calculo_simples(renda_anual))
#-----------------------------------------------------------
def escolha_de_resultado(a, b):
    if a < 0 and b < 0:
        print('VALOR A SER RESSARCIDO: R$ '+'{:.2f}'.format((-1)*b))
    elif b > 0 and a > 0:
        print("VALOR A PAGAR: R$ "+'{:.2f}'.format(b))
    else:
        print('VALOR A SER RESSARCIDO: R$ '+'{:.2f}'.format((-1)*b))
#-----------------------------------------------------------
if resultado_c >= resultado_s:
    escolha_de_resultado(a=resultado_c, b=resultado_s)

else:
    escolha_de_resultado(b=resultado_c, a=resultado_s)
