
import random
choices=["stone","paper","scissors"]  //list of choices
print("Make your throw")
user_choice=input(" Type stone, paper or scissors : ")  //user's input
if user_choice in choices:
  computer_choice=random.choice(choices)  //PC's choice from random
  print(f "\n You threw '{user_choice}', the PC threw '{computer_choice}'")  //f is used to give the {name} for the template
else:
  print(f "\n You typed '{user_choice}' which is not a valid throw")