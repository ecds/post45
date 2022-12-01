from django.urls import path

from . import views


urlpatterns = [
    path('', views.about, name="about"),
    path('index', views.index, name="index"),
    path('about', views.about, name="about"),
    path('programerarecord', views.programerarecord, name="programerarecord"),
    path('programerapeople', views.programerapeople, name="programerapeoplepage"),
    path('programeragraduations', views.programeragraduations, name="programeragraduationspage"),
    path('masterprize', views.masterprize, name="masterprize"),
    path('nytfull', views.nytfull, name="nytfull"),
    path('nyttitle', views.nyttitle, name="nyttitle"),
    path('nythathi', views.nythathi, name="nythathi"),
    path('mlpwinnders', views.mlpwinners, name="mlpwinners"),
    path('mlphathi', views.mlphathi, name="mlphathi")
]
