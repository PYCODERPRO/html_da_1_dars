# Generated by Django 3.2.18 on 2023-04-18 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Yonalish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=25)),
                ('familiya', models.CharField(max_length=25)),
                ('yosh', models.IntegerField()),
                ('date', models.DateField()),
                ('kurs', models.IntegerField(choices=[(1, '1-kurs'), (2, '2-kurs'), (3, '3-kurs'), (4, '4-kurs')])),
                ('fan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ifiles.yonalish')),
            ],
        ),
    ]
