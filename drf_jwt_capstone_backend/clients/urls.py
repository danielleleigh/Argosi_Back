from django.urls import path
from clients import views

urlpatterns = [
    path('all/', views.get_clients),
    path('add/', views.add_client),
    # path('allappts/', views.get_appointments),
    # path('addappts/', views.add_appointments),

]
