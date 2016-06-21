from django.conf.urls import url

from . import views
app_name = 'staff'
urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^hello', views.hello, name='hello'),
	url(r'^(?P<a>[0-9]+)/(?P<b>[a-z]+)/$', views.detail, name='detail'),
	
]