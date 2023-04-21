from django.db import models

# Create your models here.

class Yonalish(models.Model):
    nomi = models.CharField(max_length=55)


    def __str__(self):
        return self.nomi


class Student(models.Model):

    kurslar = ((1,"1-kurs"),
               (2,"2-kurs"),
               (3,"3-kurs"),
               (4,"4-kurs"),
               )
    ism = models.CharField(max_length=25)
    familiya = models.CharField(max_length=25)
    yosh = models.IntegerField()
    fan = models.ForeignKey(Yonalish, on_delete=models.CASCADE)
    date = models.DateField()
    kurs = models.IntegerField(choices=kurslar)
