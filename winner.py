import random

options = {1: 'Stone', 2: 'Scissors', 3: 'Paper', 4: 'Exit'}
def play():
    score = [0, 0]
    while not any(wins == 3 for wins in score):
        print(f'SCORE\tUser: {score[0]} - PC: {score[1]}')
        user_choice = int(input('Enter your selection:{}> '.format(
            ''.join([f'\n{n}: {option}\n' for n, option in options.items()]))))
        pc_choice = random.randint(1, 3)
        print(f'{options[user_choice]} vs. {options[pc_choice]}')
        if user_choice in (pc_choice - 1, pc_choice + 2):
            print('User wins')
            score[0] += 1
        elif user_choice == pc_choice:
            print('Draw')
        elif user_choice == 4:
            break
        else:
            print('PC Wins')
            score[1] += 1
        input('\n_____ ENTER TO PROCEED _____')


    winner = 'User' if score[0] == 4 else 'PC'
    print(f'\n{winner} won the match!')


play()