from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('practice/', views.practice, name='practice'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact_view, name='contact'),
    path('success/', views.success_view, name='success'),
]
