from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^others/(?P<path>.*)$', "django.views.static.serve",
{'document_root': settings.STATIC_URL}),
    url(r'^anotated/(.*)$', "cms_templates.views.showtemplate"),
    url(r'^$', "cms_templates.views.all"),
    url(r'^cars/(.*)$', "cms_templates.views.show"),
    url(r'^(.*)$', "cms_templates.views.notfound")
)
