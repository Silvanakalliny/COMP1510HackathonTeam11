import requests
import random
import re
import itertools
from vocabulary import Vocabulary
import doctest
import time
import json
import requests



def study_time(func) -> float:
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
    vocabulary = Vocabulary()

    running = True
    while running:
        menu_list = ["Check a word", "Add a word", "Add words",
                     "Remove a word", "Remove words",
                     "Print the word list", "Print the word list with definition",
                     "Test your vocabulary", "Test your grammar"]

        choice = user_input(menu_list,
                            "Welcome to Learn English App!",
                            "What would you like to do (Type 'quit' to exit the application): ")

        if choice == "quit":
            running = False
        elif choice == "1":
            pass
        elif choice == "2":
            new_word = input("Add a new word: ")
            vocabulary.add_a_word(new_word)
        elif choice == "3":
            new_words = input("Add new words (separate by commas): ")
            vocabulary.add_words(new_words)
        elif choice == "4":
            delete_word = input("Remove a word: ")
            vocabulary.remove_a_word(delete_word)
        elif choice == "5":
            words = input("Enter the words you would like to remove (separate by commas): ")
            vocabulary.remove_words(words)
        elif choice == "6":
            if len(vocabulary.sort_words()) == 0:
                print("\nYour list is empty! Add some words to your list first!")
            else:
                print("\nHere is your word list")
                print_list(vocabulary.sort_words())
            pass
        elif choice == "7":
            pass
        elif choice == "8":
            try:
                test_yourself(vocabulary)
            except IndexError:
                print("The question list is Empty")


def print_list(word_list):
    app_id = "a102c50a"
    api_key = "02d554c4537100778aa8e303c11c438a"
    for i, word in enumerate(word_list, 1):
        url = f"https://od-api.oxforddictionaries.com/api/v2/entries/en/{word}"
        response = requests.get(url, headers={"app_id": app_id, "app_key": api_key})
        word_data = json.loads(response.text)
        definition = word_data["results"][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0]
        print("%d. %s: %s" % (i, word.title(), definition))


def user_input(item_list, result, input_string) -> str:
    print("\n" + "-" * 50)
    print("\n%s\n" % result)
    print_list(item_list)
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
        response = requests.get(f"https://od-api.oxforddictionaries.com/api/v2/entrie" +
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
    except requests.exceptions.HTTPError:
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
    number_of_question = itertools.count(1)
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
    regex_word = re.compile(f"^{word}$")
    match_word = regex_word.search(answer)
    # Return True if the answer is correct else False
    return True if match_word else False


