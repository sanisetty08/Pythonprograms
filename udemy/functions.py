def lengther(lst):
    item_count = len(lst)
    return item_count


list_1 = [1, 5, 6]
list_2 = ["shiva", "srinu", "sanjay"]
list_3 = [2.5, 6.8, 9.1]

tuple_1 = (7, 5, 9, 4, 3)
tuple_2 = ("ram", "rahim", "robert")

print(lengther(list_3))
print(lengther(tuple_2))
print(lengther(list_1))
print(lengther(list_1) + lengther(list_3))  # user-defined function
print(sum(list_1, 3))  # built in function
