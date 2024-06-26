from django.urls import path
from Dropy import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'Dropy'
urlpatterns = [
    path('drop/<int:pk>', views.drop_details, name='drop_details'),
    path('all_drops', views.all_drops, name='all_drops'),
    path('add_drop', views.add_drop, name='add_drop'),
    path('update_drop/<int:pk>', views.update_drop, name='update_drop'),
    path('delete_drop/<int:pk>', views.delete_drop, name='delete_drop'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
