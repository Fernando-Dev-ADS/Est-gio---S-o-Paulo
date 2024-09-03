#3) Programa para calcular valores de faturamento diário

import json

data = '''
{
    "faturamento": [0, 1000, 2500, 800, 500, 0, 0, 1200, 3000, 0, 100, 0, 200, 0]
}
'''

faturamento = json.loads(data)["faturamento"]

faturamento = [valor for valor in faturamento if valor > 0]

menor_faturamento = min(faturamento)
maior_faturamento = max(faturamento)
media_mensal = sum(faturamento) / len(faturamento)

dias_acima_da_media = len([valor for valor in faturamento if valor > media_mensal])

print(f"Menor faturamento: {menor_faturamento}")
print(f"Maior faturamento: {maior_faturamento}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")
