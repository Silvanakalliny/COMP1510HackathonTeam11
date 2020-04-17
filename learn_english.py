def main():
    print("Welcome to Learn English App!")
    running = True
    while running:
        menu_list = ["Check a word", "Add a word", "Add words",
                     "Remove a word", "Print your word list",
                     "Print the word list", "Print the word list with definition",
                     "Test your vocabulary"]

        for i, options in enumerate(menu_list, 1):
            print("%d. %s" % (i, options))

        # user must input 1-8 or type quit to exit
        choice = input("Type 'quit' to exit the application\n").strip().lower()

        if choice == "quit":
            running = False
        elif choice == "1":
            pass
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            pass
        elif choice == "6":
            pass
        elif choice == "7":
            pass
        elif choice == "8":
            pass
        else:
            print("Invalid Choice!")


main()
