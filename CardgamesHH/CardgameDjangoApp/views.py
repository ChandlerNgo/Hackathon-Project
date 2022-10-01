from django.shortcuts import render

def index(request):
    return render(request,"index.html")

def blackjack(request):
    return render(request, "blackjack.html")

def poker(request):
    return render(request, "poker.html")

def texasholdem(request):
    return render(request, "texasholdem.html")

def war(request):
    return render(request, "war.html")

# Create your views here.
