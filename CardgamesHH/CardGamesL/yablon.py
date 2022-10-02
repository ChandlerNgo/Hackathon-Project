import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card():
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + " of " + self.suit

class Deck:
    
    def __init__(self):
        
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit,rank)
                
                self.all_cards.append(created_card)
                
    def shuffle(self):
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        return self.all_cards.pop()

class Player:
    
    def __init__(self,name):
        
        self.name = name
        self.all_cards = []
        
    def remove_one(self):
        return self.all_cards.pop(0)
    
    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
    
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'

class Chips:
    def __init__(self,total=1000):
        self.total = total 
        self.bet = 0  
    def win_bet(self):
        self.total += self.bet
        print(f"You have {self.total} chips")
    def lose_bet(self):
        self.total -= self.bet
        print(f"You have {self.total} chips")

def main():
    player_one = Player("One")

    player_one.chips = Chips()

    deck = Deck()
    deck.shuffle()

    global playing

    def take_bet(chips): 
        while True:
            try:
                chips.bet = int(input("Please enter the amount you would like to bet: "))
            except ValueError:
                print("Please enter an integer")
            else:
                if chips.bet > chips.total:
                    print("You do not have enough chips")
                else:
                    break
    def getChips():
        return player_one.chips
    def getDealtCardOne():
        return dealt_card1
    def getDealtCardTwo():
        return dealt_card2
    def getDealtCardThree():
        return dealt_card3

    while True:

        print(f"Yablon will now begin.\nPlayers Chips: {player_one.chips.total} chips")

        take_bet(player_one.chips)

        dealt_card1 = deck.deal_one()
        dealt_card2 = deck.deal_one()
        print(f'Dealt Card 1: {dealt_card1}')
        print(f'Dealt Card 2: {dealt_card2}')

        if dealt_card1.value - 1 == dealt_card2.value or dealt_card1.value + 1 == dealt_card2.value:
            print("It's a Push!")
            break
        elif dealt_card1.value == dealt_card2.value:
            dealt_card3 = deck.deal_one()
            print('Dealt Card 3: {dealt_card3}')
            if dealt_card1.value != dealt_card3.value:
                print("It's a Push!")
                break
            else:
                player_one.chips *= 11
        else:
            guess = input('Will the third card be in between the two cards? ').lower()
            dual_bet = input('Do you want to double down? ').lower()

            if dual_bet[0] == 'y':
                player_one.chips.bet *= 2
                
            third_card = deck.deal_one()
            diff = abs(dealt_card2.value - dealt_card1.value)

            if guess[0] == 'y':
                if third_card.value in range(dealt_card1.value,dealt_card2.value+1) or third_card.value in range(dealt_card2.value,dealt_card1.value+1):
                    print('You Win!')
                    if diff == 1:
                        player_one.chips.bet *= 5
                        player_one.chips.win_bet()
                    elif diff == 2:
                        player_one.chips.bet *= 4
                        player_one.chips.win_bet()
                    elif diff == 3:
                        player_one.chips.bet *= 2
                        player_one.chips.win_bet()
                    else:
                        player_one.chips.win_bet()
                else:
                    print('You Lose!')

                    player_one.chips.lose_bet()
            else:
                if not third_card.value in range(dealt_card1.value,dealt_card2.value+1) or not third_card.value in range(dealt_card2.value,dealt_card1.value+1):
                    print('You Win!')

                    player_one.chips.win_bet()
                else:
                    print('You Lose!')
                    
                    player_one.chips.lose_bet()
        
        print("\nPlayers chips total:", player_one.chips.total)
        
        new_game = input("Would you like to play another round? Enter 'y' or 'n' ")
        
        if new_game[0].lower()=='y':
            playing = True
            continue
        else:
            print("Thanks for playing!")
            break


if __name__ == '__main__':
    main()