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
        self.aces = 0    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1 

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

    def hit(deck,hand):
        hand.add_card(deck.deal())
        hand.adjust_for_ace()

    def hit_or_stand(deck,hand):
        global playing
        
        while True:
            x = input("Will you hit or stand? ").lower()
            
            if x[0] == 'h':
                hit(deck,hand)
            elif x[0] == 's':
                print("Player standing. Dealer will play.")
                playing = False
                break
            else:
                print("Please enter either hit or stand.")
                continue
            break

    def show_some(player,dealer):
        print("Dealer's Hand:")
        print(" <card hidden>")
        print('',dealer.cards[1])  
        print("\nPlayer's Hand:", *player.cards, sep='\n ')
        
    def show_all(player,dealer):
        print("Dealer's Hand:", *dealer.cards, sep='\n ')
        print("Dealer's Hand =",dealer.value)
        print("\nPlayer's Hand:", *player.cards, sep='\n ')
        print("Player's Hand =",player.value)

    def player_busts(player,dealer,chips):
        print("Bust!")
        chips.lose_bet()
    def player_wins(player,dealer,chips):
        print("Win!")
        chips.win_bet()
    def dealer_busts(player,dealer,chips):
        print("Dealer bust!")
        chips.win_bet()
    def dealer_wins(player,dealer,chips):
        print("Dealer win!")
        chips.lose_bet()
    def push(player,dealer):
        print("Tie! It's a push.")

    players_chips = Chips()

    while True:

        print(f"Blackjack will now begin. Get as close to 21 as you can without going over!\n\
        Dealer hits until she reaches 17. Aces count as 1 or 11.\n  Players Chips: {players_chips.total}")
        
        deck = Deck()
        deck.shuffle()
        
        player_hand = Hand()
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())
        
        dealer_hand = Hand()
        dealer_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())
        
        take_bet(players_chips)
        
        show_some(player_hand,dealer_hand)
        
        while playing:  
            hit_or_stand(deck,player_hand)
            
            show_some(player_hand,dealer_hand)
            
            if player_hand.value > 21:
                player_busts(player_hand,dealer_hand,players_chips)
                break
        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
        if player_hand.value <= 21:
            while dealer_hand.value < 17:
                hit(deck,dealer_hand)
            
            show_all(player_hand,dealer_hand)
            
            if dealer_hand.value > 21:
                dealer_busts(player_hand,dealer_hand,players_chips)
            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand,dealer_hand,players_chips)
            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand,dealer_hand,players_chips)
            else:
                push(player_hand,dealer_hand)
        
        print("\nPlayers chips total:",players_chips.total)
        
        new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
        
        if new_game[0].lower()=='y':
            playing=True
            continue
        else:
            print("Thanks for playing!")
            break



if __name__ == "__main__":
    main()

