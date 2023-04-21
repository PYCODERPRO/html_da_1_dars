from django.contrib import admin
from Ifiles.models import Yonalish,Student

# Register your models here.

class AdminYonalish(admin.ModelAdmin):
    list_display = ["id","nomi"]

admin.site.register(Yonalish,AdminYonalish)

class AdminStudent(admin.ModelAdmin):
    list_display = ["id","ism","familiya","yosh","fan","date","kurs"]

admin.site.register(Student,AdminStudent)