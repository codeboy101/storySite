from django.conf.urls import url , include
from django.contrib import admin

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^',include("welcome.urls")),
	url(r'^story/',include("story.urls")),	

]
