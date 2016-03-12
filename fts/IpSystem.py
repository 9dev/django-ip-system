from ._base import BaseTestCase

from ip_system.models import Ip

from main.models import Article


SELENIUM_IP = '127.0.0.1'


class TestIpSystem(BaseTestCase):

    def test_can_save_and_see_object_creator_ip_if_new_ip(self):
        # Florence hits the article create page.
        self.get('/create')

        # She fills the form.
        self.set_field('id_title', 'MyTitle')
        self.set_field('id_content', 'Some interesting content...')

        # She submits the form.
        self.submit()

        # She is being redirected to article detail page.
        pk = Article.objects.all().last().pk
        self.assertEqual(self.browser.current_url, self.get_full_url('/article/{}'.format(pk)))

        # She can see her IP address there.
        ip_elem = self.get_by_id('id_author_ip')
        self.assertEqual(ip_elem.text, SELENIUM_IP)

    def test_can_save_and_see_object_creator_ip_if_ip_already_known(self):
        # Florence's IP address is already in the database.
        Ip.objects.create(address=SELENIUM_IP)

        # Florence hits the article create page.
        self.get('/create')

        # She fills the form.
        self.set_field('id_title', 'MyTitle')
        self.set_field('id_content', 'Some interesting content...')

        # She submits the form.
        self.submit()

        # She is being redirected to article detail page.
        pk = Article.objects.all().last().pk
        self.assertEqual(self.browser.current_url, self.get_full_url('/article/{}'.format(pk)))

        # She can see her IP address there.
        ip_elem = self.get_by_id('id_author_ip')
        self.assertEqual(ip_elem.text, SELENIUM_IP)
