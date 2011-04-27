#! /usr/bin/env python
# emacs-mode: -*- python-*-
# -*- coding: utf-8 -*-
import logging
from datetime import datetime 
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from django.http import HttpResponseRedirect 
from linkthru.models import LinkThruBase, LinkClick, ImageLinkThru, LinkImpression

def linkthru_view(request, id):
    """
    Record the click in the database, then redirect to the thru url

    """
    link = get_object_or_404(LinkBase, id=id)
    logging.debug('Found ad: %s, redirecting...' % (ad))
    try:
        click = LinkClick(ad=ad, click_date=datetime.now(), source_ip=request.META.get('REMOTE_ADDR'))
        click.save()
    except:
        raise Http404
    return HttpResponseRedirect(link.url)

def linkthru_detail(request, id):
    link = get_object_or_404(LinkBase, id=id)
    return render_to_response('linkthru/linkthru_detail.html', locals(),
                              context_instance=RequestContext(request))



