#Day - 35

for i in range(5):
    print (i)
else:
    print ("The loop has ended")#The else block will be executed after the loop has finished iterating over all the elements in the range.
    
for j in range(5):
    if j == 4:
        break
    print (j)
else:
    print ("The loop has ended") #The else block will not be executed because the loop is terminated by the break statement.

i = 0
while i < 5:
    print (i)
    i += 1
    # if i == 3:
    #     break
else:
    print ("The loop has ended") #The else block will be executed after the loop has finished iterating over all the elements in the range.