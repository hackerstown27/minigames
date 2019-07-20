from random import choice


class Elements:

    def __init__(self):
        self.elements = ['rock', 'paper', 'scissors']

    def get_element(self):
        return choice(self.elements)


class Hand:

    def __init__(self, player_hand, computer_hand):
        self.player_hand = player_hand
        self.computer_hand = computer_hand

    def show_hand(self):
        print(f'\nPlayer :  {self.player_hand}', end="")

        print(f'\t\t\tComputer :  {self.computer_hand}')

    def check(self):

        if self.player_hand == self.computer_hand:
            return "Draw !"

        elif self.player_hand == 'rock' and self.computer_hand == 'scissors':
            return "Players Wins !"

        elif self.player_hand == 'scissors' and self.computer_hand == 'paper':
            return "Players Wins !"

        elif self.player_hand == 'paper' and self.computer_hand == 'rock':
            return "Players Wins !"

        else:
            return "Computer Wins !"

def play():
    elements = Elements()
    player_hand = elements.get_element()
    computer_hand = elements.get_element()

    hand = Hand(player_hand, computer_hand)

    hand.show_hand()

    print("\n", hand.check().center(40), '\n')


print("Welcome To Rock, Paper, Scissors")
print('''\nRules :\n
1. Rock Defeats Scissors\n
2. Scissors Defeats Paper\n
3. Paper Defeats Rock\n
4. Same Element Will Accounted As Draw\n''')

while True:
    user_input = input("Would You Like To Continue ? ... (Y Or N)   ")
    if user_input.lower() == 'y':
        play()
        while True:
            user_input = input("Do Want To Play More ? .... (Y Or N)   ")
            if user_input.lower() == 'y':
                play()
            elif user_input == 'n':
                break
            else:
                print("Please Provide A Valid Input !\n")
        break
    elif user_input.lower() == 'n':
        break
    else:
        print("Please Provide A Valid Input !\n")

print("Thank You Playing !")