# Much of this file is taken straight from django-ban project
import logging

from django.conf import settings

from ipfilter.models import ExcludedIP
from ipfilter.signals import excluded_ip_found

logger = logging.getLogger('django_ipfilter: IP address filtering started')

splits = lambda x: x.replace(' ','').split(',')

def get_ip(req):
    ip = req.META['REMOTE_ADDR']
    # forwarded proxy fix for proxy passing setups
    if (not ip or ip == '127.0.0.1') and req.META.has_key('HTTP_X_FORWARDED_FOR'):
        ip = req.META['HTTP_X_FORWARDED_FOR']
    return ip

def is_ip_in_nets(ip, nets):
    for net in nets:
        if ip in net:
            return True
    return False

class FilterIPs(object):
    def process_request(self, request):
        # gather some info
        request_ip = get_ip(request)
        excluded_ips = [i.get_network() for i in ExcludedIP.objects.all()]

        logger.debug(excluded_ips)
        
        request.excluded_ip = lambda: is_ip_in_nets(request_ip, excluded_ips)
        if request.excluded_ip:
                excluded_ip_found.send(sender=request, ip=request_ip)

