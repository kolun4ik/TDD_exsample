from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item


def home_page(request):
    """домашняя страница"""
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/lists/any_url/')
    items = Item.objects.all()
    return render(request, 'home.html')

def view_list(request):
    """представление списка"""
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})