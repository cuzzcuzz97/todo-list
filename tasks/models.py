from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class TaskList(models.Model):
    user = models.ForeignKey(User, null= True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100,blank=False)
    detail = models.TextField(max_length=100,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-created_at']