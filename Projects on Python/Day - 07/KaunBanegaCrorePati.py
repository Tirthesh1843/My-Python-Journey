#kaun banega crorepati game
print("Welcome to Kaun Banega Crorepati!")

questions = [
    "Which planet is known as the Red Planet?",
    "Who is known as the Father of the Indian Constitution?",
    "What is the capital of Gujarat?",
    "Which data structure follows the LIFO principle?",
    "Who wrote the Indian national anthem 'Jana Gana Mana'?",
    "What is the chemical symbol for Gold?",
    "Which programming language is primarily used for data science and AI?",
    "Which is the largest ocean on Earth?",
    "In which year did India gain independence?",
    "What does CPU stand for?",
    "Which Indian mission successfully landed near the Moon's south pole in 2023?",
    "Who developed the theory of relativity?",
    "What is the time complexity of binary search?",
    "Which country has won the most Men's ODI Cricket World Cups?",
    "Which company originally created the Java programming language?",
    "Which mathematician proposed the theorem known as Fermat's Last Theorem?"
]
options = [
    ["Venus", "Mars", "Jupiter", "Saturn"],
    ["Mahatma Gandhi", "Jawaharlal Nehru", "Dr. B. R. Ambedkar", "Sardar Patel"],
    ["Ahmedabad", "Surat", "Gandhinagar", "Rajkot"],
    ["Queue", "Array", "Stack", "Linked List"],
    ["Bankim Chandra Chattopadhyay", "Rabindranath Tagore", "Sarojini Naidu", "Subhas Chandra Bose"],
    ["Ag", "Gd", "Go", "Au"],
    ["COBOL", "Python", "Pascal", "Fortran"],
    ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
    ["1945", "1946", "1947", "1950"],
    ["Central Process Unit", "Computer Processing Unit", "Central Processing Unit", "Core Processing Unit"],
    ["Chandrayaan-1", "Chandrayaan-2", "Mangalyaan", "Chandrayaan-3"],
    ["Isaac Newton", "Galileo Galilei", "Albert Einstein", "Nikola Tesla"],
    ["O(n)", "O(log n)", "O(n²)", "O(1)"],
    ["India", "Australia", "England", "West Indies"],
    ["Microsoft", "IBM", "Sun Microsystems", "Oracle"],
    ["Leonhard Euler", "Pierre de Fermat", "Carl Gauss", "Rene Descartes"]
]

amounts = [
    "₹1,000",
    "₹2,000",
    "₹3,000",
    "₹5,000",
    "₹10,000",
    "₹20,000",
    "₹40,000",
    "₹80,000",
    "₹1,60,000",
    "₹3,20,000",
    "₹6,40,000",
    "₹12,50,000",
    "₹25,00,000",
    "₹50,00,000",
    "₹1,00,00,000",
    "₹7,00,00,000"
]

correct_answers = [
    "B",  # Mars
    "C",  # Dr. B. R. Ambedkar
    "C",  # Gandhinagar
    "C",  # Stack
    "B",  # Rabindranath Tagore
    "D",  # Au
    "B",  # Python
    "D",  # Pacific Ocean
    "C",  # 1947
    "C",  # Central Processing Unit
    "D",  # Chandrayaan-3
    "C",  # Albert Einstein
    "B",  # O(log n)
    "B",  # Australia
    "C",  # Sun Microsystems
    "B"   # Pierre de Fermat
]
answers = ["A", "B", "C", "D"]
for i in range(len(questions)):
    print("Q.", i+1, questions[i])
    for j in range(4):
        print(answers[j] + ".", options[i][j])
    user_answer = input("Your answer (A/B/C/D): ").upper()
    if user_answer == correct_answers[i]:
        print("Correct! You have won", amounts[i])
    else:
        print("Wrong answer. The correct answer was", correct_answers[i])   
        break

print("Congratulations! You have won", amounts[i])