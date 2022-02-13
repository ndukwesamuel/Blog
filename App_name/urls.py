from django.urls import path
from .views import home, details, DeleteView


urlpatterns = [
    path('', home , name='home'),

    path('<str:pk>/', details , name='details'),
    path('delete/<str:pk>/', DeleteView , name='DeleteView'),



]
