from django.shortcuts import render

def home(request):
    context = {}
    hello = 'hello'
    
    return render(request,'EnergyCost/home.html' , context=context)
