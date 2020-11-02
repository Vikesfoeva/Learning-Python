from stack import Stack
import os
os.system('clear')
print("Let's play Towers of Hanoi!!")

#Create the Stacks
stacks = []
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")
stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)

choices = [n.name[0:1] for n in stacks]

#Set up the Game
num_disks = 0

while num_disks < 3:
  try:
    num_disks = int(input('How many disks do you want to play with?\nEnter a number greater than or equal to 3\n'))
  except:
    print("Please enter an integer!")

for i in range(num_disks, 0, -1):
  left_stack.push(i)

print( "\nThe fastest you can solve this game is in {moves} moves\n".format(moves = 2**num_disks - 1))

#User Input
def get_input():
  choice = input()
  while True:
    if choice.upper() in choices:
      for i in range(len(choices)):
        if choice.upper() == choices[i]:
          return stacks[i]
    else:
      print("invalid choice, please enter a valid option")
      print(choices)
      choice = input("Please enter a new choice\n")
  return 'Broke'

#Play the Game
move_tally = 0
print("...Current Stacks...")
for i in stacks:
  i.print_items()
print("\nReferring to stacks:")
for i in stacks:
  print(str(i.name[0:1]) + ' corresponds to ' + str(i.name) + ' stack.')

while True:
  print("\nWhich stack do you want to move from?")
  from_stack =  get_input()

  if from_stack.get_size() != 0:
    print("\nWhich stack do you want to move to?")
    to_stack = get_input()

    if to_stack.size == 0:
      moving = from_stack.pop()
      to_stack.push(moving)
    elif (to_stack.size > 0) and (to_stack.peek() > from_stack.peek()):
      move_tally += 1
      moving = from_stack.pop()
      to_stack.push(moving)
      # Check for Win
      if (left_stack.get_size() == 0) and (middle_stack.get_size() == 0) and (right_stack.get_size() == num_disks):
        "You win!"
        break

    else:
      print("\n****Invalid move!  Big rings cannot be placed on little rings.***\n")

  elif from_stack.get_size() == 0:
    print("That stack is empty!  That is an invalid option.")

  print("...Current Stacks...")
  for i in stacks:
    i.print_items()

print("You took this many moves:", move_tally)