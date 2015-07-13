from django.db import models
from postgres.fields import JSONField
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from django.contenttypes.models import ContentType

User = get_user_model()


class DynoForm(models.model):
    fields = JSONField(_('fields'))
    created_by = models.ForeignKey(User)
    content_type = models.ForeignKey(ContentType)
