from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from .views import DestinationPDFView


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pdfmaker.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r"^destination.pdf$", DestinationPDFView.as_view())
)
