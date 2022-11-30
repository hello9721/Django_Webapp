from django.db import models
from django.utils import timezone

# Create your models here.
class Me(models.Model):

    title = models.CharField(max_length=20)
    singer = models.CharField(max_length=20,default='')
    date = models.DateTimeField()
    url = models.TextField()
    
    def publish(self):

        self.date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

