from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login_user', views.login_user, name='login_user'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('register_user', views.register_user, name='register_user'),
    path('user_profile/<int:pk>', views.user_profile, name='user_profile'),
    path('update_profile/<int:pk>', views.update_profile, name='update_profile'),
    path('update_password/', views.update_password, name='update_password'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='Profile/password_reset.html'), name='password_reset'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='Profile/password_reset_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='Profile/password_reset_form.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='Profile/password_reset_done.html'), name='password_reset_complete')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
