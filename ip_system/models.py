from django.db import models

from .utils import get_ip_from_request


class Ip(models.Model):
    address = models.GenericIPAddressField()

    @classmethod
    def get_or_create(cls, request):
        raw_ip = get_ip_from_request(request)
        obj, _ = cls.objects.get_or_create(address=raw_ip)
        return obj

    def __str__(self):
        return self.address.__str__()
