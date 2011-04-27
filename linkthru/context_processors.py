def get_source_ip(request):
    from_ip = request.META['REMOTE_ADDR']
    # forwarded proxy fix
    if (not from_ip or from_ip == '127.0.0.1') and request.META.has_key('HTTP_X_FORWARDED_FOR'):
        from_ip = request.META['HTTP_X_FORWARDED_FOR']

    try:
        return {'from_ip': from_ip, 'excluded_ip': request.excluded_ip }
    except:
        return {'from_ip': from_ip }
