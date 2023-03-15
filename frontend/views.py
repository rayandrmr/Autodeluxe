from django.shortcuts import render,redirect
from backapp.models import categorydb, productdb, adminreg, checkoutdb, contactdb, productde
from frontend.models import userlogindb
from django.contrib import messages


# Create your views here.
def homepage(request):
    datas = productdb.objects.all()
    return render(request,"home.html",{'datas':datas})
# def single(request):
#     return render(request,"single.html")
def single(req,dataid):
    data = productdb.objects.filter(id=dataid)
    print(data)
    return render(req,"single.html",{'data':data})
def aboutf(request):
    return render(request,"about.html")
def cars(request):
    datas = productdb.objects.all()
    return render(request,"cars.html",{'datas':datas})

def contact(request):
    return render(request,"contact.html")
def checkout(request):
    data=productde.objects.all()
    return render(request,"checkout.html",{'data':data})
def loginpag(request):
    return render(request,"loginpage.html")
def saveuserlogin(request):
    if request.method == "POST":
        em = request.POST.get('email')
        us = request.POST.get('username')
        pas = request.POST.get('passsword')
        cpas = request.POST.get('cpass')
        obj = userlogindb(EMAIL=em, USERNAME=us, PASSWORD=pas,CONFIRMPASSWORD=cpas)
        obj.save()
        return redirect(loginpag)

def custemerlogin(request):
    if request.method=='POST':
        Username_r=request.POST.get("username")
        Password_r=request.POST.get("password")

        if userlogindb.objects.filter(USERNAME=Username_r,PASSWORD=Password_r).exists():
            request.session['username']=Username_r
            request.session['password']=Password_r
            return redirect(homepage)
        else:
            return render(request,'loginpage.html')

def userlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(loginpag)

def saveadcheckout(request):
    if request.method == "POST":
        name = request.POST.get('name')
        em = request.POST.get('email')
        phon = request.POST.get('phone')
        addr = request.POST.get('address')
        obj = checkoutdb(NAME=name, EMAIL=em, PHONE=phon, ADDRESS=addr)
        obj.save()
        messages.success(request,"booked")
        return redirect(homepage)
def savecontact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        em = request.POST.get('email')
        sub = request.POST.get('subject')
        mes = request.POST.get('message')
        obj = contactdb(NAME=name, EMAIL=em,SUBJECT=sub,MESSAGE=mes)
        obj.save()
        messages.success(request,"Message Saved")
        return redirect(homepage)
def saveproduct(request):
    if request.method == "POST":
        name = request.POST.get('name')
        em = request.POST.get('price')
        obj = productde(NAME=name,PRICE=em)
        obj.save()
        return redirect(checkout)
def deleteproduct(req,dataid):
    data = productde.objects.filter(id=dataid)
    data.delete()
    return redirect(checkout)


