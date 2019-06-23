from django.conf.urls import url
from . import views

app_name = 'products'
urlpatterns = [
    url(r'^$', views.ProductList.as_view(), name='list'),
    url(r'^new/$', views.ProductCreate.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', views.ProductDetail.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update/$', views.ProductUpdate.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', views.ProductDelete.as_view(), name='delete'),
]
