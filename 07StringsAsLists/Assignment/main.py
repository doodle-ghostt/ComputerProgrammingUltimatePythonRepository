def is_alliteration(word1, word2):
    if word1[0] == word2[0]:
        return True
    else:
        return False
    
def count_vowels(word):
    count = 0
    for letter in word:
        if letter in "aeiou":
            count += 1
    return count

def count_numbers(string):
    count = 0
    for char in string:
        if char in "1234567890":
            count += 1
    return count

def count_target_letters(word, target):
    count = 0
    for letter in word:
        if target == letter:
            count += 1
    return count

def in_alphabetical_order(word):
    if len(word) != 0:
        prev = word[0]
        for letter in word[1:]:
            if letter < prev:
                return False
    return True

def alternate_case(string):
    result = ""
    is_upper = False
    for letter in string:
        if is_upper == False:
            result += (letter).upper
            is_upper = True
        if is_upper == True:
            result += (letter).lower
    return result

def remove_vowels(string):
    result = ""
    for letter in string:
        if letter in "aeiou":
            pass
        else:
            result += letter
    return result

def to_camel_case(string):
    result = ""
    is_upper = False
    for letter in string:
        if letter == " ":
            is_upper = True
        elif is_upper == True:
            result += (letter).upper
        else:
            result += letter
    return result

def to_snake_case(string):
    result = ""
    for letter in string:
        if letter == " ":
            result += "_"
        else:
            result += letter
    return result

def without_duplicates(list1):
    prev = list1[0]
    result = list1[0]
    for number in list1[1:]:
        if number != prev:
            result.append(number)
            prev = number
        else:
            prev = number
    return result

def filter_valid_act_score(scores):
    result = []
    for score in scores:
        if score <= 36 and score >= 1:
            result.append(score)
    return result