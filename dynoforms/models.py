from django.conf import settings
from django.db import models
from django.db.models import permalink
from django.contrib.postgres.fields import JSONField
from django.core.serializers.json import DjangoJSONEncoder
from django.utils.translation import ugettext_lazy as _


class BaseModel(models.Model):
    created = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated = models.DateTimeField(_("Last update"), auto_now=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                               help_text="Who created it")
    deleted = models.BooleanField(_('deleted'), default=False, editable=False)

    class Meta(object):
        abstract = True


class Schema(BaseModel):
    name = models.CharField(_('name'), max_length=30,
                            help_text=_('A name to identify the schema'))
    description = models.TextField(
        _('description'),
        help_text=_('A description to guide the form usage'),
        blank=True,
    )
    fields = JSONField(_('fields'), encoder=DjangoJSONEncoder)

    def __str__(self):
        return self.name

    @permalink
    def new_entry_url(self):
        return ('dynoforms-new-entry', [self.pk])


class Entry(BaseModel):
    schema = models.ForeignKey(Schema)
    data = JSONField(_('data'), encoder=DjangoJSONEncoder, blank=True)

    @permalink
    def get_absolute_url(self):
        return ('dynoforms-entry-detail', [self.pk])
