#Day - 34

#Dictionary Methods
#clear() - removes all the elements from the dictionary
#copy() - returns a copy of the dictionary
#keys() - returns a list of all the keys in the dictionary
#values() - returns a list of all the values in the dictionary
#items() - returns a list of all the key-value pairs in the dictionary

dic = {
    11 : "Tirthesh",
    144: "Shion",       
    "leader": "Rimuru",
    234: "Benimaru",
    1: "veldora"
}

dic2 = {
    2: "diablo",
    3: "milim",
    4: "guy",
    5: "shuna"
}

dic.update(dic2) #updates the dictionary with the key-value pairs from another dictionary
print (dic)
dic2.clear() #removes all the elements from the dictionary
print (dic2)
dic3 = dic.copy() #returns a copy of the dictionary
print (dic3)
print (dic.keys()) #returns a list of all the keys in the dictionary
print (dic.values()) #returns a list of all the values in the dictionary
print (dic.items()) #returns a list of all the key-value pairs in the dictionary
dic.pop(11) #removes the key-value pair with the specified key and returns the value
print (dic)