import time

time = time.strftime("%H:%M:%S")
if (time < "12:00:00"):
    print("Good Morning Sir")
elif (time < "18:00:00"):
    print("Good Afternoon Sir")    
elif (time < "22:00:00"):    
  print("Good Evening Sir")
else:  
  print("Good Night Sir")