def meaner(lst):
    item_mean = sum(lst) / len(lst)
    return item_mean


list_1 = [1, 5, 6]
list_2 = ["shiva", "srinu", "sanjay"]
list_3 = [2.5, 6.8, 9.1]

tuple_1 = (7, 5, 9, 4, 3)
tuple_2 = ("ram", "rahim", "robert")

# print(meaner(list_3))
# print(meaner(list_1))
# print(meaner(list_1) + meaner(list_3)) # user-defined function
# print(mean(list_1,3)) # built in function

if (meaner(list_1) > 15):
    print(list_1)
elif (meaner(tuple_1) > 15):
    print(tuple_1)
elif (meaner(list_3) > 15):
    print(list_3)
else:
    print("none")
