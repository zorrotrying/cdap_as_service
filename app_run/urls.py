from django.conf.urls import url
import views


urlpatterns = [
    url(r'^script$', views.script_run, name='app-run'),
]

