import random
import time
from card import Card


# Deal a card from the deck to the discard pile
# If discard is empty, reset the deck
def deal():
    if len(deck) != 0:
        discard.append(deck.pop())
        discard[-1].visible = True
    else:
        for i in range(len(discard)):
            deck.append(discard.pop())
            deck[-1].visible = False

# Check to see if a command is valid
def valid_input(command):
    if len(command) == 0 or command == "help": # Special commands: draw or display help
        return True
    elif len(command) < 2 or len(command) > 4:
        print('Error: wrong command length')
        return False # Has to be between length 2 and 4
    elif command[1] not in ['q','w','e','r','1','2','3','4','5','6','7']:
        return False # These are all of the keybinds for the stacks
    elif (command[0] not in ['1','2','3','4','5','6','7','d']):
        return False # Can't move from anything other than a main stack or the discard pile
    elif command[0] == command[1]:
        return False # Can't move a card onto itself
    elif len(command) in [3,4]:
        print(command[3:])
        try:
            if int(command[2:]) > 13 or int(command[2:]) == 0:
                return False
            else:
                return True # Passes every other check, so can return True here
        except ValueError:
            print('Cannot convert stack size to number')
            return False # Size of stack to move must be a number
    else:
        return True

# Moves a card (if able) from the starting stack to ending stack
# Takes starting list, ending list, ending stack type (str), and number of cards to move
def move_card(start, target, stack_type, n):
    empty_num = 13 if stack_type == 'm' else 1
    if len(target) == 0 and start[-n].value != empty_num:
        print('Invalid move: can\'t move that card onto an empty stack')
    elif len(target) != 0 and (not start[-n].is_valid_move(target[-1], stack_type)):
        print(f'Invalid move: {start[-1].name} -> {target[-1].name}')
    elif not start[-n].visible:
        print('Invalid move: can\'t move unrelvealed card')
    else:
        for i in range(n,0,-1):
            target.append(start.pop(-i))
        if len(start) > 0:
            start[-1].visible = True
        return 1
    input('{Press enter to continue)')
    return 0
    
        

# Prints the current board state
def print_board():  
    out = ' '*35
    for stack in end_stacks:
        if len(stack) == 0:
            out += '[   ]'
        else:
            out += stack[-1].print_name()
    print(out + '\n')
    for i in range(max(len(x) for x in main_stacks)):
        out = ''
        if i == 0:
            if len(deck)>0:
                out = out + deck[-1].print_name()
            else:
                out = out + '[   ]'
            if len(discard)>0:
                out = out + discard[-1].print_name()
            else:
                out = out + '[   ]'
        else:
            out = out + '          '
        out = out + '          '
        for j in range(7):
            if len(main_stacks[j]) >= i + 1:
                out = out + main_stacks[j][i].print_name()
            else:
                if i == 0:
                    out = out + '[   ]'
                else:
                    out = out + '     '
        print(out)    

# Prints instructions on how to play and asks player if they're ready
def show_instructions():
    print('INSTRUCTIONS:')
    print('-Press Enter (empty input) to deal card from the deck')
    print('-Each of the seven primary stacks is represented by a number, 1-7')
    print('-Each of the ending stacks (the ones that count up from Ace) \
    are represented by "q", "w", "e", and "r" respectively')
    print('-The discard pile is represended by "d"')
    print('-The syntax for a command is the stack to move FROM then the stack to move TO')
    print('Example 1: To move a card from stack 2 to stack 6, type "26" (without quotation marks)')
    print('Example 2: Moving from stack 3 to the fourth end stack: "3r" (without quotation marks)')
    print('Example 3: Moving from discard to stack 3: "d3" (without quotation marks)\n')
    print('To move multiple cards at the same time, add a third number to the end of your command')
    print('This third number is how many cards you want to move off of the stack')
    print('Example: If you want to move the bottom 4 cards from stack 2 to stack 7, it would be: "274"')
    print('If you forget, you can always type "help" to see these instructions again')
    ans = input('Do you understand (y/n)? ')
    if ans.lower() != "y":
        # If they don't say yes, wait a second then print instructions again
        print('Okay, I\'ll repeat myself...')
        time.sleep(1)
        show_instructions()
    else:
        print('Great! Let\'s play!')
        time.sleep(1)

# Checks to see if the player has won
def check_win():
    if all(len(x) == 13 for x in end_stacks):
        return True
    else:
        for stack in main_stacks:
            if not all(x.visible for x in stack):
                return False
    return True

#----------------------------#
#         GAME SETUP         #
#----------------------------#

# Initialize game lists representing stacks of cards
main_stacks = [[],[],[],[],[],[],[]] # Stacks in the main play area
end_stacks = [[],[],[],[]] # Ending stacks taht start empty and count up
discard = []
suits = ['D','H','S','C']
deck = []
moves = 0
zero_move = {'end': 1, 'main': 13}

# Generate the deck
for s in suits:
    for i in range(1,14):
        deck.append(Card(i,s))

# Make a randomization seed and randomize the deck based on the seed
while True:
    seed_in = input('Enter seed number or leave blank for a random seed')
    if seed_in:
        try:
            seed = int(seed_in)
        except ValueError:
            print('Invalid seed number. Try again.')
            continue
    else:
        seed = random.random()
    break

print(f'Seed: {seed} (currently for internal testing purposes)')
random.Random(seed).shuffle(deck)

# Deal cards from deck to each stack
for i, stack in enumerate(main_stacks):
    for j in range(1,i+2):
        stack.append(deck.pop())
    stack[-1].visible = True


#----------------------------------#
#         GAME STARTS HERE         #
#----------------------------------#

show_instructions()
while True:
    print_board()
    choice = input('Enter move command: ')
    if valid_input(choice):
        if choice == 'help':
            show_instructions()
        elif choice == '':
            deal()
            moves += 1
        else: # If it is a valid command to move a card
            start = choice[0]
            target = choice[1]
            n_move = int(choice[2:]) if len(choice) > 2 else 1
            if start == 'd': # If moving from discard, set "start" to point at discard pile
                if n_move > 1:
                    print('Can\'t move multiple cards onto an end stack')
                    input('(Press enter to continue)')
                    continue
                elif len(discard) == 0:
                    print('Discard pile is empty!')
                    input('(Press enter to continue)')
                    continue
                start = discard
            else: # If not, it's from a main stack
                start = main_stacks[int(start) - 1]
                if len(start) < n_move:
                        print('Stack doesn\t have that many cards')
                        input('(Press enter to continue)')
                        continue
            try: # If target can be converted to int, it's a main stack move
                target = main_stacks[int(target) - 1]
                stack_type = 'm'
            except ValueError: # If not, it's an end stack move
                target = end_stacks[['q','w','e','r'].index(target)]
                stack_type = 'e'
                if n_move > 1:
                    print('Can\'t move multiple cards onto an end stack')
                    input('(Press enter to continue)')
                    continue
            moves += move_card(start, target, stack_type, n_move)
            
    else:
        print('Invalid command, try again')
        input('{Press enter to continue)')

    if check_win():
        break

print(f'Congratulations! You won in {moves} moves!')

