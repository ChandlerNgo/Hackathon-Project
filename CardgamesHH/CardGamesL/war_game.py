# amount of cards: len of list of cards
    #len(player_one.all_cards)
    #len(player_two.all_cards)
# war button
# inital betting amount
    #Players Chips
# current card they have


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

#GAME SETUP
def main():

    player_one = Player("One")
    player_two = Player("Two")

    new_deck = Deck()
    new_deck.shuffle()

    for x in range(26):
        player_one.add_cards(new_deck.deal_one())
        player_two.add_cards(new_deck.deal_one())

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

    players_chips = Chips()

    print(f"War will now begin.\nPlayers Chips: {players_chips.total} chips")   
        
    take_bet(players_chips)

    game_on = True

    round_num = 0

    while game_on:
        
        round_num += 1
        print(f"Round {round_num}")
        # Showing the number of player's cards
        print(f"Player 1's Cards: {len(player_one.all_cards)}")
        print(f"Player 2's Cards: {len(player_two.all_cards)}")
        
        if len(player_one.all_cards) == 0:
            print('Player One, out of cards! Player Two wins')
            Chips.lose_bet(players_chips)
            game_on = False
            break
        if len(player_two.all_cards) == 0:
            print('Player Two, out of cards! Player One wins')
            Chips.win_bet(players_chips)
            game_on = False
            break 
        
        player_one_cards = []
        player_one_cards.append(player_one.remove_one())
        
        player_two_cards = []
        player_two_cards.append(player_two.remove_one())
        
        print(f"Player 1's Card: {player_one_cards[0]}")
        print(f"Player 2's Card: {player_two_cards[0]}")
        
        war_button = input("Declare War!")
        multiplier = int(input("1x, 5x, or 10x?"))
        
        at_war = True
        
        while at_war:
            
            if player_one_cards[-1].value > player_two_cards[-1].value:
                
                player_one.add_cards(player_one_cards)
                player_one.add_cards(player_two_cards)
                
                at_war = False
            
            elif player_one_cards[-1].value < player_two_cards[-1].value:
                
                player_two.add_cards(player_one_cards)
                player_two.add_cards(player_two_cards)
                
                at_war = False   
                
            else:
                print("WAR!")
                
                if len(player_one.all_cards) < multiplier:
                    print("Player One unable to declare war")
                    print("PLAYER TWO WINS!")
                    Chips.lose_bet(players_chips)
                    game_on = False
                    break
                    
                elif len(player_two.all_cards) < multiplier:
                    print("Player Two unable to declare war")
                    print("PLAYER ONE WINS!")
                    Chips.win_bet(players_chips)
                    game_on = False
                    break
                    
                else:
                    for num in range(multiplier):
                        player_one_cards.append(player_one.remove_one())
                        player_two_cards.append(player_two.remove_one())

    print("\nPlayers chips total:", players_chips.total)
        
    new_game = input("Would you like to play another game? Enter 'y' or 'n' ")
        
    if new_game[0].lower()=='y':
        game_on = True
    else:
        print("Thanks for playing!")
            


if __name__ == "__main__":
    main()

