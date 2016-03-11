from django.db import models
from django.core.urlresolvers import reverse

from ip_system.models import Ip


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=10000)
    author_ip = models.ForeignKey(Ip, null=True)

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'pk': self.pk})
