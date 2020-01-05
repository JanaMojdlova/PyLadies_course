from random import choice
import gallows_functions


list_of_words = ["python", "liska", "uzovka", "pulnoc", "buvol"]

word_to_find = choice(list_of_words)

# DOTAZ - mají být tyto dvě proměnné tvořené funkcí, když se neopakují?
field = gallows_functions.create_empty_field(word_to_find)
word_field = gallows_functions.create_field(word_to_find)

count_incorrect_guessing = 0

while "-" in field:
    gallows_functions.print_field(field)
    letter = gallows_functions.get_a_letter()
    if letter in word_field:
        gallows_functions.replace_character(letter, field, word_field)
    else:
        count_incorrect_guessing = count_incorrect_guessing + 1
        gallows_functions.draw_gallows(count_incorrect_guessing)
        if count_incorrect_guessing == 19:
            print("You lost, try again!")
            break

