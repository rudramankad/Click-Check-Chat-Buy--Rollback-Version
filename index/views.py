from django.shortcuts import render, redirect
from .models import Item
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
import os
from django.shortcuts import render, get_object_or_404

def index(request):
    items = Item.objects.all()
    return render(request, 'homepage.html', {'items': items})

def buypage(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return render(request, 'buypage.html', {'item': item})

def elcetronic(request):
    items = Item.objects.all()
    return render(request, 'electronic.html', {'items': items})

def aboutus(request):
    return render(request, 'aboutus.html')

def uploaditem(request):
    if request.method == 'POST':
        # Get form data
        item_name = request.POST.get('item_name')
        category = request.POST.get('category')
        description = request.POST.get('description')
        price = request.POST.get('price')
        condition = request.POST.get('condition')
        photo = request.FILES.get('photos')

        current_user_id = request.user.id
        current_user = User.objects.get(pk=current_user_id)

        # Validate and save data
        if item_name and category and description and price and condition:
            try:
                price = float(price)
            except ValueError:
                messages.error(request, 'Invalid price format')
                return redirect('index:uploaditem')

            new_item = Item(
                name=item_name,
                category=category,
                description=description,
                price=price,
                condition=condition,
                seller_id=current_user,
                photos=photo
            )

            new_item.save()
            messages.success(request, 'Item added successfully')
            return redirect('index:index')
        else:
            messages.error(request, 'Please fill in all required fields')
            return redirect('uploaditem')
    else:
        return render(request, 'uploadpage.html')

def chat(request):
    return render(request, 'chatbot.html')

def my_profile(request):
    user = request.user
    uploaded_items = Item.objects.filter(seller_id=user)

    context = {
        'user': user,
        'uploaded_items': uploaded_items,
    }

    return render(request, 'myprofile.html', context)
