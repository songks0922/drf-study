from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.ListBookView.as_view())
]
