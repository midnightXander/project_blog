from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect 
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.forms import UserCreationForm
from blogs.forms import BioForm
from .models import Bio
from blogs.models import BlogPost
from django.contrib.auth.decorators import login_required

def logout_view(request):
    """logout the user"""
    logout(request)
    return HttpResponseRedirect(reverse("blogs:home"))

def register(request):
    """register a new user"""

    if request.method != "POST":
        """submit a blank registration form"""
        form=UserCreationForm()

    else:
        """process POST data"""
        form=UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user=form.save()
            authenticated_user=authenticate(username=new_user.username,
            password=request.POST['password1'])
            login(request,authenticated_user)

            return HttpResponseRedirect(reverse("blogs:home"))
    context={"form":form}
    return render(request,"users/register.html",context)  

@login_required
def profile(request,post_owner_id):
    """the user profile page"""
    bio=Bio.objects.filter(owner=post_owner_id)

    #if  bio.text != True :

    posts=BlogPost.objects.filter(owner= post_owner_id).order_by("-date_added")
    post1=posts[0] 
    
    context={"bio":bio,"posts":posts,"post1":post1}

    return render(request,"users/profile.html",context)







