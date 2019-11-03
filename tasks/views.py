from django.shortcuts import render, redirect, reverse
from .forms import ItemForm
from django.contrib import auth, messages
from .models import Item


# Create your views here.
def create_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Your task has been created successfully!")
            return redirect(reverse('create_item'))
        else:
            return render(request, 'tasks/create_item_template.html', {
            "form":form
        })
    else:
        form = ItemForm()
        return render(request, 'tasks/create_item_template.html', {
            "form":form
        })

def show_items(request):
    items = Item.objects.all()
    return render(request, 'tasks/show_items.template.html', {
        "items": items
    })