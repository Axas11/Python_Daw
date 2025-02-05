ano = int(input("Inserta el ano: "))

if ano % 100 == 0:
    siglo = ano // 100
else:
    siglo = ano // 100 + 1

print(f"El ano {ano} pertenece al siglo {siglo}")