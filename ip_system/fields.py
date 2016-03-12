from django.db.models import ForeignKey

from ip_system.models import Ip


IpField = lambda: ForeignKey(Ip, null=True)
