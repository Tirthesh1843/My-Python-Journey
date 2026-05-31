# ===== Student Marks Manager =====

# 1. Add Student
# 2. View Students
# 3. Show Top Student
# 4. Exit

# Enter choice: 1

# Enter name: 
# Enter marks: 

# Student added successfully!


Student = []
percentage = []
i = int(input("Enter number of students: "))
for _ in range(i):
    name = input ("student\'s name:")
    marks = int(input ("Student\'s percentage:"))
    Student.append (name.upper())
    percentage.append (marks)

print("Student list")
for x in range(len(Student)):
    print(Student[x] ,":", percentage[x])
j = input("enter student's name for student's marks:")
SIndex = Student.index(j.upper())
print (Student[SIndex], percentage[SIndex])

TopStudent = int(input("Do you want to check top student enter \"1\" for \"Yes\" and \"2\" for \"No\": "))

if (TopStudent == 1):
    max = max(percentage)
    i = percentage.index(max)
    print ("Top student is", Student[i], percentage[i])
else:
    print("thank you for your coordination")