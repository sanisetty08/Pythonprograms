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
