# method using list comprehension
list1 = [1,2,3,4,5,8]
list2 = [3,4,5,6,7,8]
common = [num for num in list1 if num in list2]
print("common elements: ", common)
#common elements:  [3, 4, 5, 8]