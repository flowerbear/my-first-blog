from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list),
<<<<<<< HEAD
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
=======
>>>>>>> 550d02350d5da4128831dfedd334ab4b3df9e70f
]
