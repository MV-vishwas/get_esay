from django.shortcuts import render,redirect
from django.http import HttpResponse
from home.models import *
def index(request):
    l1 = Service.objects.all()
    data = {'l1': l1, }
    return render(request, 'home.html', data)

def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pd=request.POST.get('password')
        x = Member.objects.all()
        res = {'value': 'Invalid Username or Password',}
        for item in x:
            if item.mail ==username:
                    if item.password==pd:
                        request.session['msg']=item.F_name.capitalize()+" "+item.L_name.capitalize()
                        request.session.set_expiry(0)
                        l1 = Service.objects.all()
                        data = {'l1': l1, }
                        return render(request,'home.html',data)
                        break
                    else:
                        return render(request,'login.html',res)
                        break
        else:
            return render(request,'login.html',res)
    else:
        return render(request,'login.html')

def registration(request):
    return render(request,'registration.html')

def worker(request):
    return render(request,'worker.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def add_member(request):
    email= request.POST.get('mail')
    x=Member.objects.all()
    for item in x:
        if item.mail==email:
            return render(request,'registration.html',{"error_msg":'Mail ID is Already registered.',})
            break
    fname=request.POST.get('fname')
    lname=request.POST.get('lname')
    gender=request.POST.get('gender')
    city=request.POST.get('city')
    password=request.POST.get('password')
    country=request.POST.get('country')
    m=Member(F_name=fname,L_name=lname,mail=email,gender=gender,city=city,password=password,country=country)
    m.save()
    return render(request,'login.html')

def logout(request):
    request.session.flush()
    l1 = Service.objects.all()
    data = {'l1': l1, }
    return render(request,'home.html',data)

def test(request):
    l1=Service.objects.all()
    data={'l1':l1,}
    return render(request,'test.html',data)


from django.http import Http404
def service_provider(request, service_id):
    try:
        service_name = Service.objects.get(pk=service_id)
    except Service.DoesNotExist:
        raise Http404("This service is no more available.\nSorry.....")
    return render(request,'service_provider.html',{'service_name':service_name})

