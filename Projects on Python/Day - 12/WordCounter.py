import string

sentence = input("Enter a sentence: ")

# Convert to uppercase
sentence = sentence.upper()

# Remove punctuation
for char in string.punctuation:
    sentence = sentence.replace(char, "")

# Split into words
words = sentence.split()

# Count occurrences
count = {}

for word in words:
    if word not in count:
        count[word] = 1
    else:
        count[word] += 1

print(count)