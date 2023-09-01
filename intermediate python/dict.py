mydict = {"name":"sanjeet","age":28,"city":"New york"}
mydict1= {'roll':21,"height":6,}
mydict.update(mydict1)
print(mydict)
for key,value in mydict.items():
    print(key,value)
mydict["gender"]= "male"
print(mydict)
# del mydict["name"]
# mydict.pop("age")
# print(mydict)