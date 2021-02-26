def printcolors(E):
    for srinucolor in E:
        if srinucolor > 50:
            print(srinucolor)
    return srinucolor


colors = [11, 34, 98, 43, 45, 54, 54]
printcolors(colors)
##########################################################################################################
colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]
for srinucolor in colors:
    if (type(srinucolor) == int):
        print(srinucolor)
    # if(isinstance(srinucolor, int)):

########################################################################################################
colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]
for srinucolor in colors:
    if (type(srinucolor) == int and srinucolor > 50):
        print(srinucolor)


#######################################################################################################
def businesslogic(E):
    srinucolor_modified = E + 100
    srinucolor_multiplied = srinucolor_modified * 100
    srinucolor_avg = srinucolor_multiplied / 7
    return srinucolor_avg


E = [11, 34, 98, 43, 45, 54, 54]
for srinucolor in E:
    if srinucolor > 50:
        print(businesslogic(srinucolor))

    # def printcolors(E):
# return srinucolor
# colors = [11, 34, 98, 43, 45, 54, 54]
# printcolors(colors)
##############################################################################################################
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for pair in phone_numbers.items():
    # print(pair[1])
    print("{} has as phone number {}".format(pair[0], pair[1]))
#############################################################################################################
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for key, value in phone_numbers.items():
    print("{} has as phone number {}".format(key, value))

############################################################################################################
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
for key, value in phone_numbers.items():
    print("{}: {}".format(key, value))
##########################################################################################################
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
for key, value in phone_numbers.items():
    modified_value = value.replace('+', '00')
    print(modified_value)
