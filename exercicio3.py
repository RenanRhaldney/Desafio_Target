"""
3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;
"""

import json

f = open('dados.json')
data = json.load(f)

dias = len(data)
dias_uteis = dias
contador, soma, media_mensal, dias_fat_alto, maior_fat, menor_fat = 0, 0, 0, 0, 0, 0

# Descobrindo a quantidades de dias uteis e somando os faturamentos
for indice in data:        
    if indice['valor'] <= 0:
        dias_uteis -= 1
        
    soma += indice['valor']
    
media_mensal = soma / dias_uteis    


for i in data:
    # Contando quantos dias o faturamento foi maior que a media e descobrindo o maior faturamento
    if i['valor'] > media_mensal:
        fat_acima_da_media = i['valor']
        dias_fat_alto += 1
        
        if maior_fat < fat_acima_da_media:
            maior_fat = fat_acima_da_media
        
    else:
        menor_fat = i['valor']
    
print(f'MAIOR FATURAMENTO = {maior_fat:.2f}')
print(f'MENOR FATURAMENTO = {menor_fat:.2f}')

print(f'QUANTIDADE DE DIAS QUE TEVE UM FATURAMENTO ACIMA DA MEDIA = {dias_fat_alto}')

f.close