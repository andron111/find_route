from django.urls import path

from cities.views import *

urlpatterns = [
    path('', home, name='home'),
    path('detail/<int:pk>/', CityDetalView.as_view(), name='detail'),


]
