from django.shortcuts import render,HttpResponse
from .models import departments,doctor
from .forms import bookingform

# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
     return render(request,'about.html')
def docter(request):
     dict_doc = {'doct':doctor.objects.all()}
     return render(request,'docters.html',dict_doc)
def contact(request):
     return render(request,'contact.html')
def booking(request):
     if request.method == "POST":
          form = bookingform(request.POST)
          if form.is_valid():
               form.save()

     form = bookingform()
     dict_form = {'form':form}
     return render(request,'booking.html',dict_form)
def department(request):
     dict_dept = {'dept':departments.objects.all()}
     return render(request,"department.html",dict_dept)
