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
    #while True:
        menu_list = ["Check a word", "Add a word", "Add words",
                     "Remove a word", "Print your word list",
                     "Print the word list", "Print the word list with definition",
                     "Test your vocabulary"]

        for i, options in enumerate(menu_list, 1):
            print("%d. %s" % (i, options))

        user_input = input("Type 'quit' to exit the application")

main()
