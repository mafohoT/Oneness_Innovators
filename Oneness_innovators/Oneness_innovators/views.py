from django.shortcuts import render

def home(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def login(request):
    return render(request,'Login.html')

def test(request):
    return render(request,'test.html')

def home2(request):
    return render(request,'home.html')

def registration(request):
    return render(request,'registration.html')
