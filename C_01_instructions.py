print("🎲🎲 Roll It 13 🎲🎲")


# loop: for testing purpose

while True:
    want_instructions = input("Do you want to read the instructions? ").lower()

    if want_instructions == "yes":
        print("you choose yes")
    elif want_instructions == "y":
        print("you choose yes")
    elif want_instructions == "n":
        print("no")
    elif want_instructions == "no":
        print("you choose no")
    else:
        print("you did not choose a valid response")

