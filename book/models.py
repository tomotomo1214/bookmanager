from django.db import models

# Create your models here.
class Bookshelf(models.Model):
    name=models.CharField(max_length=64)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.name

class Book(models.Model):
    title=models.CharField(max_length=64)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    detail=models.TextField()
    bookshelf=models.ForeignKey(Bookshelf,on_delete=models.SET_NULL,null=True)
    def __str__(self) -> str:
        return self.title

