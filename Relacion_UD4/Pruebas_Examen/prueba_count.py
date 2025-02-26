# Cuenta cuántas veces aparece cada vocal en un texto
texto = "Programación en Python"
vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
for letra in texto.lower():
    if letra in vocales:
        vocales[letra] += 1
print(vocales)