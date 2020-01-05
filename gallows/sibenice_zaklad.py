from random import choice

# empty field at the beginning = list of "-"
def create_empty_field(word_to_find):
    field = []
    for i in range (len(word_to_find)):
        field.append("-")
    return field

# list of letters in the word
def create_field(word_to_find):
    field = []
    for character in word_to_find:
        field.append(character)
    return field

# printing "pretty" field in one line (not as a list)
def print_field(field):
    for i in field:
        print(i, end="")
    print("")    

# getting a letter from the player
def get_a_letter():
    letter = "0"
    while not letter.isalpha() or len(letter) != 1:
        letter = input("Guess a letter! ")
    return letter

# replacing "-" in the field by correct letter
def replace_character(character, field, word):
    position = word.index(character)
    field[position] = character
    if "-" not in field:
        print("You won, congratulations!")
    return field

# drawing the gallow according to count of wrong guessing
def draw_gallows(count):
    gallows = {1: """
| 
~~~~~~~ """, 2: """
| 
|
~~~~~~~ """, 3: """
|
|
| 
~~~~~~~ """, 4: """
|
|
|
| 
~~~~~~~ """, 5: """
|
|
|
| 
|
~~~~~~~ """, 6: """
+
|
|
|
| 
|
~~~~~~~ """, 7: """
+-
|
|
|
| 
|
~~~~~~~ """, 8: """
+--
|
|
|
| 
|
~~~~~~~ """, 9: """
+---
|
|
|
| 
|
~~~~~~~ """, 10: """
+---.
|
|
|
| 
|
~~~~~~~ """, 11: """
+---.
|   |
|
|
| 
|
~~~~~~~ """, 12: """
+---.
|   |
|   o
|
| 
|
~~~~~~~ """, 13: """
+---.
|   |
|   o
|   |
| 
|
~~~~~~~ """, 14: """
+---.
|   |
|   o
|  -|
| 
|
~~~~~~~ """, 15: """
+---.
|   |
|   o
| --|
| 
|
~~~~~~~ """, 16: """
+---.
|   |
|   o
| --|-
| 
|
~~~~~~~ """, 17: """
+---.
|   |
|   o
| --|--
| 
|
~~~~~~~ """, 18: """
+---.
|   |
|   o
| --|--
|  / 
|
~~~~~~~ """, 19: """
+---.
|   |
|   o
| --|--
|  / \ 
|
~~~~~~~ """}
    print(gallows[count])


list_of_words = ["python", "liska", "uzovka", "pulnoc", "buvol"]

word_to_find = choice(list_of_words)

field = create_empty_field(word_to_find)
word_field = create_field(word_to_find)
count_incorrect_guessing = 0

while "-" in field:
    print_field(field)
    letter = get_a_letter()
    if letter in word_field:
        replace_character(letter, field, word_field)
    else:
        count_incorrect_guessing = count_incorrect_guessing + 1
        draw_gallows(count_incorrect_guessing)
        if count_incorrect_guessing == 19:
            print("You lost, try again!")
            break


""" testy:
1. je zadáno písmeno?
2. vybere správnou šibenici ze seznamu obrázků?
3. kontroluje správně plné pole?
4. vyrobí prázdný seznam?
5. vyrobí seznam z písmen slova?
6. nahradí správně pomlčku za písmeno?
7. počítá správně nesprávné pokusy?
8. co s opakujícími se písmeny?
"""


