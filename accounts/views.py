from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.
def signup(request) :
    if request.method == "POST":

        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        password1 = request.POST["password_1"]
        password2 = request.POST["password_2"]
        email = request.POST["email"]

        if password1 == password2 :
            if User.objects.filter(username = username).exists():
                messages.info(request, "Username Taken")
                return redirect("signup")
            elif  User.objects.filter(email=email).exists():
                messages.info(request, "Email Taken")     
                return redirect("signup")
            else :     
                user = User.objects.create_user(username = username, password = password1, email = email, first_name = first_name, last_name = last_name)
                user.save()

                messages.info(request, "User Created Successfully")
                return redirect("signup")
        else : 
            messages.info(request, "Password Not Matching")
        return redirect("signup")
    else:

        return render(request, "signup.html")
    