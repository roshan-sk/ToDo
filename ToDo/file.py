import json

with open('ToDo\\MOCK_DATA.json') as f:
    dum=json.load(f)
l1=[]
p1=[]
for i in dum:
    l1={'model':"ToDo.Task",'fields':i}
    p1.append(l1)

json_obj = json.dumps(p1)

with open("json_obj.json", "w") as outfile:
    outfile.write(json_obj)
