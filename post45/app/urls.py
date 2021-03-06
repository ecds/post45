from django.urls import path

from . import views


urlpatterns = [
    path('index', views.index, name="index"),
    path('about', views.about, name="about"),
    path('programerarecord', views.programerarecord, name="programerarecord"),
    path('programerapeople', views.programerapeople, name="programerapeoplepage"),
    path('programeragraduations', views.programeragraduations, name="programeragraduationspage"),
    path('masterprize', views.masterprize, name="masterprize")
]
