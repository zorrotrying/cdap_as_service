from django.conf.urls import url
import views

urlpatterns = [
    url(r'^spath=(?P<spath>[^/]+)&stype=(?P<stype>[^/]+)&rtype=(?P<rtype>[^/]+)$', views.script_to_service, name='code-to-service'),
]