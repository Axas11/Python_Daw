def calcularnota(nota):
    while True:
        if nota == "DO":
            anglosajona = "C"
        elif nota == "RE":
            anglosajona = "D"
        elif nota == "MI":
            anglosajona = "E"
        elif nota == "FA":
            anglosajona = "F"
        elif nota == "SOL":
            anglosajona = "G"
        elif nota == "LA":
            anglosajona = "A"
        elif nota == "SI":
            anglosajona = "B"
        elif nota == "fin":
            break
        
        print(f"{nota} en notacion anglosajona es {anglosajona}") 
        nota = input("Introduce una nota (DO, RE, MI, FA, SOL, LA, SI(fin para terminar): ")

nota = input("Introduce una nota (DO, RE, MI, FA, SOL, LA, SI(fin para terminar): ")
calcularnota(nota)