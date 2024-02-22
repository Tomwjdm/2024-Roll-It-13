# checks users enter yes (y) or no (n)
def yes_no(question):
    while True:
        Response = input(question).lower()

        # checks user response, question
        # repeats repeat if users don't enter yes / no
        if Response == "yes" or Response == "y":
            return "yes"
        elif Response == "no" or Response == "n":
            return "no"
        else:
            print("please enter yes / no")


def instructions():
    print('''
    
    **** Instructions ****
    
        To begin, decide on a score goal (eg:  The first one to get a 
        score of 50 wins).
        
        For each round of the game, you win points by rolling the dice.
        The winner of the round is the one who gets 13 (or slightly less).
        
        If you win, then your score will increase by the
        number of points that you earned. If your first roll of two 
        dice is double (eg: both dice show a three), then your score
        will be DOUBLE the number of points.
        
        If you lose tthe round, then you dont get any points
        
        If you and the computer tie (eg: you both get a score of 11,
        then you will have 11 points added to your score.
        
        Your goal is to try to get  to the target score before the 
        computer.
        
        Good luck
        
        
    
    ''')
    
# Main Routine
print()
print("🎲🎲 Roll It 13 🎲🎲")
print()
# loop: for testing purpose

want_instructions = yes_no("Do you want to read the instructions? ")

# checks users enter yes (y) or no (n)
if want_instructions == "yes":
   instructions()

print("Program continues")

