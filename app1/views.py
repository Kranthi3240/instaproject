from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app1.models import post
# Create your views here.
@login_required(login_url="/admin")
def create(request):
    if request.method=="POST":
        image=request.FILES['image']
        capt=request.POST.get('cap')
        u=request.user
        obj=post(person=u,photo=image,caption=capt)
        obj.save()
    return render(request,'create.html')


def home(request):
    objs=post.objects.all()
    if request.method=="POST":
        a=request.POST.get('search')
        results=post.objects.filter(caption__icontains=a)
        return render(request,'index.html',{'res':results})
    return render(request,'index.html',{'posts':objs})