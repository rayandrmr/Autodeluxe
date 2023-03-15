from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError

from backapp.models import adminreg, categorydb, productdb, contactdb, productde
from frontend.views import homepage
from django.contrib import messages


# Create your views here.
def indexpage(request):
    return render(request,"index.html")
# def fhomepage(request):
#     return render(request,"home.html")

def admin(req):
    return render(req,"addadmin.html")
def saveadminpage(request):
    if request.method == "POST":
        user = request.POST.get('username')
        em = request.POST.get('email')
        mob = request.POST.get('mobile')
        password = request.POST.get('password')
        img = request.FILES['image']
        obj = adminreg(USERNAME=user, EMAIL=em, MOBILE=mob, PASSWORD=password, IMAGE=img)
        obj.save()
        return redirect(admin)
def category(req):
    return render(req,"category.html")
def savecategorypage(request):
    if request.method == "POST":
        na = request.POST.get('name')
        dis = request.POST.get('discription')
        img = request.FILES['image']
        obj = categorydb(NAME=na, DISCRIPTION=dis, IMAGE=img)
        obj.save()
        return redirect(category)
def displaycategory(req):
    data = categorydb.objects.all()
    return render(req,"displaycategory.html",{'data':data})
def editcategory(req,dataid):
    data = categorydb.objects.get(id=dataid)
    print(data)
    return render(req,"editcategory.html",{'data':data})
def updatecategorypage(req,dataid):
    if req.method == "POST":
        na = req.POST.get('name')
        dis = req.POST.get('discription')
        try:
            img = req.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = categorydb.objects.get(id=dataid).IMAGE
        categorydb.objects.filter(id=dataid).update(NAME=na, DISCRIPTION=dis, IMAGE=file)
        return redirect(displaycategory)
def deletecategory(req,dataid):
    data = categorydb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaycategory)
def products(req):
    data = categorydb.objects.all()
    return render(req,"addproducts.html", {'data':data})
def saveproducts(request):
    if request.method == "POST":
        na = request.POST.get('name')
        pri = request.POST.get('price')
        qua = request.POST.get('quantity')
        dis = request.POST.get('discription')
        img = request.FILES['image']
        cat = request.POST.get('category')
        obj = productdb(NAME=na, PRIZE=pri, QUANTITY=qua, DISCRIPTION=dis, CATEGORY=cat, IMAGE=img)
        obj.save()
        return redirect(products)
def displayproduct(req):
    data = productdb.objects.all()
    return render(req, "displayproduct.html", {'data': data})
def editproduct(req,dataid):
    data = productdb.objects.get(id=dataid)
    da = categorydb.objects.all()
    print(data)
    print(da)
    return render(req,"editproduct.html", {'datas':data,'da':da})
def updateproduct(req,dataid):
    if req.method == "POST":
        na = req.POST.get('name')
        pri = req.POST.get('price')
        qua = req.POST.get('quantity')
        dis = req.POST.get('discription')
        cat = req.POST.get('category')
        try:
            img = req.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = productdb.objects.get(id=dataid).IMAGE
        productdb.objects.filter(id=dataid).update(NAME=na, PRIZE=pri, QUANTITY=qua, DISCRIPTION=dis, CATEGORY=cat, IMAGE=file)
        return redirect(displayproduct)
def deleteproduct(req,dataid):
    data = productdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displayproduct)
def loginpage(req):
    return render(req,"login.html")
def adminlogin(req):
    if req.method == "POST":
        username_r = req.POST.get('username')
        password_r = req.POST.get('password')

        if User.objects.filter(username__contains = username_r).exists():
            user = authenticate(username = username_r, password=password_r)
            if user is not None:
                login(req,user)
                req.session['username']=username_r
                req.session['password']=password_r
                return redirect(indexpage)
            else:
                return redirect(login)
        else:
            return redirect(login)
def adminlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(loginpage)

def displaycontact(req):
    data = contactdb.objects.all()
    return render(req, "displaycontact.html", {'data': data})

def displayorder(req):
    data=productde.objects.all()
    return render(req,"displaybooking.html",{'data':data})





