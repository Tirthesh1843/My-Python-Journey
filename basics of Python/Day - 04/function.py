#Day - 20
def calculategmean (a,b):
  mean = (a*b)/(a+b)
  print (mean)
  
def isgreater (a,b):
  if a > b:
    print ("a is greater than b")
  elif a < b:
    print ("b is greater than a")
  else:
    print ("a and b are equal")
a = 9
b = 8

# gmean1 = (a*b)/(a+b)
# print (gmean1)
calculategmean (a,b)
isgreater (a,b)
c = 4
d = 12

gmean2 = (c*d)/(c+d)
print (gmean2)
isgreater (c,d)