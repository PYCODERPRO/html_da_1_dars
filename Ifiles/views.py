from django.shortcuts import render
from Ifiles.models import Student
# Create your views here.

def home(malumot):
    return render(malumot, 'index.html')

def ikkinchi_sahifa(malumot):
    talabalar = Student.objects.all()
    return render(malumot, 'foydalanuvchilar.html', {"students":talabalar})

def delete_talaba(malumot, id):
    talaba = Student.objects.get(id=id).delete()
    talabalar = Student.objects.all()
    return render(malumot,'foydalanuvchilar.html', {"students":talabalar})