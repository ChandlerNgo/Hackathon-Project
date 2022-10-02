from django.shortcuts import render
from CardGamesL.blackjack import Deck

def index(request):
    return render(request,"index.html")

def blackjack(request):
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
            blackjack.hit(blackjack.getDeck(),blackjack.getPlayerHand())
        else:
            chips = 0
        request.session['chips'] = chips
    parameters = {
        "current_card":current_card,
        "chips":request.session['chips'],
        "player_cards":["../static/CardgameDjangoApp/images/cards/Clovers/2-clover.png","../static/CardgameDjangoApp/images/cards/Clovers/3-clover.png"]
    }
    return render(request, "blackjack.html",parameters)

def poker(request):
    return render(request, "poker.html")

def yablon(request):
    return render(request, "yablon.html")

def war(request):
    return render(request, "war.html")

# Create your views here.