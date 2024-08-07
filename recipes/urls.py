from django.urls import path
from .views import home, about, contats

urlpatterns = [
    path('', home), # home
]
