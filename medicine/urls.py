from django.urls import path
from . import views

urlpatterns=[
    path ('medihome/', views.medicine_home, name = 'medicine_home'),
    path ('addmedi/', views.add_medicine, name = 'add_medicine'),

]