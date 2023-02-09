from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import userForms, UserCreationForm
from .models import Work
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def index(request):
    #return redirect('login')
    if not request.user.is_authenticated:
        # return render(request,"main/login.html",{
        #     'form':userForms()
        # })
        return redirect('login')
    return redirect('home')

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request, user)
            # user_object = Work.objects.get(user = user)
            # item_list = user_object.my_list.split(',')
            # if len(item_list[0]) == 0:
            #     item_list = []
            # return render(request,"main/home.html",{
            #     'item_list':item_list
            # })
            return redirect('home')
        else:
            return render(request,"main/login.html",{
                'form':userForms(),
                'message':"Invalid Credentials",
            })
    return render(request,"main/login.html",{
        'form':userForms()
    })

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            user = User.objects.get(username = username)
            object = Work(user = user, my_list = '')
            object.save()
            messages.info(request, "You have been registered, Try Logging in")
            return redirect('login')
        else:
            return render(request,"main/register.html",{
                'form':UserCreationForm(),
                'message':"Username taken"
            })
        
    return render(request,"main/register.html",{
        'form':UserCreationForm()
    })

def home_view(request):
    user_object = Work.objects.get(user = request.user.id)
    item_list = user_object.my_list.split(',')

    if len(item_list[0]) == 0:
        item_list = []
    return render(request,"main/home.html",{
        'user':request.user,
        'item_list':item_list
    })

def add_view(request):
    if request.method == "POST":
        new_item = request.POST['new_item']
        user = Work.objects.get(user = request.user)
        items_list_string = user.my_list
        if len(items_list_string) == 0:
            items_list_string = new_item
        else:
            items_list_string = items_list_string + "," + new_item
        user.my_list = items_list_string
        user.save()
        return render(request,"main/add.html",{
            'message':"New Item added",
            'user':request.user
        })
    return render(request,"main/add.html",{
        'user':request.user
    })

def remove_view(request):
    if request.method == "POST":
        item = request.POST['item']
        user = request.user
        object = Work.objects.get(user = user)
        item_list = object.my_list.split(',')
        item_list.remove(item)
        item_list_string = ','.join(item_list)
        object.my_list = item_list_string
        object.save()
        return render(request,"main/remove.html",{
            'message':"Item Removed"
        })
    return render(request,"main/remove.html")

def logout_view(request):
    logout(request)
    return redirect('login')

        
