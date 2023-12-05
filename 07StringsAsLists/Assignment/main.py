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