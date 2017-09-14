from django.conf.urls import url
import views


urlpatterns = [
    url(r'^(?P<stype>[^/]+)/(?P<catgname>[^/]+)/(?P<appname>[^/]+)/(?P<kwargs>[^/]*)$', views.service_run, name='service-run'),
]