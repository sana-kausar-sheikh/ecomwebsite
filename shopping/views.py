from django.shortcuts import render
from .models import Product
from .models import User
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth import login as auth_login
from .forms import CustomUserCreationForm
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages


def index1(request):
    product_objects = Product.objects.all()

    #search code
    item_value = request.GET.get('item_value')
    if item_value != '' and item_value is not None:
        product_objects = product_objects.filter(title__icontains=item_value)

    
    #paginator code
    paginator = Paginator(product_objects,4)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)

# Create your views here.
    return render(request,'index1.html',{"product_objects":product_objects})


def detail(request,id):
    product_object= Products.objects.get(id=id)
    return render(request,'detail.html',{"product_object":product_object})


def signup(request):
    if request.method == 'POST':
            first_name= request.POST.get('first_name')
            last_name= request.POST.get('last_name')
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = User.objects.filter(username=username)

            if user.exists():
                 messages.info(request,"Username already taken")
                 return redirect('/signup/')

            user = User.objects.create(
                first_name = first_name,
                last_name = last_name,
                username= username,
            )
            
            user.set_password(password)
            user.save()
            messages.info(request,"Account created Successfully")
            return redirect('/signup/')
    
    return render(request, 'signup.html')

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
             messages.info(request,"Invalid username")
             return redirect('/login/')
        
        user = authenticate(username=username,password=password)

        if user is None:
            messages.info(request,"Invalid password")
            return redirect('/login/') 
        else:
            auth_login(request,user)
            return redirect('/index1/') 
    return render(request, 'login.html')