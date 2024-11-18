from django.urls import path
from . import views

urlpatterns=[
    path ('medihome/', views.medicine_home, name = 'medicine_home'),
    path ('addmedi/', views.add_medicine, name = 'add_medicine'),
    path('add/', views.add_medicine, name='add-medicine'),
    path('edit_medicine/<int:id>/', views.edit_medicine, name='edit_medicine'),
    path('delete/<int:id>/', views.delete_medicine, name='delete_medicine'),
    path('delete_medicine/<int:id>/', views.delete_medicine, name='delete_medicine'),
    path('medicine-home/', views.medicine_home, name='medicine-home'),
]
    


