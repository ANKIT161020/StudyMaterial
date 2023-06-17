from django.db import models

# Create your models here.
class experiments(models.Model):
    exp_name = models.CharField(max_length=100)
    subject_name = models.CharField(max_length=100)
    sem_num = models.IntegerField()
    exp_file = models.FileField(upload_to='media/exptfiles',max_length=250)

class Contactus(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    msg = models.TextField(max_length=300)