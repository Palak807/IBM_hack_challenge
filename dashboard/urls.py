
from django.urls import path
from . import views

urlpatterns = [
    path('', views.LOGIN, name='LOGIN'),
    path('base.html', views.BASE),
    path('report.html', views.REPORT),
    path('story.html', views.STORY),
    path('vision.html', views.VISION),
    path('team.html', views.TEAM),
    path('login.html', views.LOGIN)
]
