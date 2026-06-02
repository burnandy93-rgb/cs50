numbers = [10,20,30,40,50]
target = 20
i = 0
found = False
while i < len(numbers):
    if numbers[i] == target:
        found = True
        break
    i+= 1
print(f"Found" if found else "not found")