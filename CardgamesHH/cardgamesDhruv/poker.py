import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return self.rank + " of " + self.suit

class Deck:
    
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += "\n"+card.__str__()
        return 'The deck has: '+ deck_comp
    def shuffle(self):
        random.shuffle(self.deck)  
    def deal(self):
        single_card = self.deck.pop()
        return single_card

class Hand:
    def __init__(self):
        self.cards = []  
        self.value = 0   
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]

class Chips:
    def __init__(self,total=1000):
        self.total = total 
        self.bet = 0  
    def win_bet(self):
        self.total += self.bet
    def lose_bet(self):
        self.total -= self.bet

def main():

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

    def show_some(player): 
        print("\nPlayer's Hand:", *player.cards, sep='\n ')
        
    def show_all(player,bot1,bot2,bot3,bot4,bot5):
        print("Bot1's Hand:", *bot1.cards, sep='\n ')
        print("Bot1's Hand =",bot1.value)
        print("Bot2's Hand:", *bot2.cards, sep='\n ')
        print("Bot2's Hand =",bot2.value)
        print("Bot3's Hand:", *bot3.cards, sep='\n ')
        print("Bot3's Hand =",bot3.value)
        print("Bot4's Hand:", *bot4.cards, sep='\n ')
        print("Bot4's Hand =",bot4.value)
        print("Bot5's Hand:", *bot5.cards, sep='\n ')
        print("Bot5's Hand =",bot5.value)
        print("\nPlayer's Hand:", *player.cards, sep='\n ')
        print("Player's Hand =",player.value)

    def player_folds(player,chips):
        print("Lose!")
        chips.lose_bet()
    def player_wins(player,chips):
        print("Win!")
        chips.win_bet()
    def bot_folds(bot,chips):
        print(f"{bot} folds!")
    def bot_wins(bot,chips):
        print(f"{bot} wins!")
        chips.lose_bet()

    
    players_chips = Chips()

    while True:

        print(f"Poker will now begin. \nPlayers Chips: {players_chips.total}")
        
        deck = Deck()
        deck.shuffle()
        
        player_hand = Hand()
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())
        
        bot1_hand = Hand()
        bot1_hand.add_card(deck.deal())
        bot1_hand.add_card(deck.deal())

        bot2_hand = Hand()
        bot2_hand.add_card(deck.deal())
        bot2_hand.add_card(deck.deal())
        
        bot3_hand = Hand()
        bot3_hand.add_card(deck.deal())
        bot3_hand.add_card(deck.deal())
        
        bot4_hand = Hand()
        bot4_hand.add_card(deck.deal())
        bot4_hand.add_card(deck.deal())
        
        bot5_hand = Hand()
        bot5_hand.add_card(deck.deal())
        bot5_hand.add_card(deck.deal())
        
        take_bet(players_chips)
        
        show_some(player_hand)









if __name__ == "__main__":
    main()
