from django.shortcuts import render ,redirect
from django.db.models import Q
from django.contrib import messages
from django.core.exceptions import ValidationError
from .models import CustomUser
# Create your views here.
from django.contrib.auth import authenticate, login


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        type_ = request.POST.get('category')

        if username and email and password and type_:
            existing_users = CustomUser.objects.filter(Q(username=username) | Q(email=email))
            if existing_users:
                 messages.error(request, 'email  incorrect')
               
                # raise ValidationError('Username or email is already taken.')
            else:
                user = CustomUser(username=username, password=password, email=email, role=type_)
                user.save()
                return redirect('login')
        else:

           
            messages.error(request, 'enter all data')

        


    


    return render(request,'register.html')



def log (request):


    if request.method =='POST':
        username1 = request.POST.get('username')
        password1 = request.POST.get('password')
        print(username1,password1)
        #user=authenticate(request,username=username1,password=password1)
        user=CustomUser.objects.filter(Q(username=username1) | Q(password=password1))
        print(user)
        if user is not None:
           # login(request,user) 
            return redirect('home')
        
        else:
            messages.error(request,'user not found')


      
    



    return render(request , 'log.html')


def home (request):

   return render(request,'home.html')
