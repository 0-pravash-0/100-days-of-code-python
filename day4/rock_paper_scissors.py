import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
image = [rock, paper, scissors]

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print("You chose:")
print(image[choice])

comp = random.randint(0,2)
print("Computer chose:")
print(image[comp])

if choice == comp:
    print("DRAW")
elif choice ==0 and comp == 1:
    print("You LOSE")
elif choice == 0 and comp == 2:
    print("You WIN")
elif choice ==1 and comp == 0:
    print("You WIN")
elif choice == 1 and comp == 2:
    print("You LOSE")
elif choice ==2 and comp == 0:
    print("You LOSE")
elif choice == 0 and comp == 1:
    print("You WIN")

