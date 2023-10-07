from django.shortcuts import render
from .models import BlogPost
from .forms import PostForm
from django.http import HttpResponseRedirect,Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def home(request):
    """home page showing all posts made"""
    posts=BlogPost.objects.order_by('-date_added')
    #to make users to see only their posts, 
    #posts=BlogPost.objects.filter(owner=request.user).oder_by('-date_added')
    context={'posts':posts}
    return render(request,"blogs/home.html",context)

@login_required
def add_post(request):
    """enable a form for the user to add a post"""

    if request.method != "POST":
        """no data submitted,generate blank form """
        form=PostForm()

    else :
        """post data submitted, process data """ 
        form=PostForm(data=request.POST)

        if form.is_valid():
            new_post=form.save(commit=False)
            new_post.owner=request.user
            new_post.save()
            return HttpResponseRedirect(reverse("blogs:home"))

    context={'form':form}
    return render(request,"blogs/add_post.html",context)       

@login_required
def edit_post(request,post_id):
    """edit an existing post"""
    post=BlogPost.objects.get(id=post_id)
    
    if post.owner != request.user:
        raise Http404

    if request.method !="POST":
        """generate already filled form from previous request"""
        form=PostForm(instance=post)

    else:
        """new post data submitted, process"""
        form=PostForm(instance=post,data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("blogs:home"))
    context={'form':form,'post':post}
    return render(request,"blogs/edit_post.html",context)

