from django.urls import path
from clients import views

urlpatterns = [
    path('all/', views.get_clients),
    path('addclient/', views.add_client),
    path('userclients/', views.get_clients),
]
