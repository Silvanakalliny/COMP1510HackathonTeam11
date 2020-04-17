class Vocabulary:
    def __init__(self):
        self.__words = set()

    def add_a_word(self, new_word):
        self.__words.add(new_word)

    def add_words(self, *new_words):
        for word in new_words:
            self.add_a_word(word)

    def remove_a_word(self, word):
        self.__words.remove(word)

    def remove_words(self, *words):
        for word in words:
            self.remove_a_word(word)

    def sort_words(self):
        return sorted(list(self.__words))

    def __str__(self):
        print([word for word in list(self.__words)])
        return f"Here are the words in the vocabulary list: {[word for word in list(self.__words)]}"

    def __repr__(self):
        return f"{self.__words}"

