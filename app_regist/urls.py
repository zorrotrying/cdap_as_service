from django.conf.urls import url
import views


urlpatterns = [
    url(r'script/stype=(?P<stype>[^/]+)&catgname=(?P<catg_name>[^/]+)&appname=(?P<app_name>[^/]+)&sname=(?P<script_name>[^/]+)$',
        views.script_identify, name='app-identify'),
]

