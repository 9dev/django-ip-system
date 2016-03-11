from django.core.exceptions import ValidationError
from django.core.validators import ip_address_validators


def get_ip_from_request(request):
    headers = (
        'HTTP_X_REAL_IP',
        'REMOTE_ADDR',
    )

    for header in headers:
        ip = request.META.get(header)
        if ip:
            try:
                ip_address_validators('both', ip)
                return ip
            except ValidationError:
                pass

    return None
