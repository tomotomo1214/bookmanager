
from django.urls import path
from .views import new_book

urlpatterns = [
    path('new/',new_book,name="new_book")
]
