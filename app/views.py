from django.shortcuts import render

def Home(request):
    return render(request,'app/index.htm')

def Heart(request):
    return render(request,'app/heart.htm')

def Malaria(request):
    return render(request,'app/malaria.htm')

def Liver(request):
    return render(request,'app/liver.htm')
