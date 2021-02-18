# the keys and value in the dict may come from database and its my responsibility to figure out how to incorporate them in the program
# hint use for loop or while loop
# srinu_list = [12,15.1,65,84,56.5]
srinu_list = (12, 15.1, 65, 84, 56.5)  # srinu_list in tuple fashion: immutable
# srinu_list.append(19.3) #modified the original
# srinu_list.remove(12) #modified to original second time
# srinu_dict = {"srinu":12, "shiva":15.1, "sanjay":65, "sai":84, "mano":56.5}
# Avgformula = total sum of elements in the list divided by total number of elements in the list
# srinu_sum = sum(srinu_dict.values())
# srinu_count = len(srinu_dict)
srinu_sum = sum(srinu_list)
srinu_count = len(srinu_list)
srinu_avg = srinu_sum / srinu_count
print(srinu_avg)
# print(srinu_dict.keys())
