from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
import logging  
from datetime import datetime
from blogApp.models import Blog_Post, Comments 


logger = logging.getLogger(__name__)

# Create your views here.
def index (request):
    articles=Blog_Post.objects.all()
    context={
        'data':articles
    }
    return render (request,"index.html", context)

def about (request):
    return render (request,"about.html")

def login_request (request):
    if request.method=='GET':
        return render (request, "login.html")
    
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user = authenticate (username=username, password=password)

        if user is not None:
            login (request,user)

        return  redirect ('blogApp:home')
    
def logout_request (request):
    logout(request)
    return redirect('blogApp:home')

def signup_request (request):
    if request.method=='GET':
        return render (request, "signup.html")
    
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        user_exist=False

        try:
            User.objects.get(username=username)
            user_exist=True
        except:
            logger.debug("{} is new user".format(username))

        if not user_exist:
            user=User.objects.create_user(username=username, email=email, password=password)
            login(request,user)
            return redirect('blogApp:home')
        else:
            return render ('blogApp:home')

def create_post (request):
    if request.method=='GET':
        return render (request, 'new_post.html')
    
    if request.method=='POST':
        title=request.POST['title']
        content=request.POST['content']
        username=request.user.username
        date=datetime.now()

        post = Blog_Post(user_name=username, title=title, post_content=content, date=date)
        post.save()
        return redirect ('blogApp:home')
        
    
def display_post (request, number):
    if request.method=='GET':
        post = Blog_Post.objects.get(id=number)
        comm = Comments.objects.filter(art_id=post)
        context={
            'post':post,
            'comm':comm
        }
        #return HttpResponse (comm)
        return render (request, 'display.html', context)
    
    if request.method=='POST':
        comment=request.POST['comment']
        username=request.user.username
        art_id = Blog_Post.objects.get(id=number)
        comm=Comments(user_name=username, comment=comment, art_id=art_id)
        comm.save()
        return redirect('blogApp:home')
    
def update_post (request, number):
    if request.method=='GET':
        post = Blog_Post.objects.get(id=number)
        context = {'post': post}
        return render (request, 'edit_post.html', context)
    
    if request.method=='POST':
        title=request.POST['title']
        content=request.POST['content']
        post = Blog_Post.objects.filter(id=number).update(title=title, post_content=content)
        return redirect('blogApp:home')
    
def delete_post (request, number):
        post = Blog_Post.objects.get(id=number).delete()
        return redirect('blogApp:home')

def user_page (request, name):
    posts = Blog_Post.objects.filter(user_name=name)
    email=""
    if (request.user.is_authenticated):
        email=request.user.email
    context={
        'curr':request.user.username,
        'look':name,
        'posts':posts,
        'email':email
    }
    #return HttpResponse(context['email'])
    return render (request, 'profile.html', context)

def change_details (request, type):
    if request.method=='GET':
        if type=='name':
            context={'type':'name'}
        elif type=='pass':
            context={'type':'pass'}
        elif type=='email':
            context={'type':'email'}
        return render (request, "changeDeets.html", context)
    
    if request.method=='POST':
        user_name = request.user.username
        person = User.objects.get(username=user_name)
        if type=='name':
            new_name=request.POST['username']
            Blog_Post.objects.filter(user_name=user_name).update(user_name=new_name)
            Comments.objects.filter(user_name=user_name).update(user_name=new_name)
            person.username=new_name
        elif type=='pass':
            new_pass=request.POST['password']
            person.password=new_pass
        elif type=='email':
            new_email=request.POST['email']
            person.email=new_email
        
        person.save()
        
        return redirect('blogApp:home')
