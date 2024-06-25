valor = float(input())

n = True
resposta = ''

if(valor < 0 or valor > 100):
    resposta += 'Fora de intervalo'
    n = False
    
if(valor <= 25.00 and n):
    resposta += 'Intervalo [0,25]'
    n = False

if(valor <= 50.0 and n):
    resposta += 'Intervalo (25,50]'
    n = False
    
if(valor <=75.0 and n):
    resposta += 'Intervalo (50,75]'
    n = False

if(valor <=100.0 and n):
    resposta += 'Intervalo (75,100]'
    n = False

print(resposta)