ask = input("What is your name: ")
print(f" Hello, {ask} nice to meet you!")
import random

while True:
    
    user_action  = input("Enter a choice (rock,paper,scissor):")

    possible_actions = ['rock', 'paper', 'scissor']
    computer_action = random.choice(possible_actions)

    print(f"\nYou choose {user_action}, computer choose {computer_action}.\n")

    if user_action == computer_action:
          print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == 'rock':
          if computer_action == 'scissor':
               print("Rock destroys scissor. You win!")
          else:
               print("Paper covers rock. You lose")
    elif user_action == 'paper':
           if computer_action == 'scissor':
                print("Scissor cuts paper. You lose!")
           else:
                print("Paper covers rock. You win")
    elif user_action == 'scissor':
           if computer_action == 'rock':
                print("Rock smashes scissor.You lose!")
           else:
                print("Scissor cuts paper.You win")
    play_again = input("Do you want to play again(y/n): ")
    if play_again.lower() == 'n':
             break
            
    
    
