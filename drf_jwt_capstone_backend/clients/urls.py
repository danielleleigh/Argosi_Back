from django.urls import path
from clients import views

urlpatterns = [
    path('all/', views.get_clients),
    path('add/', views.add_client),
    path('appointments/', views.get_appointments),
    path('appointment/add', views.add_appointments),

]
