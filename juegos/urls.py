from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from megagames import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('create-post/', views.create_post_view, name='create_post'),
    path('', views.post_list_view, name='index'),
    path('post/<int:post_id>/', views.post_detail_view, name='post_detail'),
]