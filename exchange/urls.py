from django.urls import path
from .views import exchange_page

urlpatterns = [
    path('', exchange_page),
]