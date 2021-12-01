
from django.db import models
from django.core.exceptions import ValidationError
import os
# Create your models here.
from django.core.validators import FileExtensionValidator
from django.utils import timezone
from uuid import uuid4


def validate_image(picture):
    file_size = picture.size

    if file_size > 2000000:
        raise ValidationError("Please Upload file <= 2mb")
    

def validate_file_extension(picture):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(picture.name)[1]  # [0] returns path+filename
    valid_extensions = ['.jpg', '.png', '.jpeg']

    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')


def path_and_rename(instance, filename):
    upload_to = 'Profile'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)


class Profile(models.Model):

    name = models.CharField(max_length=50)
    picture = models.ImageField(
        upload_to=path_and_rename, blank=True, validators=[validate_image, validate_file_extension])

    

























# FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg']),

    # def delete(self, *args, **kwargs):

    #     self.picture.delete()
    #     super().delete(*args, **kwargs)
        
    