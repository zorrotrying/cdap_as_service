from django.conf.urls import url
import views

urlpatterns = [
    url(r'^stype=(?P<stype>[^/]+)&rtype=(?P<rtype>[^/]+)&catgname=(?P<catg_name>[^/]+)&appname=(?P<app_name>[^/]+)&sname=(?P<script_name>[^/]+)$', views.script_to_service, name='code-to-service'),
]