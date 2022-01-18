from django.urls import path
from clients import views

urlpatterns = [
    path('all/', views.get_clients),
    path('add/', views.add_client),
    path('edit/<int:pk>/', views.edit_client),
    path('delete/<int:pk>/', views.delete_client),
    path('appointments/', views.get_appointments),
    path('appointment/add', views.add_appointments),
    path('appointment/delete/<int:pk>/', views.delete_appointment),
    path('appointment/edit/<int:pk>/', views.edit_appointment),
]
