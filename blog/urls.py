from django.urls import path, re_path
from blog import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, kwargs={'name': 'Vladimir', 'age': 29}),
    re_path(r'^contact/', views.contact),
    re_path(r'^user/(?P<name>\D+)/(?P<age>\d+)/', views.user),
    re_path(r'^user/(?P<name>\D+)/', views.user),
    re_path(r'^user/', views.user)
]

