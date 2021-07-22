from django.db import models

# Create your models here.
class PropertyImage(models.Model):
    username = models.CharField(max_length=255)
    images = models.ImageField(upload_to='images', null=True, blank=True)

    def __str__(self):
        return str(self.images)
