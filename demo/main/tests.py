from unittest.mock import patch

from django.test import TestCase

from ip_system.models import Ip

from .models import Article


@patch('ip_system.models.get_ip_from_request')
class TestModels(TestCase):

    def test_can_create_empty_foreign_key_to_Ip_model(self, mock_get_ip):
        request = None
        mock_get_ip.return_value = None

        author_ip = Ip.get_or_create(request=request)
        article = Article.objects.create(title='title', content='content', author_ip=author_ip)

        self.assertEqual(article.author_ip, None)
