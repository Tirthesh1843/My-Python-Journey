#Day - 019
#Break and Continue
for i in range(12):
  print ("5 x",i+1,"=",5 * (i+1))
  if i == 9:
    break

#Continue
for i in range(12):
  if i == 9:
    print ("Skip the value 10")
    continue
  print ("5 x",i+1,"=",5 * (i+1))