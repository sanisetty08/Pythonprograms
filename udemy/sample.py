only_integers = [1, 2, 6, 8, 9.1, "sam", "shiva"]
only = []


def only_numbers(E):
    for only_number in E:
        if (type(only_number) == int):
            only.append(only_number)
    return only


print(only_numbers(only_integers))
