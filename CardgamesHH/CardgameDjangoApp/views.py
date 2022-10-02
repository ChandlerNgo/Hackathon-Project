from django.shortcuts import render
from CardGamesL.blackjack import *

def index(request):
    return render(request,"index.html")

def blackjack(request):
    suits = ('hearts', 'diamond', 'spades', 'clover')
    ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
    values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
            'Queen':10, 'King':10, 'Ace':11}
    pic = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':'J',
            'Queen':'Q', 'King':'K', 'Ace':'A'}
    current_card = "7 of Hearts"
    chips = request.session.get('chips', 0)
    if request.method == 'POST':
        if request.POST.get("1_chip"):
            chips += 1
        elif request.POST.get("5_chip"):  # You can use else in here too if there is only 2 submit types.
            chips += 5
        elif request.POST.get("25_chip"):  # You can use else in here too if there is only 2 submit types.
            chips += 25
        elif request.POST.get("50_chip"):  # You can use else in here too if there is only 2 submit types.
            chips += 50
        elif request.POST.get("100_chip"):  # You can use else in here too if there is only 2 submit types.
            chips += 100
        elif request.POST.get("hit"):
            player_cards = []
            suit = random.choice(suits)
            rank = random.choice(ranks)
            rank = pic[rank]
            if rank in ("J","Q","K","A"):
                rank = rank.lower()
            player_cards.append(f"{rank}-{suit}")
            player_hands = []
            for i in player_cards:
                player_hands.append(f"../static/CardgameDjangoApp/images/cards/{i}.png")
                # Check to see if the player busts
            parameters = {
                "current_card":current_card,
                "chips":request.session['chips'],
                "player_cards":player_hands
            }
            return render(request, "blackjack.html",parameters)
        else:
            chips = 0
        request.session['chips'] = chips
    parameters = {
        "current_card":current_card,
        "chips":request.session['chips'],
    }
    return render(request, "blackjack.html",parameters)

def poker(request):
    return render(request, "poker.html")

def yablon(request):
    return render(request, "yablon.html")

def war(request):
    return render(request, "war.html")

# Create your views here.