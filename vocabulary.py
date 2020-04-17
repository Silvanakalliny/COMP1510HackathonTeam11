class Vocabulary:
    def __init__(self):
        self.__words = set()

    def add_a_word(self, new_word):
        self.__words.add(new_word.lower().strip())

    def add_words(self, *new_words):
        for word in new_words:
            self.add_a_word(word.lower().strip())

    def remove_a_word(self, word):
        self.__words.remove(word.lower().strip())

    def remove_words(self, *words):
        for word in words:
            self.remove_a_word(word.lower().strip())

    def sort_words(self):
        return sorted(list(self.__words))

    def __str__(self):
        return "Here is the list of words currently in the vocabulary: {}".format(" ".join([word.title() for word in
                                                                                            list(self.__words)]))

    def __repr__(self):
        return f"{self.__words}"

