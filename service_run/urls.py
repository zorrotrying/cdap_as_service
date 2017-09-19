from django.conf.urls import url
import views


urlpatterns = [
    url(r'^(?P<stype>[^/]+)/(?P<catg_name>[^/]+)/(?P<app_name>[^/]+)/(?P<kwargs>[^/]*)$', views.service_run, name='service-run'),
]