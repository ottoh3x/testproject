from django.shortcuts import render , redirect , get_object_or_404
from .forms import StudentForm 
from .models import Student

# Create your views here.



def home(request):
    return render(request , 'base.html')


def students(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect ('/')


    context = {
        'form' : form
    }
    return render(request , 'students.html' , context)

def studentslist(request):
    total = Student.objects.all().count
    obj = Student.objects.all()

    context = {
        'obj':obj, 'total':total
    }
    return render(request , 'studentslist.html' , context)

def updatestudent(request , pk):
    order = Student.objects.get(id = pk)
    form = StudentForm(instance=order)
    if request.method == "POST":
        form = StudentForm(request.POST , instance=order)
        if form.is_valid():
            form.save()
            return redirect ('list')

    context = {
        'form' : form
    }         
    return render (request , 'updatestudent.html' , context)

def deletestudent(request , pk):



    obj = Student.objects.get(id = pk)
    obj.delete()
    return redirect ('list')

    context = {
        'obj' : obj
    }  
    return render (request , 'deletestudent.html' , context)

def studentview(request , id):

    obj = get_object_or_404(Student , id = id)

    context = {
        'obj' : obj
    }
    return render (request,'studentview.html' , context)



def searchbar(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        post = Student.objects.all().filter(id = search)

    context={'post' : post}
    return render (request , 'searchbar.html' , context)    