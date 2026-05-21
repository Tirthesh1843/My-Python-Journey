# Day - 13
#string is immutable.

a = "Tirthesh"
print (len(a)) #7
print (a.upper()) #TIRTHESH
print (a.lower()) #tirthesh

b = "!!!!Tirthesh!!!!!!!"
print (b.rstrip("!")) #!!!!Tirthesh
print (a.replace("T", "P")) #Pirthesh
print (a.split(" "))
print (a.count("h")) #2
print (a.find("h")) #4