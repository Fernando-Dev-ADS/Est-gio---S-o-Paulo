#4) Programa para calcular o percentual de faturamento por estado

faturamento = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

faturamento_total = sum(faturamento.values())

percentual_por_estado = {estado: (valor / faturamento_total) * 100 for estado, valor in faturamento.items()}

for estado, percentual in percentual_por_estado.items():
    print(f"{estado}: {percentual:.2f}%")
