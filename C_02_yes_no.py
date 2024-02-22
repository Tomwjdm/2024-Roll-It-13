# checks users enter yes (y) or no (n)
def yes_no(question):
    while True:
        Response = input(question).lower()

        if Response == "yes" or Response == "y":
            return "yes"
        elif Response == "no" or Response == "n":
            return "no"
        else:
            print("you did not choose a valid response")


# Main Routine
while True:
    want_instructions = yes_no("Do you want to read the instructions ")
    print(f"you choose {want_instructions}")


