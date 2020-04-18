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
            add_word = input("Add a new word: ")
            vocabulary.add_a_word(add_word)
        elif choice == "3":
            pass
        elif choice == "4":
            delete_word = input("Remove a word: ")
            vocabulary.remove_a_word(delete_word)
        elif choice == "5":
            pass
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
            pass
        else:
            print("Invalid Choice!\n")


def print_list(a_list):
    for i, items in enumerate(a_list, 1):
        print("%d. %s" % (i, items))


def user_input(item_list, result, input_string) -> str:
    print("\n" + "-" * 50)
    print("\n%s\n" % result)
    print_list(item_list)
    return input("\n%s" % input_string).strip()


main()
