import time
import doctest


def grammar_questions():
    """
    Return a dictionary that contains all the questions used for the grammar quiz.

    :return: a dictionary that contains all the questions used for the grammar quiz.
    """
    # Questions taken from https://www.esl-lounge.com/student/grammar-exercises-beginner.php
    question_options = {"capitals": {"description": "Find and type in the word that is not properly capitalized (either missing a capital "
                        "where there should be one, or containing a capital letter that should not be there.)",
                                     "questions": {"We can go and visit you in the Autumn, possibly September but definitely before Christmas.":
                                                   "autumn", "Go and see dr. Cyril Rogers. He's our doctor and the best doctor in the city.": "dr",
                                                   "My brother goes to University in a small town in Scotland. Near Glasgow, I think.": "university",
                                                   "When I finish this novel called \"simplicity\" you can read it.": "simplicity",
                                                   "There was lots of food at the picnic. Apples, Bananas and a big chicken.": "bananas",
                                                   "I work at the Apple Store in the iPhone department. My boss is swedish and it's very interesting.": "swedish",
                                                   "Is that your mercedes in the car park? I have a small Japanese car. I can't remember its name.": "mercedes",
                                                   "My sister studies history at college and wants to work in a museum.": "history"}},
                        "verbs": {"description": "Decide whether the verb conjugation in the following sentences is correct or incorrect by entering 1 or 2.",
                                                 "questions": {"I came to see if you are tired.": "Correct", "She wants you to go and pay for it.": "Correct",
                                                               "I hope seeing you next time you visit.": "Incorrect", "It stopped to rain an hour ago.": "Incorrect",
                                                               "My sister convinced me to give up smoking.": "Correct", "Would you like dancing to this next song?": "Incorrect",
                                                               "Your aunt should eat less sugary foods.": "Correct", "The President decided explaining his decision on TV.": "Incorrect"}},
                        "present simple mc": {"description": "Choose the option that completes the sentence in a grammatically correct way by entering the corresponding number.",
                                                             "questions": {"She ________ in Florida but prefers California.": ["lives", ("lives", "goes", "arrives")],
                                                                           "When we ________ on vacation, we never fly.": ["go", ("are", "go", "went")],
                                                                           "I ________ four languages, but I love Italian the most.": ["speak", ("talk", "speak", "talks")],
                                                                           "That dog always ________ with his head against the wall.": ["sleeps", ("goes", "barks", "sleeps")],
                                                                           "We don't ________ which airport the plane goes from.": ["know", ("know", "think", "like")],
                                                                           "My girlfriend ________ her eyes when there's a horror movie on TV.": ["closes", ("open", "shut", "closes")],
                                                                           "Kathy always ________ about the boss. She hates her job!": ["complains", ("says", "tells", "complains")],
                                                                           "She ________ to disco music, only tango.": ["doesn't dance", ("no listen", "doesn't like", "doesn't dance")]}}}
    return question_options


def grammar_test():
    """
    Initialize the grammar quiz by allowing the user to input the type of exercise they'd like to do, and launching the
    proper exercise.

    :precondition: the user must input an integer between 1 and 3 when prompted.
    :postcondition: the function will launch the quiz of the users choice.
    :raise: ValueError, if the user's input is anything other than an integer between 1 and 3.
    """
    try:
        test_type_input = int(input("""\nWould you like to test your knowledge of proper use of capitals, general verb conjugation or present simple verb conjugation?
                         1. Capitalization
                         2. General Verb Conjugation
                         3. Present simple verb conjugation\n\nPlease enter a number between 1-3 to continue.\n"""))
    except ValueError:
        print("Invalid input. Please ensure you enter a number between 1-3.")
        time.sleep(1)
        grammar_test()
    else:
        test_type = ["capitals", "verbs", "present simple mc"]
        question_source = grammar_questions()
        chosen_test = test_type[test_type_input - 1]
        run_test(question_source, chosen_test)


