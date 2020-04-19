import random

# ruleBook = {
#     ('rock','paper'): False,
#     ('scissors','rock'): False,
#     ('paper','scissors'): False,
#     ('paper','rock'): True,
#     ('rock','scissors'): True,
#     ('scissors','paper'): True,
# }

def contest(a,b):
    if(a=='rock' and b=='rock'):
        print("it's a clash ")
    if(a=='scissors' and b=='scissors'):
        print("it's a clash ")
    if(a=='paper' and b=='paper'):
        print("it's a clash ")
    if(a=='rock' and b=='scissors'):
        print("You win")
    if(a=='scissors' and b=='rock'):
        print("Computer win ")
    if(a=='paper' and b=='rock'):
        print("You win ")
    if(a=='rock' and b=='paper'):
        print("Coputer win ")
    if(a=='paper' and b=='scissors'):
        print(" Computer win ")
    if(a=='scissors' and b=='paper'):
        print(" You win")



choice = str(input("Enter your choice:\n 1.Scissors \n 2.Rock \n 3.Paper \n "))

print("Your choice is ",str(choice))

choices=['rock','paper','scissors']

computer_rand = random.choice(choices)
print("Computer's choice is:  " ,str(computer_rand))

contest(choice, computer_rand)

