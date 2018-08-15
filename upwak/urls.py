from django.conf.urls import url, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # django
    url(r'^$', views.login, name='login'),
    url(r'^$', views.login, name='login'),
    ]