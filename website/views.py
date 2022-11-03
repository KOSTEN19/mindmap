from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages 
from django.contrib.auth.forms import UserCreationForm
import json

# Create your views here.
@login_required
def main_page(request):
    context = {}
    mindmap = ''
    if request.method == 'POST':
        mindmap =''
        upload_file = request.FILES.get('mindmap')
        #try:
        #    print(upload_file)
        #    mindmap = json.load(upload_file)
        mindmap = [["Python",["python2.7","python3.7","python3.8"]] ,[ "C++",["C++11","C++15","C++17"]],[ "JAVA",["Хуйня","Хуйня"]]]
        context = {'mindmap' : mindmap}
        #except : 
            #messages.add_message(request, messages.ERROR,"File not available")
        return render(request, 'index.html', context)
        
    print("mindmap->",mindmap)
    print("context->",context)    
    return render(request, 'get_mindmap.html', context)




def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username').strip()
        password = request.POST.get('password').strip()
        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.add_message(request, messages.ERROR,"User not found")
            return render(request, 'login.html')
        login(request,user)    
        return redirect('/')    
    else:
        return render(request, 'login.html')

def logout_page(request):
    logout(request)
    return redirect('/')


def registraion_page(request):
    if request.method == "POST":
        login = request.POST.get('username')
        pasw = request.POST.get('password1')
        try:
            user = User.objects.create_user(username = login.strip(),password = pasw.strip())
            user.save()
            messages.add_message(request, messages.SUCCESS,"User was created")
            return redirect('/login')
        except:    
            messages.add_message(request, messages.ERROR,"Unavailable Login or Password")
        
        print(1)
        
        print(2)   
       
    return render(request, 'registration.html', {'form': UserCreationForm()}) 
     