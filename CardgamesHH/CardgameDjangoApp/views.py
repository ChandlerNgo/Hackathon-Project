from django.shortcuts import render

def index(request):
    return render(request,"index.html")

def blackjack(request):
    current_card = "7 of Hearts"
    chips = request.session.get('chips', 0)
    if request.method == 'POST':
        if request.POST.get("1_chip"):
            request.session['chips'] = chips + 1
        elif request.POST.get("5_chip"):  # You can use else in here too if there is only 2 submit types.
            request.session['chips'] = chips + 5
        elif request.POST.get("10_chip"):  # You can use else in here too if there is only 2 submit types.
            request.session['chips'] = chips + 10
        elif request.POST.get("50_chip"):  # You can use else in here too if there is only 2 submit types.
            request.session['chips'] = chips + 50
        elif request.POST.get("100_chip"):  # You can use else in here too if there is only 2 submit types.
            request.session['chips'] = chips + 100
    parameters = {
        "current_card":current_card,
        "chips":chips
    }
    return render(request, "blackjack.html",parameters)

def poker(request):
    return render(request, "poker.html")

def texasholdem(request):
    return render(request, "texasholdem.html")

def war(request):
    return render(request, "war.html")

# Create your views here.