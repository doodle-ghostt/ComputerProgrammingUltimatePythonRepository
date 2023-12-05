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
    if count != 0:
        total = total / count
        return total
    

print("AVERAGE ACT")
print(average_act_score([20, 18, 32, 60, 29, 101, 0]))

def all_true(Booleans):
    for boolean in Booleans:
        if boolean == False:
            return False
    return True
print("ALL TRUE")
print(all_true([True, True, True, True, True]))
print(all_true([True, False, True, True, True]))
print(all_true([True, True, True, True, False]))
print(all_true([False, True, True, True, True]))
print(all_true([False, False, False, False]))

def any_true(booleans):
    for boolean in booleans:
        if boolean == True:
            return True
    return False
print("ANY TRUE")
print(any_true([True, False, False]))
print(any_true([False, False, False]))
print(any_true([False, False, True]))

def mostly_true(booleans):
    count_true = 0
    count_false = 0
    for boolean in booleans:
        if boolean == True:
            count_true = count_true + 1
        else:
            count_false =  count_false + 1
    if count_true > count_false:
        return True
    else:
        return False
print("MOSTLY TRUE")
print(mostly_true([True, False, False]))
print(mostly_true([False, False, False]))
print(mostly_true([False, True, True]))

def has_vowel(characters):
    for character in characters:
        if character in ["a", "e", "i", "o", "u"]:
            return True
    return False
print("HAS VOWEL")
print(has_vowel(["a", "b", "n", "b", "b" ]))
print(has_vowel(["k", "b", "n", "b", "b" ]))
print(has_vowel(["f", "b", "n", "u", "b" ]))
print(has_vowel(["e", "s", "o", "i", "a" ]))

def all_the_same(ints):
    goal = ints[0]
    for int in ints:
        if int != goal:
            return False
    return True

def increasing(ints):
    prev = ints[0]
    for current in ints[1:]:
        if current <= prev:
            return False
        else:
            prev = current
    return True

def is_incrementing(ints):
    prev = ints[0]
    for int in ints[1:]:
        if int - prev != 1: 
            return False
        else:
            prev = int
    return True

def has_adjacent_repeat(list1):
    prev = list1[0]
    for num in list1[1:]:
        if num == prev:
            return True
        else:
            prev = num
    return False

def sum_with_skips(list1):
    skip = False
    total = 0
    for num in list1:
        if num == -1 and skip == False:
            skip = True
        elif num == -1 and skip == True:
            skip = False
        elif skip == False:
            total = total + num
    return total