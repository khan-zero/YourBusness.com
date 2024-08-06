from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dashboard_index'),
    path('contact', views.contactList, name='contactList'),
    path('contact/update/<int:id>/', views.updateStatus, name='updateStatus'),
]