import requests
import random
import re
import itertools
import vocabulary


def main():
    pass


def definition_and_example(word: str) -> tuple or str:
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


def test_yourself(user_class: vocabulary):
    # Make a counter of the number of question
    number_of_question = itertools.count(1)
    # Make a new list of vocabulary sheet as the question list
    question_list = [user_class.sort_words()]
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
                pass
        # If the answer is wrong, tell the user
        else:
            print(f"Wrong. The answer is {the_word}\n")


def print_word_information(question_list: list, question_number: int) -> str:
    # Randomly pick a word from the question list
    the_word = random.choice(question_list)
    # Seek the example sentence of the word
    example_sentence = definition_and_example(the_word)[1].replace(the_word, "________")
    # Print the question number, definition, and example sentence of the word
    print(f"{question_number}. Definition: {definition_and_example(the_word)[0]}\n"
          f"   Example:{example_sentence}")
    # Return the word
    return the_word


def regex_check(word: str, user_input: str) -> bool:
    # Check the answer with regular expression
    regex_word = re.compile(f"^{word}$")
    match_word = regex_word.search(user_input)
    # Return True if the answer is correct else False
    return True if match_word else False
