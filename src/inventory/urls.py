from django.conf.urls import url, include

from .import views
from .import view

urlpatterns = [
    url(r'^all/$', views.articles),
    url(r'^get/(?P<inventory_id>\d+)/$', views.article),
    url(r'^language/(?P<lang>[a-z\-]+)/$',views.language),
    url(r'^create/$', views.create),
    url(r'^add_comment/(?P<inventory_id>\d+)/$', views.add_comment),
    url(r'^like/(?P<inventory_id>\d+)/$', views.like),


    url(r'^$', views.articles, name='index'),
    url(r'^item/(?P<id>\d+)/', views.item_detail, name='item_detail'),
    url(r'^hello/$', views.hello),
    url(r'^hello_simple/$', views.hello_simple),
    url(r'^hello_template/$', views.hello_template),
    url(r'^hello_class/$', views.HelloTemplate.as_view()),
    url(r'^auth/$', view.auth_view),
    url(r'^login/$', view.login_view),
    url(r'^logged_in/$', view.logged_in_view),
    url(r'^logout/$', view.logout_view),
    url(r'^invalid/$', view.invalid_view),
    url(r'^register/$', view.register_view, name='register'),
    url(r'^registered/$', view.registered_view),
    url(r'^edit_profile/$', view.edit_profile),
    ]