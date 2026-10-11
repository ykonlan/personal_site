from django.test import SimpleTestCase

# Create your tests here.
class HomepageTest(SimpleTestCase):
    def test_homepage_exists_at_url(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_about_exists_at_url(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)
