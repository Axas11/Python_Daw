# Crea una lista con 1000 números aleatorios entre 1 y 100. Encuentra el número que MÁS veces se repite. 
import random
nums = []

max_reps = 0
num_rep = 0

for _ in range(1000):
    nums.append(random.randint(1,100))

for n in range(len(nums)):
    repes = nums.count(n)
    if repes > max_reps:
        max_reps = repes
        num_rep = n

print(f"El número que más veces se repite es: {num_rep} se repite {max_reps} veces")
