scores = input().split()

# put your python code here
# print(scores)
incorrect_answers, correct_answers = 0, 0


def score_counter(answers):
    global incorrect_answers, correct_answers

    for i in answers:
        # if element is incorrect then increase number of incorrect answers
        if i == "I":
            incorrect_answers += 1

        # if element is correct then increase number of correct answers
        elif i == "C":
            correct_answers += 1
        if incorrect_answers == 3:
            break


# Run score counter function to count correct and incorrect answers
score_counter(scores)
if incorrect_answers < 3:
    print("You won")
    print(correct_answers)
else:
    print("Game over")
    print(correct_answers)
