from django.urls import path
from Posty import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'Posty'
urlpatterns = [
    path('post/<int:pk>', views.post_details, name='post_details'),
    path('all_posts', views.all_posts, name='all_posts'),
    path('add_post', views.add_post, name='add_post'),
    path('update_post/<int:pk>', views.update_post, name='update_post'),
    path('delete_post/<int:pk>', views.delete_post, name='delete_post'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)