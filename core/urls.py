from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('schools/', views.schools, name='schools'),
    path('pricing/', views.pricing, name='pricing'),
    path('library/', views.library, name='library'),
    path('story/', views.story, name='story'),
]
