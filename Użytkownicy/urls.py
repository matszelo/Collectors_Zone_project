from django.urls import path
from . import views

app_name = 'Użytkownicy'
urlpatterns = [
    path('login_user', views.login_user, name='login_user'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('register_user', views.register_user, name='register_user'),
    path('user_profile/<int:pk>', views.user_profile, name='user_profile'),
    path('update_profile/<int:pk>', views.update_profile, name='update_profile'),
]
