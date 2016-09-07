from django.conf.urls import include, url
from django.contrib import admin
from .views import TagListView, TagDetailView

urlpatterns = [

    url(r'^$', TagListView.as_view(),  name='list_view'),
    url(r'^(?P<slug>[\w-]+)/$', TagDetailView.as_view(),  name='detail_view'),

]
