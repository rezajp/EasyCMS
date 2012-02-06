from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'EasyCMSProject.EasyCMS.views.home_page', name='home'),
     url(r'^(?P<page_key>\w{0,50})/$', 'EasyCMSProject.EasyCMS.views.show_page', name='page'),
     url(r'^siteadmin/pages$', 'EasyCMSProject.EasyCMS.siteadmin.pages.index', name='pagesadmin'),
    # url(r'^EasyCMSProject/', include('EasyCMSProject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
