from django.conf import settings
from django.db import models
from django.db.models import permalink
from postgres.fields import JSONField
from django.utils.translation import ugettext_lazy as _


class Schema(models.Model):
    name = models.CharField(_('name'), max_length=30,
                            help_text=_('A name to identify the schema'))
    fields = JSONField(_('fields'))
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.name

    @permalink
    def new_entry_url(self):
        return ('dynoforms-new-entry', [self.pk])


class Entry(models.Model):
    schema = models.ForeignKey(Schema)
    data = JSONField(_('data'), blank=True)
    deleted = models.BooleanField(_('deleted'), default=False, editable=False)

    @permalink
    def get_absolute_url(self):
        return ('dynoforms-entry-detail', [self.pk])
