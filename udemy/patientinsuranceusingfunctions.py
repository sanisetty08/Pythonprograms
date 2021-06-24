import json

import pandas as pd

with open('D:\IDE\Pythonbasics\SimpleUSMedicalSurgeryClaimAll.json', 'r') as myfile:
    data = myfile.read()

print(type(data))

jobj = json.loads(data)


# print(jobj)
# myinsurance = jobj['contained'][0]['name'][0]['given'][0]
# print(type(myinsurance))
# print(myinsurance)

# This will not work because each result is not saved anywhere
# def mynamefunc():
#     for my_contain in jobj['contained']:
#         if my_contain.get('resourceType') == 'Patient':
#             name_list = my_contain.get('name')
#             for my_name in name_list:
#                 my_namelistFinal = my_name.get('given')
#                 for my_namefinal in my_namelistFinal:
#                     name = my_namefinal
#     return name

# This will not work because each result is not saved anywhere
# def myfunc(inputkey):
#     for my_contain in jobj['contained']:
#         if my_contain.get('resourceType') == 'Patient':
#             address_list = my_contain.get('address')
#             for add in address_list:
#                 full_address = add
#                 #print(address_home)
#     return full_address.get(inputkey)

# This function will work because for each result will be saved into empty list.
def myfunc_list():
    mylist_list = []
    for my_contain in jobj['contained']:
        if my_contain.get('resourceType') == 'Patient':
            address_list = my_contain.get('address')
            for add in address_list:
                full_address = add
                var0 = my_contain.get('name')[0].get('given')[0]
                var1 = full_address.get('line')[0]
                var2 = full_address.get('city')
                var3 = full_address.get('state')
                var4 = full_address.get('postalCode')
                var5 = full_address.get('country')
                var_v = [var0, var1, var2, var3, var4, var5]
                mylist_list.append(var_v)
    return mylist_list


# my_functest = mynamefunc() + ' ' + myfunc('line')[0] + ' ' + myfunc('city') + ' ' + myfunc('state') + ' ' + myfunc('postalCode')\
#             + ' ' + myfunc('country')
# print(my_functest)

# print(myfunc_list())

data = myfunc_list()
# converting list of lists to dataframe
df = pd.DataFrame(data)
df.columns = ['Name', 'Address', 'City', 'State', 'Zipcode', 'Country']
print(df)
