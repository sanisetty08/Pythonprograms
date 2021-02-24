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


#######################################################################################################
def password_controller(E):
    if len(E) < 8:
        return False
    else:
        return True


print(password_controller("mypass"))
print(password_controller("mylingpassword"))
# method2
password_controller_var = password_controller("mypass")
print(password_controller_var)


###########################################################################################################
def temperature(E):
    if (E > 7):
        return "Warm"
    else:
        return "Cold"


print(temperature(10))
print(temperature(7))


###########################################################################################################
def temperature(E):
    if (E > 25):
        return "Hot"
    elif (E >= 15) and (E <= 25):
        return "Warm"
    else:
        return "Cold"


# print(temperature(10))
# print(temperature(70))
# user_input = int(input("Enter some number:"))
user_input = float(input("please enter some temperature number:"))
print(temperature(user_input))
