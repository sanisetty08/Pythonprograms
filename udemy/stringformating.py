# loop with two variables with string formating
phone_numbers = ['37682929928', '423998200919']
flat_number = ['401', '404']
# for phone_numbers, flat_number in zip(phone_numbers, flat_number):
# print("phone number=" + str(phone_numbers) + " and flat number=" + str(flat_number))

for phone_numbers, flat_number in zip(phone_numbers, flat_number):
    print("phone number= %s and flat number= %s" % (phone_numbers, flat_number))

# loop with dictionaries
# phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
# for key, value in phone_numbers.items():
# print("{}: {}" .format(key,value))
