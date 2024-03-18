from django.urls import path
from Collectors_Zone import views

app_name = 'Collectors_Zone'
urlpatterns = [
    path('', views.home, name='home'),
]
