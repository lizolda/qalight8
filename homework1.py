total = 0
list1 = [7, 9, 10, 11]
for element in range(0, len(list1)):
    total = total + list1[element]

print("Sum of all elements in given list: ", total)

list2 = [2, 2, 6, 10, 15, 10, 6]
print(set(list2))

dict = {'Name': 'Yuriy', 'ID': 'user_id', 'Salary': 20000}
dict['Salary'] = dict['Salary'] * 1.5
print(dict)