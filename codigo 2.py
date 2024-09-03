#2) Programa para verificar se um número pertence à sequência de Fibonacci

def fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n or n == 0

num = int(input("Informe um número: "))

if fibonacci(num):
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")
