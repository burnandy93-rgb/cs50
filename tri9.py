#method 4 taking user
list1 = list(map(int, input("enter first list").split()))
list2 = list(map(int, input("enter second list").split()))
common =[num for num in list1 if num in list2]
print("common elements: ",common)
#3input lists as follow 10 20 30 40
