from django.urls import path
from WebSite import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('index/<slug:some_slug>/', views.show_persons, name='persons'),
]