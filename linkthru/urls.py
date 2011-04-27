from django.conf.urls.defaults import *

from linkthru.views import linkthru_view, linkthru_detail

urlpatterns = patterns('',
    url(r'^view/(?P<id>[\d]+)/$', linkthru_view, name='lt-linkthru-view'),
    url(r'^linkthrus/(?P<id>[\d]+)/$', linkthru_detail, name='lt-linkthru-detail'),
    #url(r'^addisplay.html', ad_display, name='adzone_ad_display'),
    #url(r'^linkthrus/$', linkthru_index, name='lt-index'),
    #url(r'^xhr_ads/(?P<format>\w+)$', xhr_ad_table, name='adzone_xhr_ad_table'),
)
