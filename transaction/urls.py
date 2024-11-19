# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('addtransaction/', views.add_transaction, name='add_transaction'),
    path('success/', views.transaction_success, name='transaction_success'),
    path('view-transactions/', views.view_transactions, name='view_transactions'),
    
]
