from django.contrib import admin
from django.urls import path
from basic import views

urlpatterns = [
    path('myadmin/', admin.site.urls),
    path('home/', views.index),
    path('', views.index),
    path('Views/', views.Views, name='myapp-views'),  # Add a name to the URL pattern
]
