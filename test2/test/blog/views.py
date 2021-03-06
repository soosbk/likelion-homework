from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from .models import Blog
# Create your views here.
def home(request):
    blogs=Blog.objects.all()
    return render(request,'home.html',{'blogs':blogs})



def detail(request,id):
    blog=get_object_or_404(Blog,pk=id)
    return render(request,'detail.html',{'blog':blog})


def new(request):
    return render(request,"new.html")
    

def create(request):
    new_blog=Blog()
    
    new_blog.title=request.POST['title']
    new_blog.publish=request.POST['publish']
    new_blog.body=request.POST['body']
    new_blog.create_at=timezone.now()\

    try:
        new_blog.image=request.FILES['image']
    except:
        pass
    
    new_blog.save()

    return redirect('detail', new_blog.id)


def edit(request,id):
    edit_blog=Blog.objects.get(id=id)
    return render(request, 'edit.html',{'blog':edit_blog})  


def update(request, id):
    update_blog=Blog.objects.get(id=id)
    update_blog.title=request.POST['title']
    update_blog.publish=request.POST['publish']
    update_blog.body=request.POST['body']
    update_blog.create_at=timezone.now()
    update_blog.save()

    return redirect('detail', update_blog.id)



def delete(request, id):
    delete_blog=Blog.objects.get(id=id)
    delete_blog.delete()
    return redirect('home')