from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages 
from django.contrib.auth.forms import UserCreationForm
import json

@login_required
def main_page(request):
    context = {}
    if request.method == 'POST':
        upload_file = request.FILES.get('mindmap')
        try:
            mindmap = json.load(upload_file) 
            context = {'mindmap' : mindmap}
        except: pass
        return render(request, 'index.html', context)
    return render(request, 'get_mindmap.html')




def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username').strip()
        password = request.POST.get('password').strip()
        user = authenticate(request, username=username, password=password) #  get account from db
        if user is None: 
            messages.add_message(request, messages.ERROR,"User not found") # if account not exist
            return render(request, 'login.html')
        else: 
            login(request,user)    
            return redirect('/')    
    else:
        return render(request, 'login.html')    



def registraion_page(request):
    if request.method == "POST":
        login = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1==password2:
            try:
                user = User.objects.create_user(username = login.strip(),password = password1.strip()) 
                user.save()
                messages.add_message(request, messages.SUCCESS,"User was created")       
                return redirect('/login')
            except: 
                messages.add_message(request, messages.ERROR,"Unavailable Login or Password")
        else:
            messages.add_message(request, messages.ERROR,"Passwords don't match!")        
    return render(request, 'registration.html', {'form': UserCreationForm()}) 
     