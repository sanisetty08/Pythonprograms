import json

with open('D:\IDE\Pythonbasics\SimpleUSMedicalSurgeryClaimAll.json', 'r') as myfile:
    data = myfile.read()

print(type(data))

jobj = json.loads(data)
# print(jobj)
# myinsurance = jobj['contained'][0]['name'][0]['given'][0]
# print(type(myinsurance))
# print(myinsurance)

for my_contain in jobj['contained']:
    if my_contain.get('resourceType') == 'Patient':
        name_list = my_contain.get('name')
        # print(type(name_list[0]))
        for my_name in name_list:
            my_namelistFinal = my_name.get('given')
            for my_namefinal in my_namelistFinal:
                print(my_namefinal)

    # if
    # q = my_contain
    # print(q)

#     for my_insurer in insurer:
#         if my_name == 'contained':
#             n = insurer[my_name][0]
#             p = n.get('name')
#             r = p[0]
#             s = r.get('given')
#     print(insurer)
#
# print(jobj_f(jobj))
