"""project241 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView



urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    #user auth urls
    url(r'^accounts/login/$', 'filepanda.views.login' ),
    url(r'^accounts/auth/$', 'filepanda.views.auth_view' ),
    url(r'^accounts/logout/$', 'filepanda.views.logout' ),
    #url(r'^accounts/loggedin/$', 'fileupload.models.abc' ),
    url(r'^accounts/loggedin/$', 'fileupload.views.loggedin'),
    
    url(r'^accounts/invalid/$', 'filepanda.views.invalid_login' ),

    url(r'^$', RedirectView.as_view(url='/accounts/loggedin/', permanent=True)),

    url(r'^accounts/delete/(?P<document_id>\d+)/$', 'fileupload.views.delete_article'),

    url(r'^su/(?P<document_id>\d+)/$', 'fileupload.views.download_file'),

    #Registration urls
    url(r'^accounts/register/$', 'filepanda.views.register_user'),
    url(r'^accounts/register_success/$', 'filepanda.views.register_success'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
