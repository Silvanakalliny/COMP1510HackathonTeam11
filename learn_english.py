import random
import re
import itertools
from vocabulary import Vocabulary
from grammar import grammar_test
import doctest
import time
import requests


def study_time(func) -> float:  # DECORATOR
    """
    Times the runtime of a function.

    :param func: the function to be timed
    :return: the run time, in seconds
    """
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        hours = int(run_time // 3600)
        minutes = int(run_time % 3600 // 60)
        seconds = int(run_time % 3600 % 60)
        print(f"You studied for {hours} hours, {minutes} minutes and {seconds} seconds.")
        return run_time  # removed {func.__name__!r} from above, may use it later to state lesson name or something
    return wrapper_timer


@study_time
def main():
    """
    Drives the program.

    """

    vocabulary = Vocabulary()

    running = True
    while running:  # LOOPING
        menu_list = ["Check a word", "Add a word", "Add words",
                     "Remove a word", "Remove words",
                     "Print the word list", "Print the word list with definition",
                     "Test your vocabulary", "Test your grammar"]  # DATA STRUCTURE - LIST

        choice = user_input(menu_list,
                            "Welcome to Learn English App!",
                            "What would you like to do (Type 'quit' to exit the application): ")

        if choice == "quit":
            running = False
        elif choice == "1":
            the_word = input("What word you want to check? : ")
            check_dictionary(vocabulary, the_word)
        elif choice == "2":
            new_word = input("Add a new word: ")
            vocabulary.add_a_word(new_word)
            if new_word.strip() == "":
                print("Error. Your word only contains whitespace.")
        elif choice == "3":
            new_words = input("Add new words (separate by commas): ")
            vocabulary.add_words(new_words)
        elif choice == "4":
            try:                 # ERROR HANDLING - TRY EXCEPT
                delete_word = input("Remove a word: ")
                vocabulary.remove_a_word(delete_word)
            except KeyError:
                print("Error: That word is not in the vocabulary.")
        elif choice == "5":
            try:
                words = input("Enter the words you would like to remove (separate by commas): ")
                vocabulary.remove_words(words)
            except KeyError:
                print("Error: One or more of your words are not in the vocabulary.")
        elif choice == "6":
            if len(vocabulary.sort_words()) == 0:
                print("\nYour list is empty! Add some words to your list first!")
            else:
                print("\nHere is your word list")
                print_lists(vocabulary.sort_words())
        elif choice == "7":
            if len(vocabulary.sort_words()) == 0:
                print("\nYour list is empty! Add some words to your list first!")
            else:
                print("\nHere is your word list with definition")
                print_list_with_definition(vocabulary.sort_words())
        elif choice == "8":
            try:
                test_yourself(vocabulary)
            except IndexError:
                print("The question list is Empty")
        elif choice == "9":
            grammar_test()


def print_list_with_definition(word_list: list):
    """
    Prints each word in the word list along with its definition.

    :param word_list: a list of words to be printed.
    """
    word_and_definition = {word: definition_and_example(word)[0] for word in word_list}  # DICTIONARY COMPREHENSION
    for num, (word, definition) in enumerate(word_and_definition.items(), 1):  # ENUMERATE FUNCTION
        print("%d. %s: %s" % (num, word.title(), definition))


def print_lists(a_list: list):
    """
    format a list in vertical with number assigning to each item

    pattern matching: print out a listed in the vertical format is repeated
    automating with algorithm: using for loop to print out each item in a list
    :param a_list: a list
    precondition: must be a list
    postcondition: enumerates the list and print the list vertically
    :return: returns a formatted list

    """
    # enumerate through a list of items and number them
    for n in range(len(a_list)):  # RANGE FUNCTION
        print("%d. %s" % (n+1, a_list[n]))


def user_input(item_list: list, result: str, input_string: str) -> str:
    """
    Prints in the format of dotted line, a message, the item list and returns a prompt

    pattern matching: use pattern matching for multiple print statement is in the same format
    :param item_list: a list
    :param result: a string that informs the user
    :param input_string: a string for prompting the user
    :return: return input_string as a prompt
    """

    # Dotted line for separating each print
    print("\n" + "-" * 50)
    print("\n%s\n" % result)
    print_lists(item_list)
    return input("\n%s" % input_string).strip()


def definition_and_example(word: str) -> tuple or str:
    """
    Return the definition and an example of the word.

    Computational thinking: I used Algorithms and Automation to automatically call a request from dictionary API.
    :precondition: must be a string has a meaning
    :postcondition: return the definition and an example sentence of the word
    :raise requests.exceptions.HTTPError: if the word is not in the dictionary
    :param word: must be a string has a meaning
    :return: the definition and an example sentence of the word

    Can't do doctest and unittest because it's API related
    """
    # ID and KEY are needed for authentication
    my_id = "67421323"
    my_key = "427d2d5a8f8aab43d83284acf09cfa3f"
    # try making requests to the API
    try:
        response = requests.get(f"https://od-api.oxforddictionaries.com/api/v2/entrie" +    # API
                                f"s/en-us/{word}", headers={'app_id': my_id, 'app_key': my_key})
        response.raise_for_status()
        # Get access to the word's definition and example
        access_word_information = response.json()['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]
        # Get access to the definition
        definition = access_word_information['definitions'][0]
        # Get access to the example
        an_example = access_word_information['examples'][0]['text']
        # Return the definition and the example
        return definition, an_example
    # Catch the Error if the word dose not exist and return a helping message
    except (requests.exceptions.HTTPError, KeyError):
        help_message = "!!! There is no such a word"
        return help_message


def test_yourself(user_class: Vocabulary):
    """
    Test the user with his or her vocabulary

    Computational thinking: I used Decomposition to break the task down to smaller tasks
    :precondition: user_class must be a vocabulary
    :postcondition: test the user's vocabulary by words in the user's vocabulary sheet
    :raise AttributeError: if the parameter is not a vocabulary
    :param user_class: must be a vocabulary
    :return: A test to test the user's vocabulary

    Can't do doctest and unittest because it's API related
    """
    # Make a counter of the number of question
    number_of_question = itertools.count(1)  # ITERTOOLS
    # Make a new list of vocabulary sheet as the question list
    question_list = user_class.sort_words()
    # Keep looping until the user stops the test
    while True:
        # Print the definition and an example of the a random word and return the word
        the_word = print_word_information(question_list, next(number_of_question))
        # Ask the user to type his or her answer
        user_answer = input("Your Answer (type '0' to quit the test): ").strip().lower()
        # Type 0 to stop the test
        if user_answer == "0":
            break
        # If the answer is correct
        if regex_check(the_word, user_answer):
            # Remove the word from the question list to prevent it shows again
            question_list.remove(the_word)
            # Ask the user if he or her wants to delete the word from the vocabulary sheet
            delete_or_not = input(f"Delete \"{the_word}\" from your vocabulary sheet? ('Y'-yes. press 'Enter' to pass)")
            # Delete the word from the vocabulary sheet
            if delete_or_not.strip().lower() == "y":
                user_class.remove_a_word(the_word)
        # If the answer is wrong, tell the user
        else:
            print(f"Wrong. The answer is {the_word}\n")


def print_word_information(question_list: list, question_number: int) -> str:
    """
    Return the information of a randomly picked word.

    Computational thinking: I used Pattern Matching to find the similarity between information I wanted
    :precondition: question_list must be a list with strings, question_number must be a positive integer
    :postcondition: return the information of a randomly picked word
    :param question_list: must be a list with strings
    :param question_number: must be a positive integer
    :return: a randomly picked word from the question list

    Can't do doctest and unittest because it's API related
    """
    # Randomly pick a word from the question list
    the_word = random.choice(question_list)
    # Seek the example sentence of the word
    example_sentence = definition_and_example(the_word)[1].replace(the_word, "________")
    # Print the question number, definition, and example sentence of the word
    print(f"{question_number}. Definition: {definition_and_example(the_word)[0]}\n"
          f"   Example:{example_sentence}")
    # Return the word
    return the_word


def regex_check(word: str, answer: str) -> bool:
    """
    Check if the answer is correct.

    Computational thinking: I used Item Matching to match the word by using regular expression.
    :precondition: both parameters must be strings
    :postcondition: Check if the user input matches the word
    :param word: must be a string
    :param answer: must be a string
    :raise TypeError: if any of both parameters are not a string
    :return: True if matches else False

    >>> regex_check('', '')
    True
    >>> regex_check(' ', ' ')
    True
    >>> regex_check('1', '1')
    True
    >>> regex_check('True', 'True')
    True
    >>> regex_check('True', 'ture')
    False
    """
    # Check the answer with regular expression
    regex_word = re.compile(f"^{word}$")  # REGEX
    match_word = regex_word.search(answer)
    # Return True if the answer is correct else False
    return True if match_word else False


def check_dictionary(user_class: Vocabulary, word: str):
    """
    Check the definition and example of the word by dictionary API

    Computational thinking: I used Decomposition to breakdown the user action into smaller tasks
    :precondition: user_class must be a Vocabulary class, the word must be a string has a meaning
    :postcondition: print the definition and an example of the word
    :raise KeyError, HTTPError: if the word doesn't have an definition and example, or the word doesn't exist
    :param user_class: must be a Vocabulary Class
    :param word: must be a string that has a meaning
    :return: the definition and an example of the word

    Can't do doctest and unittest because it's API related
    """
    # Get the definition and example
    definition = definition_and_example(word)[0]
    example_sentence = definition_and_example(word)[1]
    # Print the definition and example of the word
    print(f"----    {word}    ----\n"
          f"Definition: {definition}\n"
          f"Example: {example_sentence}\n")

    if definition == "!":
        print("This is not a word in the dictionary!")
    else:
        # If the word is not in the vocabulary sheet
        if word not in user_class.sort_words():
            # Ask the user if the user wants to add the word to the vocabulary sheet
            user_choice = input(f"Do you want to add \'{word}\' into you vocabulary? ('Y' to add, 'N' pass):")
            # If yes, add the word to the vocabulary sheet
            if user_choice.strip().lower() == 'y':
                user_class.add_a_word(word)


if __name__ == '__main__':
    main()

