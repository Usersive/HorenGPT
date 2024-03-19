from django.shortcuts import redirect, render
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordResetForm


# Create your views here.
def login(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Invalid username or passsword")
            return redirect('login')
    else:
        return render(request, 'horen/login.html')
        
    

def forgotPassword(request):
    if request.method == "POST":
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save(request=request)
    else:
        form = PasswordResetForm()
        
    return render(request, 'horen/forgotPassword.html', {'form': form})

def register(request):
    if request.method =="POST":
        full_name = request.POST['full_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2:
            try:
                user = User.objects.create_user(username, email, password1)
                user.save()
                auth.login(request, user)
                return redirect('index')
            except:
                messages.error(request, "Error in creating an account")
                return redirect('register')
        else:
            # error_message = "Your password does not match"
            # return render(request, 'horen/register.html', {'error_message': error_message})
            messages.error(request, "Your password did not match")
            return redirect('register')
    return render (request, 'horen/register.html')

def logout(request):
   auth.logout(request)
   return redirect('index')