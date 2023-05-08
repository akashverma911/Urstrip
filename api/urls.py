from django.urls import path, include
from . import views

urlpatterns = [
    path('api/', views.LCMyModelAPI.as_view()),
    path('api/<int:pk>', views.RUDMyModelAPI.as_view()),
]
