import ipcalc

from django.db import models
from django.utils.translation import ugettext_lazy as _

class ExcludedIP(models.Model):
    title = models.CharField(_('Title'), max_length=100)
    network = models.CharField(_('IP network'), max_length=18, help_text='Insert one ip address or a network mask (i.e. 10.1.1.0/24) to exclude a whole network.')
    
    def __unicode__(self):
        return self.title
    
    def get_network(self):
        return ipcalc.Network(self.network)
    
    class Meta:
        verbose_name = _('IP mask to exclude')
        verbose_name_plural = _('IP masks to exclude')