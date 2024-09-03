#5) Programa para inverter os caracteres de uma string

def inverter_string(s):
    invertida = ""
    for i in range(len(s)-1, -1, -1):
        invertida += s[i]
    return invertida

string = input("Informe a string: ")
print("String invertida:", inverter_string(string))
