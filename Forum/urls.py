from django.urls import path
from Forum import views

app_name = 'Forum'
urlpatterns = [
    path('all_topics', views.all_topics, name='all_topics'),
    path('topic/<int:pk>', views.topic_details, name='topic_details'),
    path('add_topic', views.add_topic, name='add_topic'),
]