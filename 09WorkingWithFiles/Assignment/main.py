import csv
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

f = open("../data/4000-most-common-english-words.csv", "r")
words = csv.reader(f)

def most_vowels(wordlist):
    most_vowels = ""
    prev_vowel_count = 0
    current_vowel_count = 0
    for row in wordlist:
        for word in row:
            for letter in word:
                if letter in "aeiou":
                    current_vowel_count += 1
            if current_vowel_count > prev_vowel_count:
                most_vowels = word
                prev_vowel_count = current_vowel_count
            current_vowel_count = 0
    return most_vowels

def average_word_length(wordlist):
    letter_count = 0
    word_count = 0
    for row in wordlist:
        for word in row:
            word_count += 1
            for letter in word:
                letter_count += 1
    return round(letter_count/word_count)

f = open("../data/gradebook_data.csv", "r")
reader = csv.reader(f)

def grade_counter(gradebook): 
    a = 0
    b = 0
    c = 0
    d = 0
    f = 0
    for row in reader:
        name, gradelevel, grade = row
        if int(grade) >= 90:
            a += 1
        elif int(grade) >= 80:
            b += 1
        elif int(grade) >= 70:
            c += 1
        elif int(grade) >= 60:
            d += 1
        else:
            f += 1
    return a, b, c, d, f


def average_grades(gradebook):
    freshmen_average = 0
    freshmen_total = 0
    sophomore_average = 0
    sophomore_total = 0
    junior_average = 0
    junior_total = 0
    senior_average = 0
    senior_total = 0
    
    for row in reader:
        name, gradelevel, percent = row
        if int(gradelevel) == 9:
            freshmen_average += int(percent)
            freshmen_total += 1
        elif int(gradelevel) == 10:
            sophomore_average += int(percent)
            sophomore_total += 1 
        elif int(gradelevel) == 11:
            junior_average += int(percent)
            junior_total += 1
        elif int(gradelevel) == 12:
            senior_average += int(percent)
            senior_total += 1     
    return freshmen_average/freshmen_total, sophomore_average/sophomore_total, junior_average/junior_total, senior_average/senior_total
print(average_grades(reader))
