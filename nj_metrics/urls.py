"""nj_metrics URL Configuration

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
from django.conf.urls import include, url
from django.contrib import admin
from metrics import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^CSV/Counties/$', views.counties_csv, name='counties_csv'),
    url(r'^CSV/Parties/$', views.party_csv, name='party_csv'),
    url(r'^CSV/votes_year_csv_county/$', views.votes_year_csv, name = 'votes_year_csv'),
    url(r'^CSV/votes_year_csv_county/(?P<countyId>\d+)/$', views.votes_year_csv_county, name = 'votes_year_csv_county'),
    url(r'^CSV/votes_party_csv/', views.votes_party_csv, name = 'votes_party_csv'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
