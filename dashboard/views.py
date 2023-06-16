from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from item.models import Item
# Create your views here.

@login_required
def index(request):
    your_items = Item.objects.filter(created_by=request.user).filter(is_sold=False)

    your_owned_items = Item.objects.filter(was_owned_by=request.user)

    return render(request, 'dashboard/index.html',{
        'your_items': your_items,
        'your_owned_items':your_owned_items,
    })


