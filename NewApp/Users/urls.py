from django.urls import path
from Users import views


urlpatterns = [
    path('register/', views.register_users, name='register'),
    path('login/', views.login_users, name='login'),
    path('logout/', views.logout_users, name='logout')
]