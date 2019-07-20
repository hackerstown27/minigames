from random import shuffle



class Deck:
    def __init__(self):
        self.suits = ("Club", "Spades", "Heart", "Diamond")
        self.ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
                 "Ten", "King", "Queen", "Jocker", "Ace")
        self.deck = [(suit, rank) for suit in self.suits for rank in self.ranks]
        shuffle(self.deck)

    def get_card(self):
        return self.deck.pop()


class Hand:
    def __init__(self):
        self.hand = []
        self.values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9,
                       "Ten": 10, "King": 10, "Queen": 10, "Jocker": 10, "Ace": 11}
        self.ace = 0

    def add_card(self, card):
        self.hand.append(card)

    def check_bust(self):
        hand_values = 0
        for suit, rank in self.hand:
            hand_values += self.values[rank]
            if rank == 'Ace':
                self.ace += 1
        if hand_values > 21:
            while self.ace:
                hand_values -= 10
                self.ace -= 1
        if hand_values > 21:
            return False
        return True

    def dealer_hits(self):
        hand_values = 0
        for suit, rank in self.hand:
            hand_values += self.values[rank]
        if hand_values >= 17:
            return False
        return True

    def points(self):
        hand_values = 0
        for suit, rank in self.hand:
            hand_values += self.values[rank]
            if rank == 'Ace':
                self.ace += 1
        if hand_values > 21:
            while self.ace:
                hand_values -= 10
                self.ace -= 1
        return hand_values


class Chips:

    def __init__(self):
        while True:
            try:
                self.amount = int(input("\nPlease Enter Your Amount Of Chips ?   "))
                if self.amount == 0:
                    print("\nZero Coud'nt Do Anything Here !")
                else:
                    break

            except:
                print("\nPlease Provide An Integer!  ")

    def bet(self):
        while True:
            try:
                self.bet_amount = int(input("\nPlease Enter the Amount To Bet ? "))
                if self.bet_amount == 0 :
                    print("\nZero Coud'nt Do Anything Here !")
                    continue
                if self.bet_amount > self.amount:
                    print("\nInsufficient Balance!")
                    continue
                else:
                    break
            except:
                print("\nPlease Provide An Integer! ")


def show_cards(player_hand,dealer_hand,first=False):
    if first:
        print("\nPlayer Cards Are: ")
        for suit, rank in player_hand:
            print(f"{rank} Of {suit}")
        print("\nDealer Cards Are: ")
        print(f"{dealer_hand[0][1]} Of {dealer_hand[0][0]}")
        print("Hidden Card")

    else:
        print("\nPlayer Cards Are: ")
        for suit, rank in player_hand:
            print(f"{rank} Of {suit}")
        print("\nDealer Cards Are: ")
        for suit, rank in dealer_hand:
            print(f"{rank} Of {suit}")


print("Welcome To BlackJack !\n")
print('''
To play a hand of Blackjack the following steps must be followed:\n

1. Create a deck of 52 cards\n
2. Shuffle the deck\n
3. Ask the Player for their bet\n
4. Make sure that the Player's bet does not exceed their available chips\n
5. Deal two cards to the Dealer and two cards to the Player\n
6. Show only one of the Dealer's cards, the other remains hidden\n
7. Show both of the Player's cards\n
8. Ask the Player if they wish to Hit, and take another card\n
9. If the Player's hand doesn't Bust (go over 21), ask if they'd like to Hit again.\n
10. If a Player Stands, play the Dealer's hand. The dealer will always Hit until the Dealer's value meets or exceeds 17\n
11. Determine the winner and adjust the Player's chips accordingly\n
12. Ask the Player if they'd like to play again\n
''')
chips = Chips()
while True:
    report = True
    user_input = input("\nAre You Ready ? (Y OR N)  ")
    if user_input.lower() == 'y':

        chips.bet()
        cards = Deck()
        player = Hand()
        dealer = Hand()

        for _ in range(2):
            player.add_card(cards.get_card())
            dealer.add_card(cards.get_card())

        show_cards(player.hand, dealer.hand, first=True)

        while player.check_bust():
            user_input = input("\nDo You Want To Hit Or Stand ?  (H OR S)   ")
            if user_input.lower() == 'h':
                player.add_card(cards.get_card())
                show_cards(player.hand, dealer.hand)
            elif user_input.lower() == 's':
                while dealer.dealer_hits() and dealer.check_bust():
                    dealer.add_card(cards.get_card())
                else:
                    show_cards(player.hand, dealer.hand)

                if not dealer.check_bust():
                    print("\nDealer Bust, Player Wins!")
                    report = False
                    chips.amount += chips.bet_amount
                break
            else:
                print("\nPlease Choose Between (H OR S)")

        else:
            print("\nPlayer Bust, Dealer Wins!")
            report = False
            chips.amount -= chips.bet_amount

        player_points = player.points()
        dealer_points = dealer.points()

        if report:

            if player_points > dealer_points:
                print("\nPlayer Wins!")
                chips.amount += chips.bet_amount

            elif player_points < dealer_points:
                print("\nDealer Wins!")
                chips.amount -= chips.bet_amount

            elif player_points == dealer_points:
                print("\nDraw")

        print(f"\nPlayer Balance : {chips.amount}")

    elif user_input.lower() == 'n':
        print("\nQuiting......")
        break
    else:
        print("\nPlease Choose Between Y OR N")