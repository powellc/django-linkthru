# -*- coding: utf-8 -*-

# © Copyright 2009 Andre Engelbrecht. All Rights Reserved.
# This script is licensed under the BSD Open Source Licence
# Please see the text file LICENCE for more information
# If this script is distributed, it must be accompanied by the Licence

from django.contrib import admin
from linkthru.models import LinkThruZone, ImageLinkThru, LinkClick, LinkImpression

class LinkThruZoneAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'description']


class ImageLinkThruAdmin(admin.ModelAdmin):
    fieldsets = [ (None,         {'fields': [('title', 'url'), ('enabled', 'begins_on'), 'zone', 'content']}), ]
    list_display = ['title', 'url', 'updated', 'enabled']
    list_filter = ['updated', 'enabled',]
    search_fields = ['title', 'url']

class LinkClickAdmin(admin.ModelAdmin):
    search_fields = ['link', 'source_ip']
    list_display = ['link', 'click_date', 'source_ip']
    list_filter = ['click_date']
    date_hierarchy = 'click_date'

class LinkImpressionAdmin(admin.ModelAdmin):
    search_fields = ['link', 'source_ip']
    list_display = ['link', 'impression_date', 'source_ip']
    list_filter = ['impression_date']
    date_hierarchy = 'impression_date'

admin.site.register(LinkThruZone, LinkThruZoneAdmin)
admin.site.register(ImageLinkThru, ImageLinkThruAdmin)
admin.site.register(LinkClick, LinkClickAdmin)
admin.site.register(LinkImpression, LinkImpressionAdmin)
