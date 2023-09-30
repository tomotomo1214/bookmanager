from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=64)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    detail=models.TextField()

