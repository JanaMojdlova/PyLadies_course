from random import choice

questions_list = ["Who? ", "With whom? ", "What? ", "Where? ", "When? ", "How? ", "Why? "]
words = [] 

for question in range(len(questions_list)):
    # first answer to the list of answers
    answers_list = []
    answer = input(questions_list[question])
    answers_list.append(answer)
    # next answers to the list of answers
    while True:
        repetition = input("Do you want to add another answer to this question? (yes/no) ")
        if repetition.lower() == "yes":
            response = input(questions_list[question])
            answers_list.append(response)
        elif repetition.lower() == "no":
            break
        else:
            print("I do not understand. Yes or no? ")
    # random choice of answer to the final list 
    words.append(choice(answers_list))

# print of the answers in whole sentence
for i in range(len(words)): 
    print(words[i])

 

   