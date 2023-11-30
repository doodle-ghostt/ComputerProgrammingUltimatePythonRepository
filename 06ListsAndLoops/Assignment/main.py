def count_failing_grades(grades):
    count = 0
    for grade in grades:
        if grade < 60:
            count = count + 1
    return count

print("COUNT FAILING")
print(count_failing_grades([20, 85, 90, 46, 60, 59, 101]))

def count_act_scores(scores):
    count = 0
    for score in scores:
        if score >= 1 and score <= 36:
            count = count + 1
    return count

print("COUNT ACT")
print(count_act_scores([20, 18, 32, 60, 29, 101, 0]))

def number_sum(list):
    count = 0
    for number in list:
        count = count + number
    return count

print("NUMBER SUM")
print(number_sum([1, 2, 3, 4]))

def average_act_score(list):
    total = 0
    count = 0
    for score in list:
        if score  >= 1 and score <= 36:
            count  = count + 1
            total  = total + score
    total = total / count
    return total

print("AVERAGE ACT")
print(average_act_score([20, 18, 32, 60, 29, 101, 0]))