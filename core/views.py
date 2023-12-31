from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from item.models import Item, Category
from django.contrib import auth

from .forms import SignupForm

# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    category = Category.objects.all()
    return render(request, 'core/index.html',{'items':items,'category':category,})

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html',{
        'form':form
        })

def login(request):
    return render(request, 'core/login.html')

# @login_required
# def logout(request):
#     for sesskey in request.session.keys():
#         del request.session[sesskey] 
#     auth.logout(request)
#     return render(request, 'core/index.html')
@login_required
def logout(request):
    session_keys = list(request.session.keys())
    for sesskey in session_keys:
        del request.session[sesskey]
    auth.logout(request)
    return redirect(request, '/login/')