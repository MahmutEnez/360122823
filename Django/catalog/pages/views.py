from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'pages/index.html')
    
def shop(request):
    return render(request,'pages/shop.html')
    
def detail(request):
    return render(request,'pages/detail.html')    

def cart(request):
    return render(request,'pages/cart.html')

def checkout(request):
    return render(request,'pages/checkout.html')

def contact(request):
    return render(request,'pages/contact.html')
    
