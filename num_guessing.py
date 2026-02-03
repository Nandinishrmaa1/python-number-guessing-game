import random

def number_guessing_game():
    print("Select Difficulty Level:")
    print("1. Easy (1–50, 10 attempts)")
    print("2. Medium (1–100, 7 attempts)")
    print("3. Hard (1–200, 5 attempts)")
    try :
        choice = int(input("Enter your Choice : "))
    except ValueError:
        print("Invalid number : Enter a number")
        return
        
    max_attempts = 0
    upper_limit = 0 
    if choice == 1:
        max_attempts = 10 
        upper_limit = 50
    elif choice == 2:
        max_attempts = 7
        upper_limit = 100
    elif choice == 3 :
        max_attempts = 5
        upper_limit = 200
    else : 
        print("Invalid choice!")
        return
    
    random_num = random.randint(1,upper_limit)
  
    
    is_winner = False
    while max_attempts > 0:
       
        try :
            user_num = int(input("Enter the number : "))
        except ValueError: 
            print("Invalid number : Enter a number")
            continue
            
        if user_num == random_num:
            is_winner = True
            break
        elif user_num > random_num:
            print("Too high")
        else:
            print("Too low")
       
        max_attempts -= 1
        print(f"Attempts left: {max_attempts}")
        
    if is_winner:
        print("Congratulations! You won the game")
    else : 
        print("Nice try! You lost")

#Replay
while True:
    number_guessing_game()
    option = input("\nDo you want to play again? (yes/no): ").lower()

    if option != "yes":
        print("Thanks for playing!")
        break