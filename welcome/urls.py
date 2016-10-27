from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.front,name='front'),
	url(r'^storyRedirect/$',views.storyRedirect,name='storyRedirect'),
]