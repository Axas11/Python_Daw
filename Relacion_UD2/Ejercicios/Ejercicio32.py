nterm = int(input("Cuantos numeros quieres generar de fibonnaci: "))
contador = 1
termant = 0
termact = 0
newterm = 0
while contador<=nterm:
    
    contador = contador + 1
    
    if contador == 1:
        termant = 0
        print(termant)
    
    if contador == 2:
        termact = 1
        print(termact)

    if contador >= 3:
        newterm = termact + termant
        print(newterm)
        termant = termact
        termact = newterm
