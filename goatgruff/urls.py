from django.conf.urls import patterns, include, url
from django.contrib import admin
from jsonrpc import jsonrpc_site
import goatrpc.views # you must import the views that need connected


admin.autodiscover()

urlpatterns = patterns('',
  url(r'^$', include('goat.urls')),
  url(r'^admin/', include(admin.site.urls)),
  url(r'^json/', jsonrpc_site.dispatch, name="jsonrpc_mountpoint")
)
