from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *

# Create your views here.


def index(request):
    return render(request, 'index.html')

def display_kitchenware(request):
    items = Kitchenware.objects.all()
    context = {
        'items': items,
        'header': 'Kitchenware',
    }
    return render(request, 'index.html', context)

def display_chicken(request):
    print(Chicken)
    items = Chicken.objects.all()
    context = {
        'items': items,
        'header': 'Chicken',
    }
    return render(request, 'index.html', context)
    

def add_item(request, cls):
    if request.method == "POST":
        form = cls(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = cls()
        return render(request, 'add_new.html', {'form' : form})


def add_kitchenware(request):
    return add_item(request, KitchenwareForm)

def add_chicken(request):
    return add_item(request, ChickenForm)

def edit_item(request, pk, model, cls):
    item = get_object_or_404(model, pk=pk)

    if request.method == "POST":
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = cls(instance=item)

        return render(request, 'edit_item.html', {'form': form})



def edit_kitchenware(request, pk):
    return edit_item(request, pk, Kitchenware, KitchenwareForm)


def edit_chicken(request, pk):
    return edit_item(request, pk, Chicken, ChickenForm)


def delete_kitchenware(request, pk):

    template = 'index.html'
    Kitchenware.objects.filter(id=pk).delete()

    items = Kitchenware.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)


def delete_chicken(request, pk):

    template = 'index.html'
    Chicken.objects.filter(id=pk).delete()

    items = Chicken.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)

