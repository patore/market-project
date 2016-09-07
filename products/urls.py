from django.conf.urls import include, url
from django.contrib import admin
from products.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView

urlpatterns = [

    url(r'^$', ProductListView.as_view(),  name='list_view'),
    url(r'^add/$', ProductCreateView.as_view(),  name='create_view'),
    url(r'^(?P<pk>\d+)/edit/$', ProductUpdateView.as_view(),  name='update_view'),
    url(r'^(?P<slug>[\w-]+)/edit/$', ProductUpdateView.as_view(),  name='update_view'),
    url(r'^(?P<slug>[\w-]+)/$', ProductDetailView.as_view(),  name='detail_view'),

    url(r'^admin/', include(admin.site.urls)),
]
