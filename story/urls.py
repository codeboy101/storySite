from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.redirector,name='redirector'),
	url(r'^home/$',views.frontPage,name='frontPage'),
	url(r'^postStory/$',views.postStory,name='postStory'),
	url(r'^readStory/(?P<pk>\d+)/$',views.readStory,name='readStory'),
	url(r'^changeRating/(?P<pk>\d+)(?P<value>-{0,1}\d+)/$',views.changeRating,name='changeRating'),
	url(r'^register/$',views.register,name='register'),
	url(r'^login/$',views.login,name='login'),
	url(r'^logout/$',views.logout,name='logout'),
	url(r'^delete/(?P<pk>\d+)/$',views.deleteStory,name='deleteStory'),
]
