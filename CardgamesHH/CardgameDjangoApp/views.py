from django.shortcuts import render

def index(request):
    return render(request,"index.html")

def blackjack(request):
    dealer = "Sami, Chandler, Laith, Dhruv"
    current_card = "7 of Hearts"
    parameters = {
        "dealer":dealer,
        "current_card":current_card
    }
    return render(request, "blackjack.html",parameters)

def poker(request):
    return render(request, "poker.html")

def texasholdem(request):
    return render(request, "texasholdem.html")

def war(request):
    return render(request, "war.html")

# Create your views here.
