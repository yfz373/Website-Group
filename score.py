def my_score (score) :

    if score > 100 :
        grade = "Excellent!"
    elif score > 59 and score < 100 :
        grade = "You Pass"
    else :
        grade = "You Fail!"
    return grade

myscore = my_score (56)
print(myscore)

hisscore = my_score (78)
print(hisscore)