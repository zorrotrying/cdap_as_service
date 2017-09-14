from django.conf.urls import url
import views


urlpatterns = [
    url(r'^$', views.script_run, name='app-run'),
]

