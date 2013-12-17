from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'ifiltr_site.views.index', name='home'),
    url(r'^inprogress/', 'ifiltr_site.views.under_construction', name='under_construction'),
    url(r'^privacy/', 'ifiltr_site.views.privacy', name='privacy'),
	url(r'^about/', 'ifiltr_site.views.about', name='about'),
	url(r'^forums/', 'ifiltr_site.views.forums', name='forums'),
	url(r'^blogs/', 'ifiltr_site.views.blogs', name='blogs'),
	url(r'^news/', 'ifiltr_site.views.news', name='news'),
	url(r'^advertising/', 'ifiltr_site.views.advertising', name='advertising'),
	url(r'^partners/', 'ifiltr_site.views.partners', name='partners'),
	url(r'^contact/', 'ifiltr_site.views.contact', name='contact'),
	url(r'^contacts_support/', 'ifiltr_site.views.contacts_support', name='contacts_support'),
	url(r'^contacts_advertising/', 'ifiltr_site.views.contacts_advertising', name='contacts_advertising'),
	url(r'^contacts_partnerships/', 'ifiltr_site.views.contacts_partnerships', name='contacts_partnerships'),
	url(r'^q/', 'ifiltr_site.views.search'),
    url(r'^category/', 'ifiltr_site.views.getCategories'),
    url(r'^discover/', 'ifiltr_site.views.discover'),
    # url(r'^ifiltr/', include('ifiltr.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
        (r'^janrain/', include('janrain.urls')),
)

urlpatterns += staticfiles_urlpatterns()
