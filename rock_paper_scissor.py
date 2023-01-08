import random

# creating a sequence, to put in random function to get random selections

options = ['rock','paper','scissor']
computer_choice = random.choice(options)

# to get input from user

user_choice = input("select your input out of rock, paper or scissor to play the game with Vivek\n")

# code to give results
if computer_choice == user_choice:
    print("You tied with Vivek")
elif computer_choice=='rock' and user_choice=='paper':
    print("You win, Vivek selected "+computer_choice)
elif computer_choice=='paper' and user_choice=='scissor':
    print("You win, Vivek selected "+computer_choice)
elif computer_choice=='scissor' and user_choice=='rock':
    print("You win, Vivek selected "+computer_choice)
else:
    print("Vivek win, he selected "+computer_choice)
