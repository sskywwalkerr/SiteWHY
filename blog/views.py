from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
def shop(request):
    return render(request, 'shop.html')
def news(request):
    return render(request, 'news.html')
def team(request):
    return render(request, 'team.html')
def categories(request):
    return render(request, 'categories.html')
def contact(request):
    return render(request, 'contact.html')

