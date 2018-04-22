from django import forms
from .models import Student, Staff, Subject
from django.contrib.auth.models import User


class StudentForm(forms.ModelForm):
    
    class Meta:
        model = Student
        widgets={
            'roll_no' : forms.Textarea(attrs={'rows': 9, 'cols':42 }),
            }
        fields = ['roll_no','name','dob','department','clas','batch','email','mobie']
        
        
class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        widgets={
            'staff_id' : forms.Textarea(attrs={'rows':7,'cols':42}),
            }
        fields = ['staff_id','name','doj','department','email','mobie']
    

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        widgets={
            'sub_id' : forms.Textarea(attrs={'rows':3,'cols':10}),
            }
        fields = ['sub_id','sub_name']
    


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'password']
