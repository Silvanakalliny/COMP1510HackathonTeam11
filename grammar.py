
easy = {"capitals": {"description": "Find and type in the word that is not properly capitalized (either missing a capital "
        "where there should be one, or containing a capital letter that should not be there.)",
                     "questions": {"We can go and visit you in the Autumn, possibly September but definitely before Christmas.":
                                    "autumn",
                                   "Go and see dr. Cyril Rogers. He's our doctor and the best doctor in the city.": "dr",
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

medium = {}
hard = {}


def grammar_test():
    difficulty_input = int(input("""Would you like to be tested at a beginner, intermediate or advanced level?
                         1. Beginner
                         2. Intermediate
                         3. Advanced\nPlease enter a number between 1-3 to continue."""))

    test_type_input = int(input("""\nWould you like to test your knowledge of proper use of capitals, general verb conjugation or present simple verb conjugation?
                         1. Capitals
                         2. General Verb Conjugation
                         3. Present simple verb conjugation\nPlease enter a number between 1-3 to continue."""))
    difficulty = [easy, medium, hard]
    test_type = ["capitals", "verbs", "present simple mc"]
    chosen_difficulty = difficulty[difficulty_input - 1]
    chosen_test = test_type[test_type_input - 1]
    score = 0
    run_test(chosen_difficulty, chosen_test, score)
    possible_score = len(chosen_difficulty[chosen_test]["questions"].keys())
    print(f"Your final score was {score} out of a possible {possible_score}.")


def run_test(level, test, score):
    questions = level[test]["questions"].keys()
    test_description = level[test]["description"]
    print("\n{}\n".format(test_description))
    for n, question in enumerate(questions, 1):
        print('%d. %s' % (n, question))
        if test == "verbs":
            print("""   1. Correct\n   2. Incorrect""")
        elif test == "present simple mc":
            for num, answer in enumerate(level[test]["questions"][question][1], 1):
                print('     %d. %s' % (num, answer))
        user_answer = input().strip().lower()
        remove_punctuation(user_answer)
        if test == "capitals":
            check_answer_capitals(level, question, user_answer, score)
        elif test == "verbs":
            check_answer_verbs(level, question, user_answer, score)
        else:
            check_answer_present_simple(level, question, user_answer, score)


def remove_punctuation(answer):
    punctuation = ',.~!@#$%^&*()_+-={}[]|/<>:’\“;\"\'\n'
    for marker in punctuation:
        if marker in answer:
            answer = answer.replace(marker, "")


def check_answer_capitals(level, question, answer, score):
    correct_answer = level["capitals"]["questions"][question]
    if answer == correct_answer:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong answer.The correct answer is {correct_answer}.")


def check_answer_verbs(level, question, answer, score):
    possible_answers = ["Correct", "Incorrect"]
    correct_answer = level["verbs"]["questions"][question]
    answer = int(answer)
    if answer != 1 and answer != 2:
        raise ValueError
    elif possible_answers[answer - 1] == correct_answer:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong answer.The correct answer is {correct_answer}.")


def check_answer_present_simple(level, question, answer, score):
    correct_answer = level["present simple mc"]["questions"][question][0]
    given_answer = level["present simple mc"]["questions"][question][1][int(answer)-1]
    if int(answer) != 1 and int(answer) != 2 and int(answer) != 3:
        raise ValueError
    elif given_answer == correct_answer:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong answer.The correct answer is {correct_answer}.")


grammar_test()