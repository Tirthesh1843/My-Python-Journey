#3 round snake water gun game

import random

i = 0
j = 0
k = 0
Name = input("Enter your name: ")
Name_of_computer = input("Enter name of computer: ")
while i < 3:
    X = int(input("Enter 1 for snake, 2 for water and 3 for gun: "))
    c = random.randint(1, 3)
    if c==X:
        print (f"{Name} and {Name_of_computer} both chose same thing. Tie")
    elif c==1 and X==2:
        print (f"{Name_of_computer} chose snake and {Name} chose water. {Name_of_computer} wins this round")
        j += 1
    elif c==1 and X==3:
        print (f"{Name_of_computer} chose snake and {Name} chose gun. {Name} win this round")
        k += 1
    elif c==2 and X==1:
        print (f"{Name_of_computer} choose water and {Name} chose snake. {Name} win this round")
        k += 1
    elif c==2 and X==3:
        print (f"{Name_of_computer} choose water and {Name} chose gun. {Name_of_computer} wins this round")
        j += 1
    elif c==3 and X==1:
        print (f"{Name_of_computer} choose gun and {Name} chose snake. {Name_of_computer} wins this round")
        j += 1
    elif c==3 and X==2:
        print (f" {Name_of_computer} choose gun and {Name} chose water. {Name} win this round")
        k += 1
    i += 1

print ("Game Over")
if k > j:
    print (f"{Name} won the game")
elif k < j:
    print (f"{Name_of_computer} won the game")
else:
    print ("Tie")