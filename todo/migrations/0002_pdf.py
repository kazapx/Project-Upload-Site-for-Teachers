# Generated by Django 4.0 on 2021-12-12 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pdf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentname', models.CharField(max_length=50, verbose_name='Öğrenci Adı')),
                ('studentsurname', models.CharField(max_length=50, verbose_name='Öğrenci Soyadı')),
                ('studentno', models.IntegerField(verbose_name='Öğrenci Numarası')),
                ('studenttype', models.IntegerField(verbose_name='Öğretim Türü')),
                ('projecttype', models.CharField(max_length=50, verbose_name='Ders Adı')),
                ('projectsummary', models.TextField(verbose_name='Proje Özeti')),
                ('projectdate', models.CharField(max_length=50, verbose_name='Teslim Edildiği Dönem')),
                ('projecttitle', models.CharField(max_length=100, verbose_name='Proje Başlığı')),
                ('keywords', models.TextField(max_length=200, verbose_name='Anahtar Kelimeler')),
                ('counselorname', models.CharField(max_length=50, verbose_name='Danışman Adı')),
                ('counselorsurname', models.CharField(max_length=50, verbose_name='Danışman Soyadı')),
                ('counselordegree', models.CharField(max_length=50, verbose_name='Danışman Ünvan')),
                ('juryname', models.CharField(max_length=50, verbose_name='Jüri Adı')),
                ('jurysurname', models.CharField(max_length=50, verbose_name='Jüri Soyadı')),
                ('jurydegree', models.CharField(max_length=50, verbose_name='Jüri Ünvan')),
                ('pdfself', models.FileField(upload_to='', verbose_name='Pdf Dosyası')),
            ],
        ),
    ]
