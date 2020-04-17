def main():
    #while True:
        menu_list = ["Check a word", "Add a word", "Add words",
                     "Remove a word", "Print your word list",
                     "Print the word list", "Print the word list with definition",
                     "Test your vocabulary"]

        for i, options in enumerate(menu_list, 1):
            print("%d. %s" % (i, options))

        user_input = input("Type 'quit' to exit the application")

main()
