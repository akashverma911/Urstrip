from django.db import models

# Create your models here.


def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)
  
class MyModel(models.Model):
  image_url = models.FileField(upload_to=upload_to, blank=True, null=True)
