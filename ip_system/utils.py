from django.core.exceptions import ValidationError
from django.core.validators import validate_ipv46_address


def get_ip_from_request(request):
    headers = (
        'HTTP_X_REAL_IP',
        'REMOTE_ADDR',
    )

    for header in headers:
        ip = request.META.get(header)
        if ip:
            try:
                validate_ipv46_address(ip)
                return ip
            except ValidationError:
                pass

    return None
