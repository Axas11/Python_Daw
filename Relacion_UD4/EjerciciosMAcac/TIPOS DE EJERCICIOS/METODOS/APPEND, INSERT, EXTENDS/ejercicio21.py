# Crea un programa que inserte números en una lista hasta que insertes el número 0 para terminar. Los números deberán estar ordenados de menor a mayor. Prohibido utilizar el método .sort().
nums = []
while True:
    n = int(input("Inserta un número: "))
    if n == 0:
        break
    if not nums:
        nums.append(n)
    else:
        for i in range(len(nums)):
            if n < nums[i]:
                nums.insert(i, n)
                break
        else:
            nums.append(n)
print(f"Los números insertados ordenados de menor a mayor son: {nums}") 
