#Rock, Paper, Scissors
import random
options = ["R", "S", "P"]
CPU = random.choice(options)
def check_winner(choices):
    choice_copy = choices.copy()
    choice_copy.reverse()
    #R > S , S > P & P > R
    if choice_copy == ["R", "P"] or choice_copy == ["P", "R"]:
        return choices.index("P")
    elif choice_copy == ["R", "S"] or choice_copy == ["S", "R"]:
        return choices.index("R")
    elif choice_copy == ["S", "P"] or choice_copy == ["P", "S"]:
        return choices.index("S")
print('Let\'s play Rock(R), Paper(P) and Scissors(S) \n ')
print('Rock beats Scissors, Scissors beats Paper and Paper beats Rock\n')
user_input = input ("Enter your choice either R, S or P: ")
while True:
     if user_input in options:
         print("Player ({}): CPU ({})".format (user_input, CPU))
         if user_input == CPU:
             print("It's a tie")
             user_input = input("Enter your choice: ")
             CPU = random.choice(options)
             continue
         else:
             res = check_winner([CPU, user_input])
             if res == 0:
                 print("CPU wins")
             else:
                 print("User wins")
         break
     else:
         print("Invalid option")
         user_input = input("Enter your choice: ")
