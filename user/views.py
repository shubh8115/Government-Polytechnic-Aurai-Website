from django.shortcuts import render
from .models import *
def index(request):
    data=tblbranch.objects.all().order_by("-id")[0:4]
    pdata=tblplacements.objects.all().order_by("-id")[0:4]
    ndata=new.objects.all().order_by("-id")[0:6]
    md={"bdata":data,"pdata":pdata,"ndata":ndata}
    return render(request,"user/index.html",md)


    
def about(request):
    return render(request,"user/about.html")


def contact(request):
    md={}
    if request.method=="POST":
        a=request.POST.get("name")
        b=request.POST.get("mobile")
        c=request.POST.get("email")
        d=request.POST.get("msg")
        tblcontact(name=a,mobile=b,email=c,message=d).save()
        md={"msg":"Data saved successfully.............."}

        
    return render(request,"user/contact.html",md)    

def gallery(request):
    data=tblgallery.objects.all().order_by("-id")
    md={"rows":data}
    return render(request,"user/gallery.html",md)


def team(request):
    data=tblteam.objects.all().order_by("-id")
    md={"tdata":data}
    return render(request,"user/team.html",md)

def branch(request):
    data=tblbranch.objects.all().order_by("-id")
    md={"bdata":data}    
    return render(request,"user/branch.html",md)

def placements(request):
    
    pdata=tblplacements.objects.all().order_by("-id")
    md={"pdata":pdata}    
    return render(request,"user/placements.html",md)  

def facilities(request):
    
    data=tblfacilities.objects.all().order_by("-id")
    md={"fdata":data}
    return render(request,"user/facilities.html",md)


def developer(request):
    return render(request,"user/developer.html")           


