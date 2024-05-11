import django.test


class TestView(django.test.TestCase):
    def test_home_valid_url(self):
        result = self.client.get("/hello/")
        self.assertEqual(result.status_code, 200)

    def test_home_redirect(self):
        result = self.client.get("/")
        self.assertEqual(result.status_code,302)