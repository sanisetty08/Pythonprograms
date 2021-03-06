def srinu(a_list):
    return [a_list[0], a_list[-1]]


a = [5, 10, 15, 20, 25]
print(srinu(a))

######################################################################################
only_integers = []


def only_numbers(E):
    for only_number in E:
        if (type(only_number) == int):
            only_integers.append(only_number)
    return only_integers


print(only_numbers([99, 'no data', 95, 94, -45, 'no data']))

##########################################################################################
only_integers = []


def only_numbers(E):
    for only_number in E:
        if (type(only_number) == int):
            only_integers.append(only_number)
        else:
            only_integers.append(0)
    return only_integers


print(only_numbers([99, 'no data', 95, 94, -45, 'no data']))

#########################################################################################

only_integers = []


def only_numbers(E):
    for only_number in E:
        if (type(float(only_number)) == float):
            only_integers.append(float(only_number))
    return sum(only_integers)


my_sum_output = only_numbers(['1.2', '2.6', '3.5'])
print(my_sum_output)


################################################################################################
def my_conc(E, F):
    return E + F


print(my_conc('shiva', 'ram'))


################################################################################################
def my_conc(E):
    return '$'.join(E)


print(my_conc(['shiva', 'ram']))
