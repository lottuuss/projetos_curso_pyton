
import re

cpf_enviado = re.sub(r'[^0-9]','',input('Digite o seu cpf:')) 

#digito 1
nove_digitos = cpf_enviado[:9]
contador_regressivo1 = 10
resultado1 = 0


for digito1 in nove_digitos:
    resultado1 += int(digito1) * contador_regressivo1
    contador_regressivo1 -=1
digito1 = ((resultado1 * 10) % 11)
digito1 = digito1 if digito1 <9 else 0


#digito 2 
dez_digitos = nove_digitos + str(digito1)
contador_regressivo2 = 11
resultado2 = 0

for digito2 in dez_digitos:
    resultado2 += int(digito2) * contador_regressivo2
    contador_regressivo2 -=1
digito2 = ((resultado2) * 10 % 11)
digito2 = digito2 if digito2 <= 9 else 0    


cpf_verificado = f'{nove_digitos}{digito1}{digito2}'

if cpf_enviado == cpf_verificado :
    print(f'O CPF: {cpf_enviado} é válido')
else:    
    print(f'O CPF: {cpf_enviado} é inválido')
