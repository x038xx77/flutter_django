from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class InfoMenuPage(models.Model):
    title = models.CharField(_('title'), max_length=5000)
    description = models.CharField(_('description'), max_length=300000)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
