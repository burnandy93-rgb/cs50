numbers = [10,20,30,40,50]
target = 20
found = False
for num in numbers:
    if num == target:
        found = True
        break
print(f"Found" if found else "not found")
