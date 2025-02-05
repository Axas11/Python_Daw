cont = 0
pal = ""

while pal != "fin":
  pal = input("Ingrese una palabra o fin para terminar: ")
  if len(pal) <= 5 and pal != "fin":
    cont += 1

print("Cant de palabras con menos de 5 caracteres:", cont)