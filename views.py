# from django.shortcuts import render
# from .models import LogIn

from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import check_password
from django.http import JsonResponse
from django.contrib import messages
from .models import Books
from .models import User

# Create your views here.

# def Log(request):
#     return render(request, 'UserBooks/Log.html')

def SignUp(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirmpassword')
        email = request.POST.get('email')
        user_type = request.POST.get('userType')
        if password != confirmPassword:
            messages.error(request, "Passwords do not match")
            return render(request, 'Pages/signup.html')

        if user_type == 'admin':            
            new_user = User.objects.create(
                username=username,
                password=password,
                confirmPassword=confirmPassword,
                email=email,
                is_admin = True
            )
            new_user.save()

            return redirect('AdminBooks')  
        else:
            new_user = User.objects.create(
                username=username,
                password=password,
                confirmPassword=confirmPassword,
                email=email,
                is_admin = False
            )
            new_user.save()
            return redirect('UserBooks')
    return render(request, 'Pages/signup.html' )

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_exists = False
        for user in User.objects.all():
            if user.username == username:
                user_exists = True
                if user.password == password:
                    data = User(username=username,password=password,email=user.email,is_admin=user.is_admin)
                    if user.is_admin:
                        return redirect('AdminBooks')  
                    else:
                        return redirect('UserBooks')  
                else:
                    messages.error(request, "Invalid password")
                    break
        if not user_exists:
            messages.error(request, "User does not exist. Sign up first.")
    return render(request, 'Pages/login.html')


