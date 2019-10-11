# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

from passerelle.base.models import BaseResource
from passerelle.utils.api import endpoint
from passerelle.utils.jsonresponse import APIError


class ReunionConnector(BaseResource):

    server = models.CharField(max_length=128, verbose_name=_('DB server'))
    username = models.CharField(max_length=128, verbose_name=_('DB user'))
    password = models.CharField(max_length=128, verbose_name=_('DB server'), null=True, blank=True)

    category = 'Divers'

    class Meta:
        verbose_name = u'Connecteur de test réunion'

    @endpoint(description_get=_('Ping'), methods=['get'], perm='can_access')
    def ping(self, request):
        return {'data': 'pong'}
