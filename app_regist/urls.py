from django.conf.urls import url
import views


urlpatterns = [
    url(r'script/type=(?P<type>[^/]+)&spath=(?P<spath>[^/]+)$', views.script_identify, name='app-identify'),
]

