from django.db import models
from datetime import datetime    

# Create your models here.
class city(models.Model):
    name = models.CharField(max_length = 200)
    datetime = models.DateTimeField(default=datetime.now())
    

    
    def __str__ (self):
        return self.name


    class Meta:
        verbose_name_plural = 'cities'
