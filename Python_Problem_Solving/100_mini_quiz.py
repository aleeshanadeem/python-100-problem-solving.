questions = [
    {
        "question": "What is the capital of Pakistan?",
        "answer": "Islamabad"
    },
    {
        "question": "What is 5 + 3?",
        "answer": "8"
    },
    {
        "question": "Which language are we learning?",
        "answer": "Python"
    },
    {
        "question": "How many days are in a week?",
        "answer": "7"
    },
    {
        "question": "What keyword creates a function in Python?",
        "answer": "def"
    }
]

score = 0

for item in questions:
    print("\n" + item["question"])

    answer = input("Your answer: ")

    if answer.strip().lower() == item["answer"].lower():
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
        print("Correct answer:", item["answer"])

print("\n--- Quiz Finished ---")
print("Your Score:", score, "/", len(questions))