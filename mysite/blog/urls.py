from django.conf.urls import url

from blog.views import home, post_detail, edit_post

urlpatterns = [
    url(r'^$', home, name="home"),
    url(r'^(?P<pk>[0-9]+)/$', post_detail, name="post"),
    url(r'^(?P<pk>[0-9]+)/edit$', edit_post, name="edit_post"),
]
