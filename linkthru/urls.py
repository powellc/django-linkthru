from django.conf.urls.defaults import *

from linkthru.views import linkthru_view

urlpatterns = patterns('',
    url(r'^view/(?P<id>[\d]+)/$', linkthru_view, name='lt-linkthru-view'),
    #url(r'^addisplay.html', ad_display, name='adzone_ad_display'),
    #url(r'^ads/$', ad_index, name='adzone_ad_index'),
    #url(r'^ads/<?P<id>[\d]+)/$', ad_detail, name='adzone_ad_detail'),
    #url(r'^xhr_ads/(?P<format>\w+)$', xhr_ad_table, name='adzone_xhr_ad_table'),
)
