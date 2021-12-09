from django.db import models

# Create your models here.

from django.db import models

# Create your models here.


class SendEmail(models.Model):
    sendTo = models.EmailField(max_length=50)
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=100)
    file = models.FileField(upload_to="Media", null=True)

    class Meta:
        db_table = 'SendEmail'
    
    def __str__(self):
        return self.sendTo
