"""cDAP_v2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^newapp/', include('app_regist.urls',namespace='app-register')),
    # url(r'^newservice/', include('service_core.urls', namespace='service-register')),
    url(r'^runservice/', include('app_run.urls', namespace='app-run')),
    url(r'^service/', include('service_core.urls', namespace='service')),
    url(r'^admin/', admin.site.urls),
]
