from . import views
from django.urls import path

urlpatterns = [
    path('', views.image_list, name='image_list'),
    path('post/', views.post_image, name='post_image'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('Speeches/post/', views.post_speech, name='post_speech'),
]