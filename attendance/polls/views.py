from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.db.models import Q
from django.http import HttpResponse
from . models import Student, Staff, Subject
from . forms import StudentForm, StaffForm, SubjectForm, UserForm
from django.http.response import HttpResponseRedirect, HttpResponseServerError
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.query import QuerySet
from . import views
# Create your views here.
def polls(request):
        if request.user.is_authenticated:
            
            form = UserForm(request.POST or None)
            return render(request, 'polls/base.html', {'form' : form})
        
        else:
            
            form = StudentForm(request.POST or None, request.FILES or None)
            form = StaffForm(request.POST or None, request.FILES or None)
            form = SubjectForm(request.POST or None, request.FILES or None)
    
        if form.is_valid():
            
            stud = form.save()
            stafs = form.save()
            sub = form.save()
            
            return render(request,'polls/create_student.html', {'stud' : stud })
            return render(request,'polls/create_staff.html', {'stafs' : stafs })
            return render(request,'polls/create_subject.html', {'sub' : sub })
            
        
        context = {
            'form' : form
            }
        return render(request, 'polls/base.html', context)



def create_student(request, students_id,roll_no):
    form = StudentForm(request.POST or None, request.FILES or None)
    stud = get_object_or_404(Student, pk=students_id)
        
    if form.is_valid():
        #clean data
        for data in stud.student_set.all():
            if data.roll_no == form.cleaned_data.get("roll_no"):
                context= {
                    'stud' : stud,
                    'form' : form,
                    'error_message' : "Student already exists!!!"
                    }
                return render(request,'polls/create_student.html', context)
            student = form.save(commit=False)
            student.students = stud   
        
            student.save()
        print("stud:", stud)
        return render(request, 'polls/detail.html', { 'stud' : stud })
    
    context = {
        'stud' : stud,
        'form' : form
        }
    return render(request,'polls/create_student.html', context)


def create_staff(request, id):
    form = StaffForm(request.POST or None, request.FILES or None)
    stafs = get_object_or_404(Staff, pk=id)
        
    if form.is_valid():
        #clean data
        for data in stafs.staff_set.all():
            if data.staff_id == form.cleaned_data.get("id"):
                context= {
                    'stafs' : stafs,
                    'form' : form,
                    'error_message' : "Staff already exists!!!"
                }
        return render(request,'polls/create_staff.html', context)
        staff = form.save(commit=False)
        staff.staff = stafs   
        
        staff.save()
        #return HttpResponse("<h1> Staff Added</h1>")
        print("stafs:", stafs)
        return render(request, 'polls/create_staff.html', { 'stafs' : stafs })
    
    context = {
        'stafs' : stafs,
        'form' : form
        }
    return render(request,'polls/create_staff.html', context)

def create_subject(request, id):
    form = SubjectForm(request.POST or None, request.FILES or None)
    sub = get_object_or_404(Subject, pk=id)
        
    if form.is_valid():
        #clean data
        for data in sub.subject_set.all():
            if data.sub_id == form.cleaned_data.get("id"):
                context= {
                    'sub' : sub,
                    'form' : form,
                    'error_message' : "Subject already exists!!!"
                }
        return render(request,'polls/create_subject.html', context)
        subject = form.save(commit=False)
        subject.subject = sub   
        
        subject.save()
        #return HttpResponse("<h1> Subject Added</h1>")
        print("sub:", sub)
        return render(request, 'polls/create_subject.html', { 'sub' : sub })
    
    context = {
        'sub' : sub,
        'form' : form
        }
    return render(request,'polls/create_subject.html', context)
def detail(request, id):
    try:
        stud = Student.objects.get(pk=id)
    except Student.DoesNotExist:
        raise Http404("Could not find Software tutorial!!!")
    
    return render(request, 'polls/detail.html', {'stud': stud})


def view_students(request):
    
    stud = Student.objects.all()
    
    return render(request,'polls/view_student.html', {'stud' : stud})
def view_staffs(request):
    
    stafs = Staffs.objects.all()
    
    return render(request,'polls/view_staffs.html', {'stafs' : stafs})
def view_subject(request):
    
    sub = Subject.objects.all()
    return render(request,'polls/view_subject.html', {'sub' : sub})









