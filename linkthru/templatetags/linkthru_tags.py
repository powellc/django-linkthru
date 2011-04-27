# -*- coding: utf-8 -*-

# © Copyright 2009 Andre Engelbrecht. All Rights Reserved.
# This script is licensed under the BSD Open Source Licence
# Please see the text file LICENCE for more information
# If this script is distributed, it must be accompanied by the Licence

import logging
from django import template
from linkthru.models import LinkThruBase, LinkImpression
from datetime import datetime

register = template.Library()

@register.inclusion_tag('linkthru/link_tag.html', takes_context=True)
def random_zone_link(context, lin_zone):
    """
    Returns a random linkthru from the database.

    In order for the impression to be saved add the following
    to the TEMPLATE_CONTEXT_PROCESSORS:

    'linkthru.context_processors.get_source_ip'

    Tag usage:
    {% load linkthru_tags %}
    {% random_zone_link 'zone_slug' %}

    """
    to_return = {}

    # Retrieve a random link for the category and zone
    link = LinkThruBase.objects.get_random_link(link_zone)
    to_return['link'] = link
    
    # Record a impression for the link 
    if context.has_key('from_ip') and link:
        from_ip = context.get('from_ip')
        excluded_ip = context.get('excluded_ip')
        if not excluded_ip:
            try:
                impression = LinkImpression(
                        link=link,
                        impression_date=datetime.now(),
                        source_ip=from_ip
                )
                impression.save()
            except:
                pass
    return to_return

@register.inclusion_tag('linkthru/link_tag_block.html', takes_context=True)
def random_zone_link_block(context, link_zone, number):
    """
    Returns a block of random linkthrus from the database.

    In order for the impression to be saved add the following
    to the TEMPLATE_CONTEXT_PROCESSORS:

    'linkthru.context_processors.get_source_ip'

    Tag usage:
    {% load linkthru_tags %}
    {% random_zone_link_block 'zone_slug' 4 %}

    """
    to_return = {}

    # Retrieve a random link for the category and zone
    links=[]

    logging.debug('Looking up linkthrus for %s' % link_zone)
    # Check whether category has been specified
    lookup_links=LinkThruBase.objects.filter(enabled=True, zone__slug=link_zone)

    # If we have fewer links in system, adjust our block
    if len(lookup_links) < number: number = len(lookup_links)

    while(number > 0):
        new_link= LinkThruBase.objects.get_random_link(link_zone)
        if new_link in links:
            pass
        else:
            logging.debug('Adding ad %s to the list' % new_link)
            links.append(new_link)
            number=number-1
        
            # Record a impression for the link 
            if new_link:
                excluded_ip = context.get('excluded_ip')
                if not excluded_ip:
                    try:
                        impression = LinkImpression(
                                link=new_link,
                                impression_date=datetime.now(),
                                source_ip=context.get('from_ip')
                                )
                        impression.save()
                    except:
                        pass
    to_return['links'] = links
    return to_return

