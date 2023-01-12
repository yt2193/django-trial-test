from django.shortcuts import render,redirect
from .models import Company
from .forms import myForm,modelForm

# Create your views here.
def index(request):
    return render(request,"index.html")

def create(request):
    if request.method=='POST':
        Name=request.POST['name']
        Age=request.POST['age']
        Address=request.POST['address']
        obj=Company.objects.create(name=Name,age=Age,address=Address)
        obj.save()
        return redirect('/')

def retrieve(request):
    detail=Company.objects.all()
    return render(request,"index.html",{"details":detail})



def delete(request,id):
    Company.objects.filter(id=id).delete()
    return redirect("/")


def edit(request,id):
    obje=Company.objects.get(id=id)
    return render(request,"edit.html",{'object':obje})

def update(request,id):
     object=Company.objects.get(id=id)
     form=modelForm(request.POST,instance=object)
     form.save()
     return redirect("/")



def entryForm(request):
    return render(request,"form.html",{"forms":myForm()})

def dbForm(request):
    #f=modelForm(request.POST)
    return render(request,"modelform.html",{"forms":modelForm()})





    

