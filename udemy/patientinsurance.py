import json

with open('D:\IDE\Pythonbasics\SimpleUSMedicalSurgeryClaimAll.json', 'r') as myfile:
    data = myfile.read()

print(type(data))

jobj = json.loads(data)
# print(jobj)
# myinsurance = jobj['contained'][0]['name'][0]['given'][0]
# print(type(myinsurance))
# print(myinsurance)

myaddress_list = []
for my_contain in jobj['contained']:
    if my_contain.get('resourceType') == 'Patient':
        name_list = my_contain.get('name')
        # print(type(name_list[0]))
        for my_name in name_list:
            my_namelistFinal = my_name.get('given')
            for my_namefinal in my_namelistFinal:
                name = my_namefinal
                # print(my_namefinal)

    if my_contain.get('resourceType') == 'Patient':
        address_list = my_contain.get('address')
        for add in address_list:
            address_home = add.get('line')
            address_city = add.get('city')
            address_state = add.get('state')
            address_postal = add.get('postalCode')
            address_country = add.get('country')
            for addmain in address_home:
                # print(addmain + ' ' + address_city + ' ' + address_state + ' ' + address_postal + ' ' + address_country)
                # s_tuple = (name,addmain + ' ' + address_city + ' ' + address_state + ' ' + address_postal + ' ' + address_country)
                # print(s_tuple)
                # s_dict = {name: addmain + ' ' + address_city + ' ' + address_state + ' ' + address_postal + ' ' + address_country}
                # print(s_dict)
                s_list = [name, addmain, address_city, address_state, address_postal, address_country]
                # print(s_list)
                myaddress_list.append(s_list)

print(myaddress_list)
