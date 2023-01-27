import random

def play():
    user = input('Choose between: scissors (s), paper (p), rock (r)\n')
    computer = random.choice(['s, p, r'])

    if user == computer:
        return 'Tie!'
    
    # r > s, s > p, p > r
    if is_win(user, computer):
        return 'You won!'

    return 'Lost!'

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent =='r'):
        return True

print(play())