from django.db import models

class Student(models.Model):
    
    roll_no = models.IntegerField(default=0)
    name = models.CharField(max_length=50)
    dob=models.DateField()
    department=models.CharField(max_length=50)
    clas=models.CharField(max_length=20)
    batch=models.IntegerField(default=0)
    email=models.CharField(max_length=50)
    mobie=models.CharField(max_length=10)

    def __str__(self):
        return self.roll_no
    
class Staff(models.Model):
    
    staff_id = models.IntegerField(default=0)
    name = models.CharField(max_length=50)
    doj = models.DateField()
    department=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    mobie=models.CharField(max_length=10)

    def __str__(self):
        return self.staff_id
    
class Subject(models.Model):
    
    sub_id = models.IntegerField(default=0)
    sub_name = models.CharField(max_length=50)

    def __str__(self):
        return self.sub_id
