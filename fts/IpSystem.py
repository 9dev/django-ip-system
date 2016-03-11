from ._base import BaseTestCase

from main.models import Article


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
        self.assertEqual(ip_elem.text, '127.0.0.1')

    def test_can_save_and_see_object_creator_ip_if_ip_already_known(self):
        self.fail()

    def test_can_cope_with_incorrect_ip(self):
        self.fail()
