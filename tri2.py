#find the index of element in array
def linear_search(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1
result = linear_search([10,20,30,40,50],50)
if result != -1:
    print("found at index: ",result)
else:
    print("not found")
    #found at index:  4