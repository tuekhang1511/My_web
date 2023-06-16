from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
# from django.contrib.auth.models import User
from .models import EmailVerificationToken
from django.urls import reverse

from item.models import Category,Item
from core.models import User
from .forms import SignupForm, ChangeAvatarForm

from .models import user_avatar_upload_path

# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold=False)
    sold_items = Item.objects.filter(is_sold=True)
    catergories = Category.objects.all()
    context = {
        'categories' : catergories,
        'sold_items':sold_items,
        'items': items    
    }
    return render(request, 'core/index.html',context)

def contact(request):
    return render(request, 'core/contact.html')

import uuid
from .utils import *
@csrf_protect
def signup(request):
    if request.method == 'POST':
        # send_mail('Test Email', 'This is a test email', settings.EMAIL_HOST_USER, ['tienduongftu@gmail.com'])
        form = SignupForm(request.POST)

        if form.is_valid():
            # user = form.save()
            form.save(commit=False)
            
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            
            user_obj = User(username=username)
            user_obj.set_password(password)
            user_obj.save()
            
            verification_obj = EmailVerificationToken.objects.create(
                user = user_obj,
                token = str(uuid.uuid4())
            )
            send_email_token(email, verification_obj.token)
            return redirect('core:wait_for_verification')
            # form.save()
            # return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })

def verify(request, token):
    try:
        obj = EmailVerificationToken.objects.get(token=token)
        if obj.token == token:
            obj.is_verified = True
            obj.user.email_verified = True
            obj.user.save()
            obj.save()
            return redirect(reverse('core:index'))  # Replace with the desired URL
        else:
            return HttpResponse("Invalid token")
    except EmailVerificationToken.DoesNotExist:
        return HttpResponse("Invalid token")

def wait_for_verification(request):
    return render(request, 'core/wait_for_verification.html',{})


def profile(request, pk):
    user = User.objects.get(id=pk)

    return render(request, 'core/profile.html',{
        'user':user,
    })

import os
def change_avatar(request):
    if request.method == 'POST':
        form = ChangeAvatarForm(request.POST, request.FILES)

        if form.is_valid():
            user = request.user  # Retrieve the currently logged-in user
            # user.avatar.delete()
            user.avatar = form.cleaned_data['avatar']  # Assign the avatar value
            user.save()  # Save the user instance
            profile_url = reverse('core:profile', kwargs={'pk': user.pk})
            return redirect(profile_url)

    else:
        form = ChangeAvatarForm()

    return render(request, 'core/change_avatar.html', {
        'form': form
    })


    
