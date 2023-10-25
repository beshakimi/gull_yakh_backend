from django.urls import path
from accounts import views

urlpatterns = [
    
    
    path('login', views.login_page, name='login'),
    path('register', views.register, name='register'),
    path('profile', views.profile_view, name='profile'),
    
]