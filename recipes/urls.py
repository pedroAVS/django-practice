from django.urls import path

from recipes.views import home, temp

urlpatterns = [
    path('', home),  # home
    path('temp/', temp),
]
