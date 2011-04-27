# -*- coding: utf-8 -*-

# © Copyright 2011 Colin Powell. All Rights Reserved.
# This script is licensed under the BSD Open Source Licence
# Please see the text file LICENCE for more information
# If this script is distributed, it must be accompanied by the Licence

from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from django_extensions.db.models import TimeStampedModel, TitleSlugDescriptionModel
from linkthru.managers import LinkThruManager

class LinkThruZone(TitleSlugDescriptionModel, TimeStampedModel):
    """
    a Model that describes the attributes and behaviours of a link zones

    A link zone is simply a location on a website so different size link thrus
    can be organized to display at different locations around the site.

    """
    class Meta:
        verbose_name = 'Link zone'
        verbose_name_plural = 'Link zones'

    def __unicode__(self):
        return "%s" % self.title

class LinkThruBase(TimeStampedModel):
    """
    This is our base model, from which all links will inherit.
    The manager methods for this model will determine which links to
    display return etc.

    """
    title = models.CharField(max_length=255)
    url = models.URLField(verify_exists=False)
    enabled = models.BooleanField(default=False)
    begins_on = models.DateTimeField(default=datetime.now)
    expires_on = models.DateTimeField(_('Expires on'), blank=True, null=True)
    updated = models.DateTimeField(editable=False, auto_now=True)
    zone = models.ForeignKey(LinkThruZone)

    objects = LinkThruManager()

    def __unicode__(self):
        return "%s" % self.title

    @models.permalink
    def get_view_url(self):
        return ('lt-linkthru-view', (), {'id': self.pk,})

    @models.permalink
    def get_absolute_url(self):
        return ('lt-linkthru-detail', (), {'id': self.pk,})

    def impressions(self, start=None, end=None):
        if start is not None:
            start_q=models.Q(impression_date__gte=start)
        else:
            start_q=models.Q()
        if end is not None:
            end_q=models.Q(impression_date__lte=end)
        else:
            end_q=models.Q()
        return self.adimpression_set.filter(start_q & end_q).count()

    def clicks(self, start=None, end=None):
        if start is not None:
            start_q=models.Q(click_date__gte=start)
        else:
            start_q=models.Q()
        if end is not None:
            end_q=models.Q(click_date__lte=end)
        else:
            end_q=models.Q()
        return self.adclick_set.filter(start_q & end_q).count()

class LinkImpression(models.Model):
    """
    The LinkImpression Model will record every time the ad is loaded on a page

    """
    impression_date = models.DateTimeField(auto_now=True)
    source_ip = models.IPAddressField(null=True, blank=True)
    link = models.ForeignKey(LinkThruBase)

    class Meta:
        verbose_name = 'Link Impression'
        verbose_name_plural = 'Link Impressions'

class LinkClick(models.Model):
    """
    The LinkClick model will record every click that a add gets

    """
    click_date = models.DateTimeField(default=datetime.now)
    source_ip = models.IPAddressField(null=True, blank=True)
    link = models.ForeignKey(LinkThruBase)

    class Meta:
        verbose_name = 'Link Click'
        verbose_name_plural = 'Link Clicks'

# Example Link Types
class TextLinkThru(LinkThruBase):
    """ A most basic, text based advert """
    content = models.TextField()

class ImageLinkThru(LinkThruBase):
    """ A standard image link thru """
    content = models.ImageField(upload_to="linkthru/images/")
