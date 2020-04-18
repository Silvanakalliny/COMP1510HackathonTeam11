"""Module containing Vocabulary class and related-functions."""


def word_lister(string):
    string = string.lower()
    word_list = string.split(",")
    for word in word_list:
        if word.strip() == "":
            word_list.remove(word)
    return word_list


def is_valid_word(string: str) -> str:
    """
    Remove all characters from a string except Latin letters and whitespace.

    :param string: a string containing letters and/or spaces
    :precondition: string argument contains words separated by whitespace
    :postcondition: generates a new string containing only letters and whitespace
    :return: refactored string containing only Latin letters and whitespace
    """
    valid_chars = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)] + [' ', ',', "\'"]
    for character in string:
        if character not in valid_chars:
            return False
    return True


class Vocabulary:
    def __init__(self):
        """Initialize a new Vocabulary object."""
        self.__words = set()

    def add_a_word(self, new_word: str):
        """
        Add a word to the words set.

        :param new_word: a string of a valid word
        :precondition: new_word exists in Oxford dictionary API
        :postcondition: word is added to to this instance's __words set
        """
        try:
            if is_valid_word(new_word):
                if new_word.strip() != "":
                    self.__words.add(new_word.lower().strip())
                    print(f"Added {new_word} to word list.")
            else:
                raise ValueError(new_word + " is not a valid word")
        except ValueError as e:
            print(f"Word not added: " + str(e))

    def add_words(self, new_words: str):  # will need to add code in main for splitting input by commas (',')
        """
        Add multiple words to the words set using a string of comma-separated words.

        :param new_words: a string containing words separated by commas
        :precondition: new_words argument is a comma-separated list of valid words
        :postcondition: each word is added to __words set
        """
        whitespace_word = False
        word_list = word_lister(new_words)
        for word in word_list:
            word = word.strip()
            if word != "":
                whitespace_word = True
                self.add_a_word(word)
        if whitespace_word:
            print("Error. One or more of your words are all whitespace.")

    def remove_a_word(self, word: str):
        """
        Remove a specific word from the word set.

        :param word: a string that exists in __words
        :precondition: word argument is in __words
        :postcondition: word is removed from __words set
        """
        print(f"Removing {word} from your word list.")
        self.__words.remove(word.lower().strip())

    def remove_words(self, words: str):
        """
        Remove multiple existing words from the word set.

        :param words: a string containing words separated by commas
        :precondition: words argument is a comma-separated list of valid words
        :postcondition: each word is removed from the __words set
        """
        word_list = word_lister(words)
        for word in word_list:
            self.remove_a_word(word)

    def sort_words(self) -> list:
        """
        Return the words set as a list sorted in alphabetic order.

        :precondition: __words contains at least one item
        :postcondition: returns a list of words in __words
        :return: list of strings of each word from the __words set
        """
        return sorted(list(self.__words))

    def __str__(self) -> str:
        """
        Return this object as an informative string message.

        This message is printed when the Vocabulary object is printed.
        :return: message containing words in the __words set as a string
        """
        return "Here is the list of words currently in the vocabulary: {}".format(" ".join([word.title() for word in
                                                                                            list(self.__words)]))

    def __repr__(self) -> str:
        """
        Return this object's properties as a string.

        This string is printed when the Vocabulary object is inside a collection.
        :return: string containing value of the __words set
        """
        return f"{self.__words}"

