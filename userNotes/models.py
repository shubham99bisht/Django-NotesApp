from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Notes(models.Model):
    # Fields
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=30, help_text='Note title')
    note = models.TextField(max_length=20, help_text='Note text')
    color = models.CharField(max_length=10, help_text='Color Hex Code')

    # Metadata
    class Meta:
        ordering = ['timestamp']

    # Methods
    def save(self, *args, **kwargs):
        if not self.id:
            self.timestamp = timezone.now()
        return super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('home', args=[str(self.id)])

    def __str__(self):
        return self.note
    