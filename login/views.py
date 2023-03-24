from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer

def index(request):
    return render(request, 'login/index.html')
def register(request):    
    if request.method =="POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        user_name = request.POST.get('user_name','')
        password = request.POST.get('password','')
        customer = Customer(first_name= first_name, last_name= last_name, user_name = user_name, password = password)
        customer.save()
    return render(request, 'login/register.html')        
def home(request):
    return render(request, 'login/home.html')    
