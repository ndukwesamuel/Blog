from django.urls import path
from .views import home, details, DeleteView, CreateView, UpdateView


urlpatterns = [
    path('', home , name='home'),
    path('create/', CreateView , name='CreateView'),

    path('<str:pk>/', details , name='details'),
    path('delete/<str:pk>/', DeleteView , name='DeleteView'),
    path('update/<str:pk>/', UpdateView , name='UpdateView'),




]
