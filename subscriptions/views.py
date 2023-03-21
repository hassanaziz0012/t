from django.shortcuts import render
from .forms import SubsciptionForm

def subscribe(request):
    # view to display subscription form 
    form = SubsciptionForm()
    return render(request,"subscriptions/subscriptions.html", {"form":form})