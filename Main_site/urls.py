from django.urls import path
from Main_site import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'Main_site'
urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
