from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
import rest_framework
from django.contrib import admin
admin.autodiscover()
from todo.views import TodoDetailView, TodoView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'skeleton.views.home', name='home'),
    # url(r'^skeleton/', include('skeleton.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name="todo.html")),
    url(r'^todos/$', TodoView.as_view(), name='todo-view'),
    url(r'^todos/(?P<pk>\d+)$', TodoDetailView.as_view(), name='todo-view'),
)
