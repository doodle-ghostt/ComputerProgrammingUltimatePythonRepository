import csv
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
#f = open(r'09WorkingWithFiles\data\4000-most-common-english-words.csv', "r")
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

most_vowels(words)