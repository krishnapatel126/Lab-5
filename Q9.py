list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = [4, 5, 6, 8, 9]
list3 = [num for num in list1 if num not in list2]
print("Numbers from list1 that are not in list2:", list3)
