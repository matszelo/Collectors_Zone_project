from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'Użytkownicy'
urlpatterns = [
    path('login_user', views.login_user, name='login_user'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('register_user', views.register_user, name='register_user'),
    path('user_profile/<int:pk>', views.user_profile, name='user_profile'),
    path('update_profile/<int:pk>', views.update_profile, name='update_profile'),
    path('password_change', views.password_change, name='password_change')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