def run_test(question_bank, test):
    """
    Run the quiz by asking the user each question from the test bank for the activity they chose, and grading their answers.

    :param question_bank: a dictionary which contains all the questions to be used for the quiz, as well as the answers.
    :param test: a string which specifies the type of activity the user has selected.
    :precondition: users must only enter valid values for their answers to the questions, as indicated in the prompts.
    :precondition: the function will continue to ask questions and mark users until it has gone through all of the questions.

    """
    questions = question_bank[test]["questions"].keys()  # gets the list of questions for this activity
    score = 0  # initial score
    test_description = question_bank[test]["description"]  # gets the description/brief instructions of the activity
    print("\n{}\n".format(test_description))  # prints the test description
    for n, question in enumerate(questions, 1):
        print('%d. %s' % (n, question))  # prints the question and question number
        if test == "verbs":  # if the test is a verb conjugation test, it prints out the two options: correct and incorrect
            print("""   1. Correct\n   2. Incorrect""")
        elif test == "present simple mc":  # if the user is doing the present simple test, the three MC options are printed to the user
            for num, answer in enumerate(question_bank[test]["questions"][question][1], 1):
                print('     %d. %s' % (num, answer))
        user_answer = input().strip().lower()  # cleans up the input
        user_answer = remove_punctuation(user_answer)  # removes all punctuation from the input
        if test == "capitals":  # selects the appropriate 'grading' function depending on what type of quiz it is
            score += check_answer_capitals(question_bank, question, user_answer)
        elif test == "verbs":
            score += check_answer_verbs(question_bank, question, user_answer)
        else:
            score += check_answer_present_simple(question_bank, question, user_answer)
    possible_score = len(question_bank[test]["questions"].keys())  # determines the highest possible score for that quiz
    print(f"Your final score was {score} out of a possible {possible_score}.")  # prints the user's actual score and the highest possible score.


def remove_punctuation(answer):
    """
    Remove all punctuation from the string 'answer' and return 'answer' with all punctuation removed
    :param answer: a string, from which all punctuation will be removed
    :return: 'answer,' a version of the string 'answer' with all punctuation removed

    >>> remove_punctuation("Dr.")
    'Dr'
    >>> remove_punctuation("hello_")
    'hello'
    """
    punctuation = ',.~!@#$%^&*()_+-={}[]|/<>:’\“;\"\'\n'
    for marker in punctuation:
        if marker in answer:
            answer = answer.replace(marker, "")
    return answer


def check_answer_capitals(question_source, question, answer):
    """
    Checks the answer if the user is doing a capitalization quiz.

    :param question_source: a dictionary which contains the questions referenced for the quiz.
    :param question: a string, the question whose answer is currently being 'graded'.
    :param answer: a string, the answer the user has given to be 'graded'.
    :return: the score for that question, an integer.
    """
    score = 0
    correct_answer = question_source["capitals"]["questions"][question]  # retrieves the correct answer
    if answer == correct_answer:
        print("Correct!\n")
        time.sleep(1)
        score += 1
    else:
        print(f"Wrong answer.The correct answer is {correct_answer}.\n")
        time.sleep(1)
    return score


def check_answer_verbs(question_source, question, answer):
    """
    Checks the answer if the user is doing a verb conjugation quiz.

    :param question_source: a dictionary which contains the questions referenced for the quiz.
    :param question: a string, the question whose answer is currently being 'graded'.
    :param answer: a string, the answer the user has given to be 'graded'.
    :return: the score for that question, an integer.
    """
    score = 0
    possible_answers = ["Correct", "Incorrect"]
    correct_answer = question_source["verbs"]["questions"][question]  # retrieves the correct answer
    try:  # code that could raise a Value Error
        answer = int(answer)
        if answer != 1 and answer != 2:
            raise ValueError
    except ValueError:  # excepts the error
        print("Invalid input. Please enter either 1 or 2.")
        time.sleep(1)
        answer = input("Enter a valid input.").strip().lower()
        return check_answer_verbs(question_source, question, answer)
    else:
        if possible_answers[answer - 1] == correct_answer:
            print("Correct!\n")
            time.sleep(1)
            score += 1
        else:
            print(f"Wrong answer. The correct answer was {correct_answer}.\n")
            time.sleep(1)
        return score


def check_answer_present_simple(question_source, question, answer):
    """
    Checks the answer if the user is doing a present simple quiz.

    :param question_source: a dictionary which contains the questions referenced for the quiz.
    :param question: a string, the question whose answer is currently being 'graded'
    :param answer: a string, the answer the user has given to be 'graded'
    :return: the score for that question, an integer.
    """
    score = 0
    correct_answer = question_source["present simple mc"]["questions"][question][0]
    try:  # code that could raise a Value Error
        if answer != "1" and answer != "2" and answer != "3":
            raise ValueError
    except ValueError:
        print("Invalid input. Input must be a number between 1 and 3.\n")
        answer = input("Enter a valid input.\n").strip().lower()
        return check_answer_present_simple(question_source, question, answer)
    else:
        if question_source["present simple mc"]["questions"][question][1][int(answer) - 1] == correct_answer:
            print("Correct!\n")
            time.sleep(1)
            score += 1
        else:
            print(f"Wrong answer. The correct answer was {correct_answer}.\n")
            time.sleep(1)
        return score


def main():
    grammar_test()


if __name__ == "__main__":
    doctest.testmod()
