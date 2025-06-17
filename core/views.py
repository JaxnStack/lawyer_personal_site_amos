from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def practice(request):
    return render(request, 'practice.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')
