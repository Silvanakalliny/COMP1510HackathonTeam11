"""Main module for vocabulary program. Contains functions for user interface."""

import time
import vocabulary


def study_time(func) -> float:
    """
    Print the time spent from start of app to when the user quits.

    :param func: a function
    :precondition: this function is wrapped around a function requiring user input
    :postcondition: prints the time user spent using program, and returns time in seconds as a float
    :return: time in seconds as a floating point number
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
    """Run the vocabulary program."""
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
