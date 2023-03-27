import random

# generate a random number between 1 and 100
number = random.randint(1, 100)

def guess_number():
    # initialize the guess counter
    num_guesses = 0
    while True:
        # ask the user to enter a guess, or "q" to quit
        guess_str = input("Guess the number (1-100), or 'q' to quit: ")
        
        # check if the user entered "q"
        if guess_str.lower() == "q":
            print("Thanks for playing! The number was", number)
            break
            
        # try to convert the guess to an integer
        try:
            guess = int(guess_str)
        except ValueError:
            print("Invalid input, please enter a number or 'q' to quit.")
            continue
        
        # increment the guess counter
        num_guesses += 1
        
        # check if the guess is correct
        if guess == number:
            print("Congratulations, you guessed the number in", num_guesses, "guesses!")
            break
        elif guess < number:
            print("Too low!")
        else:
            print("Too high!")

        
    
guess_number()

        




    
        

    
    
    
   
    
    

