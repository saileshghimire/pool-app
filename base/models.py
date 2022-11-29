from django.db import models
from django.utils import timezone
# Create your models here.
class Party(models.Model):
    title = models.CharField(max_length=100)
    count = models.IntegerField(blank=True)
    date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title