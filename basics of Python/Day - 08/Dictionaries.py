#Day - 33
#Dictionaries are unordered collection of key-value pairs. They are defined using curly braces {} and the key-value pairs are separated by a colon (:). Dictionaries do not allow duplicate keys and the values can be of any data type.

dic = {
    11 : "Tirthesh",
    144: "Shion",
    "leader": "Rimuru",
    234: "Benimaru",
    1: "veldora"
}
print (dic)
print (dic[11])
print (dic.get(144))
print (dic["leader"])

print (dic.keys())
print (dic.values())

for key in dic.keys():
    print (f"the value corresponding to the key {key} is {dic[key]}")