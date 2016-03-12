from django.db import models
from django.core.urlresolvers import reverse

from ip_system.fields import IpField


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=10000)
    author_ip = IpField()

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'pk': self.pk})
