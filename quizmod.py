def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1
    for key in questions:
        print("----------------")
        print(key)
        for i in options[question_num - 1]:
            print(i)
        guess = input("enter A, B, C, or D: ").upper()
        guesses.append(guess)
        correct_guesses += check_answers(questions.get(key), guess, correct_guesses, questions)
        question_num += 1

    display_score(correct_guesses, question_num, guesses)  # Pass question_num as well
    play_again()


def check_answers(answer, guess, correct_guesses, questions):
    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("Wrong!")
        return 0


def display_score(correct_guesses, question_num, guesses):
    print("----------------")
    print("RESULTS!!")
    print("----------------")
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()
    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()
    score = ((correct_guesses / question_num) * 100)
    print("Your score is: " + str(score) + "%")


def play_again():
    response = input("Do you want to play again? (yes or no): ")
    if response == "yes":
        return new_game()
    else:
        print("Thanks for playing! Goodbye!")


questions = {
    "What is the capital of France?": "A",
    "What is the capital of Germany?": "B",
    "What is the capital of Spain?": "C",
    "What is the capital of Italy?": "D",
    "What is the capital of the UK?": "A",
    "What is the capital of the USA?": "D",
    "What is the capital of Canada?": "A",
    "What is the capital of Australia?": "C",
    "What is the capital of Japan?": "D",
    "What is the capital of China?": "B",
}

options = [
    ["A) Paris", "B) Berlin", "C) Madrid", "D) Rome"],  # France - A
    ["A) Berlin", "B) Paris", "C) Madrid", "D) Rome"],  # Germany - B
    ["A) Madrid", "B) Berlin", "C) Paris", "D) Rome"],  # Spain - C (correction)
    ["A) Madrid", "B) Berlin", "C) Rome", "D) Paris"],  # Italy - D
    ["A) London", "B) Berlin", "C) Madrid", "D) Paris"],  # UK - A
    ["A) Washington", "B) Berlin", "C) Madrid", "D) Paris"],  # USA - D
    ["A) Ottawa", "B) Berlin", "C) Madrid", "D) Paris"],  # Canada - A
    ["A) Canberra", "B) Berlin", "C) Madrid", "D) Paris"],  # Australia - C
    ["A) Tokyo", "B) Berlin", "C) Madrid", "D) Paris"],  # Japan - D
    ["A) Beijing", "B) Berlin", "C) Madrid", "D) Paris"],  # China - B (correction)
]

new_game()
