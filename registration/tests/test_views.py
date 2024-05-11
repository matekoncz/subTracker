import django.test
from django.contrib.auth.models import User


class TestViews(django.test.TestCase):
    def test_registration_url_valid(self):
        result = self.client.get("/registration/")
        self.assertEqual(result.status_code, 200)

    def test_registration_data_invalid(self):
        result = self.client.post("/registration/", data={})
        self.assertEqual(result.status_code, 200)

    def test_registration_data_valid(self):
        self.assertEqual(User.objects.count(), 0)
        data = {
            "username": "proba",
            "email": "proba@proba.com",
            "password1": "validpassword",
            "password2": "validpassword",
        }
        result = self.client.post("/registration/", data=data)
        self.assertEqual(result.status_code, 302)
        self.assertEqual(User.objects.count(), 1)

    def test_login_url_valid(self):
        result = self.client.get("/login/")
        self.assertEqual(result.status_code, 200)

    def test_login_invalid_data(self):
        result = self.client.post("/login/", data={})
        self.assertEqual(result.status_code, 200)

    def test_login_valid_data_auth_failed(self):
        result = self.client.post("/login/", data={"username": "en", "password": "te"})
        self.assertEqual(result.status_code, 200)

    def test_login_vaild_data_auth_passed(self):
        data = {
            "username": "proba",
            "email": "proba@proba.com",
            "password1": "validpassword",
            "password2": "validpassword",
        }
        self.client.post("/registration/", data=data)
        result = self.client.post(
            "/login/", data={"username": "proba", "password": "validpassword"}
        )
        self.assertEqual(result.status_code, 302)
