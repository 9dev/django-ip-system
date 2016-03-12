from unittest.mock import patch

from django.test import TestCase

from .models import Ip
from .utils import get_ip_from_request


TEST_IP = '127.0.0.1'
TEST_IPv6 = 'FE80:0000:0000:0000:0202:B3FF:FE1E:8329'


class RequestMock:
    def __init__(self, meta=None):
        if meta is None:
            meta = {}
        self.META = meta


class TestUtils(TestCase):

    def test_can_get_ip_if_only_HTTP_X_REAL_IP_present(self):
        request = RequestMock({'HTTP_X_REAL_IP': TEST_IP})
        ip = get_ip_from_request(request=request)
        self.assertEqual(ip, TEST_IP)

    def test_can_get_ip_if_only_REMOTE_ADDR_present(self):
        request = RequestMock({'REMOTE_ADDR': TEST_IP})
        ip = get_ip_from_request(request=request)
        self.assertEqual(ip, TEST_IP)

    def test_can_get_IPv6_address(self):
        request = RequestMock({'REMOTE_ADDR': TEST_IPv6})
        ip = get_ip_from_request(request=request)
        self.assertEqual(ip, TEST_IPv6)

    def test_cannot_get_ip_if_no_headers_present(self):
        request = RequestMock()
        ip = get_ip_from_request(request=request)
        self.assertEqual(ip, None)

    def test_cannot_get_ip_if_ip_incorrect(self):
        request = RequestMock({'REMOTE_ADDR': 'cc.xx.cc.xx'})
        ip = get_ip_from_request(request=request)
        self.assertEqual(ip, None)


@patch('ip_system.models.get_ip_from_request')
class TestModels(TestCase):

    def test_can_create_Ip_object_if_raw_ip_correct(self, mock_get_ip):
        mock_get_ip.return_value = TEST_IP
        request = None

        Ip.get_or_create(request=request)
        obj = Ip.objects.latest('pk')

        mock_get_ip.assert_called_once_with(request)
        self.assertEqual(obj.address, TEST_IP)

    def test_can_create_Ip_object_if_ip_exists(self, mock_get_ip):
        Ip.objects.create(address=TEST_IP)
        mock_get_ip.return_value = TEST_IP
        request = None

        Ip.get_or_create(request=request)
        obj = Ip.objects.latest('pk')

        mock_get_ip.assert_called_once_with(request)
        self.assertEqual(obj.address, TEST_IP)

    def test_cannot_create_Ip_object_if_raw_ip_incorrect(self, mock_get_ip):
        mock_get_ip.return_value = None
        request = None

        obj = Ip.get_or_create(request=request)

        mock_get_ip.assert_called_once_with(request)
        self.assertEqual(Ip.objects.all().count(), 0)
        self.assertEqual(obj, None)
