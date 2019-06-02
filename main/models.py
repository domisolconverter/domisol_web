from django.db import models

# Create your models here.
class UploadFileModel(models.Model):

    title = models.TextField(default='')
    email = models.TextField(default='')
    melody = models.TextField(default='')
    file = models.FileField(null=True)
