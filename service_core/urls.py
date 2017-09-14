from django.conf.urls import url
import views


urlpatterns = [
    url(r'new/spath=(?P<spath>[^/]+)&stype=(?P<stype>[^/]+)&rtype=(?P<rtype>[^/]+)$', views.script_to_service, name='code-to-service'),
    url(r'^run/(?P<stype>[^/]+)/(?P<catgname>[^/]+)/(?P<appname>[^/]+)/(?P<kwargs>[^/]*)$', views.service_run, name='service-run'),
    url(r'^test$', views.rob_test),
]