import random
n_questions = int(input("How many questions would you like?"))
count_correct = 0

for i in range(n_questions):
    print(f"Question {i + 1}:")

    n1 = random.randint(1, 9)
    n2 = random.randint(1, 9)
    correct_answer = n1 + n2
    user_answer = int(input(f"{n1} + {n2} = ? "))

    if user_answer == correct_answer:
        print("Correct! :)")
        count_correct = count_correct + 1
    else:
        print("Incorrect! :(")
        print("Correct answer is", correct_answer)

    print("--------------------")

print(f"You answered {count_correct} out of {n_questions} questions correctly.")

