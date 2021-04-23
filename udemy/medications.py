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
def myfunc(my_dict):
    my_dose = ?
    return my_dose
