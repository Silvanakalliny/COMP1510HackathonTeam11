from vocabulary import Vocabulary
import time


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
                     "Test your vocabulary"]

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
            word = input("Enter the word you would like to remove: ")
            vocabulary.remove_a_word(word)
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
            print("Invalid Choice!")


def print_list(a_list):
    for i, items in enumerate(a_list, 1):
        print("%d. %s" % (i, items))


def user_input(item_list, result, input_string) -> str:
    print("\n" + "-" * 50)
    print("\n%s\n" % result)
    print_list(item_list)
    return input("\n%s" % input_string)


main()
