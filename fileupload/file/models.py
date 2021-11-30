from django.db import models

# Create your models here.

class Profile(models.Model):
    def nameFile(instance, filename):
        return '/'.join(['images', str(instance.name), filename])
    name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to=nameFile, blank = True)
    files = models.FileField(upload_to=nameFile, blank= True)
    