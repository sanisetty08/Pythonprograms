import json

with open('D:\IDE\Pythonbasics\sample_nested_json.json', 'r') as myfile:
    data = myfile.read()

print(type(data))
# print(data.keys())
# data_dict = {}


jobj = json.loads(data)
# teststr = obj.read()
teststr = jobj['medications'][0]['anticoagulants'][0]['dose']
# print(json.loads(teststr))

# print(jobj)
print(type(teststr))
mymedications = jobj['medications'][0]


# print(type(mymedications))

def jobj_f(my_dict):
    for my_dose in my_dict:
        if my_dose == 'medications':
            p = my_dict[my_dose][0]
            q = p.get('anticoagulants')
            for my_dose2 in q:
                if my_dose2.keys().get('dose'):
                    print(my_dict)

        # sample = my_dict['medications'][my_dose]
    # if my_dose == my_dict['medications'][my_dose]:
    # print(my_dose)
    return 0


print(jobj_f(jobj))
# jobj['medications'][0]
