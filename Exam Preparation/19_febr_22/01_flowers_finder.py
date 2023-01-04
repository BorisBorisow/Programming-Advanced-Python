from collections import deque
import re

searched_words = {"rose": "rose",
                  "tulip": "tulip",
                  "lotus": "lotus",
                  "daffodil": "daffodil"}

vowels = deque(input().split())
consonant = input().split()
found_word = False

while vowels and consonant:
    current_vowel = vowels.popleft()
    current_consonant = consonant.pop()
    for value in searched_words.keys():
        if current_consonant or current_vowel in value:
            searched_words[value] = searched_words[value].replace(current_consonant, "")
            searched_words[value] = searched_words[value].replace(current_vowel, "")

        if len(searched_words[value]) == 0:
        #if searched_words[value] == "":
            print(f"Word found: {value}")
            found_word = True

    if found_word:
        break

if not found_word:
    print("Cannot find any word!")
if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonant:
    print(f"Consonants left: {' '.join(consonant)}")
