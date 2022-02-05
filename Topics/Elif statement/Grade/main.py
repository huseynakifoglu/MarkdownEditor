student_score = int(input())
max_score = int(input())

score_ratio = 100 * student_score / max_score
# print("Score is "+str(score_ratio))
if score_ratio < 60:
    print("F")
elif 69.9 >= score_ratio >= 60:
    print("D")
elif 79.9 > score_ratio >= 70:
    print("C")
elif 89.9 >= score_ratio >= 79.9:
    print("B")
elif 100 >= score_ratio >= 90:
    print("A")
