from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login ,logout,authenticate
from users.forms import coustomregistrationform,Assignroleform,creategroupform
from django.contrib import messages
from django.contrib.auth.models import User,Group
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.decorators import login_required,user_passes_test

def is_admin(user):
    return user.is_superuser or user.groups.filter(name='Admin').exists()
# Create your views here.
def sing_up(request):
    form= coustomregistrationform()
    if request.method =="POST":
        form = coustomregistrationform(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get('password'))

            user.is_active = False   
            user.save()
            messages.success(request,"Confarmation Mail Send your Account")
            return redirect("login")
    return render(request,'Registration/register.html',{"form":form})




def login_in(request):
    if request.method =="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(request,username = username ,password=password)
       
        if user is not None:
            login(request , user)
            return redirect("All_dashboard")
    

    return render(request,'Registration/login.html')

@login_required
def out(request):
    if request.method=="POST":
        logout(request)
        return redirect("login")
    
    return render(request,"Registration/register.html")

def activate_user(request,user_id,token):
    try:
      user = User.objects.get(id = user_id)
      if default_token_generator.check_token(user,token):
        user.is_active =True
        user.save()
        return redirect("login")
      else:
          return HttpResponse("Invalid id")
    except User.DoesNotExits:
        return HttpResponse("User Not Found")

    



@user_passes_test(is_admin,login_url="no-permission")
def admin_dashboard(request):
    users = User.objects.all()

    return render(request,"admin/control.html",{"users":users})

@user_passes_test(is_admin,login_url="no-permission")
def assign_role(request,user_id):
    user = User.objects.get(id=user_id)
    form = Assignroleform()

    if request.method=="POST":
        form = Assignroleform(request.POST)
        if form.is_valid():
            role = form.cleaned_data.get('role')
            user.groups.clear()
            user.groups.add(role)
            messages.success(request,f"user {user.username} has been assiged to {role.name} role")
            return redirect("admin")
        
    return render(request,"admin/ChangeRoleform.html",{"form":form})

@user_passes_test(is_admin,login_url="no-permission")
def create_group(request):
    form = creategroupform()
    if request.method =="POST":
        form = creategroupform(request.POST)
        if form.is_valid():
            group = form.save()
            messages.success(request,f"Group {group.name} has been created succesfull")
            return redirect('create_group')
    return render(request,"admin/Create_group.html",{"form":form})

@user_passes_test(is_admin,login_url="no-permission")
def delet_group(request,id):
    group  = Group.objects.get(id=id)
    if request.method=="POST":
        group.delete()
        messages.success(request,f"group {group.name} delet successfully ")
        return redirect("group_list")
    return render(request,"admin/delet_group.html",{"group":group})

@user_passes_test(is_admin,login_url="no-permission")
def group_list(request):
    group = Group.objects.all()
    return render(request,"admin/Group_list.html",{"group":group})

@user_passes_test(is_admin,login_url="no-permission")
def delet_user(request,id):
    
    if request.method=="POST":
        users =User.objects.get(id=id)
        
        users.delete()
        return redirect("admin")
    else:
        return redirect("admin")

    

    