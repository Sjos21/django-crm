from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from .forms import Signupform, Addrecordform
from .models import Record


def home(request):
    records=Record.objects.all()
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "you have been logged in")
            return redirect('home')
        else:
            messages.success(request, "there was an error logging in!")
            return redirect('home')
    else:
        return render(request, 'home.html', {'records':records})

def logout_user(request):
    logout(request)
    messages.success(request, "you have been logged out!!")
    return redirect('home')

def register_user(request):
    if request.method=="POST":
        form=Signupform(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "you have registered!")
            return redirect('home')
    else:
        form=Signupform()
        return render(request, 'register.html', {'form':form })
        
    return render(request, 'register.html', {'form':form })


def customer_record(request,pk):
	if request.user.is_authenticated:
		customer_record = Record.objects.get(id=pk)
		return render(request, 'record.html', {'customer_record':customer_record})
	else:
		messages.success(request, "You Must Be Logged In To View That Page")
		return redirect('home')
     
def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it=Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Deleted the record successfully!")
        return redirect('home')
    else:
        messages.success(request, "You Must Be Logged In To View That Page")
        return redirect('home')
    
def add_record(request):
    form=Addrecordform(request.POST or None)
    if request.user.is_authenticated:
        if request.method=="POST":
            if form.is_valid():
                add_record=form.save()
                messages.success(request, "Record has been added!")
                return redirect('home')
        return render(request, 'add_record.html', {'form':form}) 
    else:
        messages.success(request, "You must be logged in")
        return redirect('home')
        
         
    
def update_record(request, pk):
    if request.user.is_authenticated:
        current_record=Record.objects.get(id=pk)
        form =Addrecordform(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record has been updated")
            return redirect('home')
        return render(request, 'update_record.html',{'form':form})
    else:
        messages.success(request, "You must be logged in")
        return redirect('home')


     