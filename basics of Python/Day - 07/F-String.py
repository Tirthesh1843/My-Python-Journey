letter = "hey my name is {} and i am from {}"
country = "India"
name = "Tirthesh"

print(letter.format(name, country))
print(f"hey my name is {name} and i am from {country}")
price = 49.032409
txt = f"For only {price:.2f} dollars!"
print(txt)

print(f"{{ {name} }}")