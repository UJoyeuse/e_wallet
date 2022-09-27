
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import *
from django.contrib import messages, auth
from django.http import HttpResponse

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone_number = request.POST['phone_number']
        account_no = request.POST['account_no']
        gender = request.POST['gender']
        dob = request.POST['dob']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
       

       
        if Client.objects.filter(username=username).exists():
                messages.warning(request, 'That username is taken')
                return redirect('register')
        elif Account.objects.filter(account_no=account_no):
                messages.warning(request, "The account already exists")
                return redirect('register')
        
        else:
                user = Client.objects.create_user(first_name=first_name, last_name=last_name,
                                                      phone_number=phone_number,gender=gender,dob=dob,
                                                      username=username, email=email, password=password,

                                                      )
                Account.objects.create(
                    owner=user, account_no=account_no,)
                return redirect("login")

        
    else:
        return render(request, 'pages/register.html')

def login_view(request):
     if request.method=='POST':
          
          username=request.POST['username']
          password=request.POST['password']
          user=auth.authenticate(request,username=username,password=password)
          if user is not None:
               auth.login(request,user)
               return redirect("dashboard")
          else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
     else:      
       return render(request, 'pages/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        # messages.success(request, 'You are now logged out')
        return redirect("login")


@login_required
def transfer(request):
  if request.method == "POST":
    account = request.POST["account"]
    amount = request.POST["amount"]
    senderUser= Account.objects.get(owner=request.user)
    receiverUser= Account.objects.get(account_no=account)

    if(int(amount)>=100000):          
     senderUser.balance = senderUser.balance - (int(amount)+1000)
     receiverUser.balance = receiverUser.balance + int(amount)
    elif(int(amount)>=10000 and int(amount)<=100000):
     senderUser.balance = senderUser.balance - (int(amount)+200)
     receiverUser.balance = receiverUser.balance + int(amount)
    else:
      senderUser.balance = senderUser.balance - int(amount)
      receiverUser.balance = receiverUser.balance + int(amount)

    receiverUser.save()
    senderUser.save()

    Transaction.objects.create(amount=amount, account_receiver=receiverUser,
                               account_sender=senderUser)
    return redirect("accounts")
    
  return render(request, 'pages/dashboard.html')

@login_required
def account_view(request):
    user =request.user
    accounts = Account.objects.filter(owner=user)
    return render(request, 'pages/all_accounts.html',{'accounts': accounts})

def about_view(request):
    return render(request, '_partials/about.html')


def contact_view(request):
    return render(request, '_partials/contact.html')

def index(request):
    return render(request, '_partials/index.html')




