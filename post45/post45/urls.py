"""post45 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from app import views

router = routers.DefaultRouter()
router.register(r'records', views.RecordViewSet)
router.register(r'programerarecords', views.ProgramEraRecordViewSet)
router.register(r'programerapeople', views.ProgramEraPeopleViewSet)
router.register(r'programeragraduations', views.ProgramEraPeopleViewSet)
router.register(r'masterprizedata', views.MasterPrizeRecordViewSet)

urlpatterns = [
    url(r'^', include('app.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^records/$', views.RecordViewSet.as_view({'get': 'list'}), name='records'),
    url(r'^programerarecords/$', views.ProgramEraRecordViewSet.as_view({'get': 'list'}), name='programerarecords'),
    url(r'^programerapeople/$', views.ProgramEraPeopleViewSet.as_view({'get': 'list'}), name='programerapeople'),
    url(r'^programeragraduations/$', views.ProgramEraGraduationsViewSet.as_view({'get': 'list'}), name='programeragraduations'),
    url(r'^masterprizedata/$', views.MasterPrizeRecordViewSet.as_view({'get': 'list'}), name='masterprizedata'),
    path(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^download/', views.RecordExportCsvView.as_view(), name="download"),
    url(r'^programerarecordsdownload/', views.ProgramEraRecordExportCsvView.as_view(), name="programerarecordsdownload"),
    url(r'^programerapeopledownload/', views.ProgramEraPeopleExportCsvView.as_view(), name="programerapeopledownload"),
    url(r'^programeragraduationsdownload/', views.ProgramEraGraduationsExportCsvView.as_view(), name="programeragraduationsdownload"),
    url(r'^masterprizedownload/', views.MasterPrizeRecordExportCsvView.as_view(), name="masterprizedownload"),
    # url(r'^htrc/<docid>/', views.htrc_download, name='htrc_download'),

]
