
from django.urls import path

from productos import views
from . import views

urlpatterns = [
    path("<pk>", views.ProductoDetailView.as_view(), name="detalle-producto"),
    
]
