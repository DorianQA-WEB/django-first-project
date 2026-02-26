from django.urls import path, re_path, include
from blog import views

product_patterns = [
    path('', views.products),
    path('new/', views.new),
    path('top/', views.top),
    path('comments/', views.comments),
    path('questions/', views.questions)
]

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, kwargs={'name': 'Vladimir', 'age': 29}),
    re_path(r'^contact/', views.contact),
    path('user/', views.user),
    re_path(r'^user/(?P<name>\D+)/', views.user),
    re_path(r'^user/', views.user),
    path('products/<int:id>/', include(product_patterns)),
    path('detail/', views.detail),
    path('access/<int:age>/', views.access),
]

