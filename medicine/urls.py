from django.urls import path
from . import views

urlpatterns=[
    path ('addmedi/', views.add_medicine, name = 'add_medicine'),
]