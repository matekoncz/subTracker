import django.test
from home.models import Category, Subscription


class TestView(django.test.TestCase):
    def test_add_remove_auth_failed(self):
        result = self.client.get("/myrecords/")
        self.assertEqual(result.status_code, 302)

    def test_add_remove_auth_passed(self):
        data = {
            "username": "proba",
            "email": "proba@proba.com",
            "password1": "validpassword",
            "password2": "validpassword",
        }
        self.client.post("/registration/", data=data)
        self.client.post(
            "/login/", data={"username": "proba", "password": "validpassword"}
        )
        result = self.client.get("/myrecords/")
        self.assertEqual(result.status_code, 200)

    def test_add_valid_category(self):
        data = {
            "username": "proba",
            "email": "proba@proba.com",
            "password1": "validpassword",
            "password2": "validpassword",
        }
        self.client.post("/registration/", data=data)
        self.client.post(
            "/login/", data={"username": "proba", "password": "validpassword"}
        )
        category = {"name": "catname", "description": "catdesc"}
        result = self.client.post("/addCategory/", data=category)
        self.assertEqual(result.status_code, 302)
        self.assertEqual(Category.objects.count(), 1)

    def test_add_invalid_category(self):
        data = {
            "username": "proba",
            "email": "proba@proba.com",
            "password1": "validpassword",
            "password2": "validpassword",
        }
        self.client.post("/registration/", data=data)
        self.client.post(
            "/login/", data={"username": "proba", "password": "validpassword"}
        )
        category = {}
        result = self.client.post("/addCategory/", data=category)
        self.assertEqual(result.status_code, 302)
        self.assertEqual(Category.objects.count(), 0)

    def test_add_valid_subscription(self):
        data = {
            "username": "proba",
            "email": "proba@proba.com",
            "password1": "validpassword",
            "password2": "validpassword",
        }
        self.client.post("/registration/", data=data)
        self.client.post(
            "/login/", data={"username": "proba", "password": "validpassword"}
        )
        category = {"name": "catname", "description": "catdesc"}
        self.client.post("/addCategory/", data=category)
        sub = {"service_name": "netflix", "price": 10, "category": "catname"}
        result = self.client.post("/addsubscription/", data=sub)
        self.assertEqual(result.status_code, 302)
        self.assertEqual(Subscription.objects.count(), 1)

    def test_add_invalid_subscription(self):
        data = {
            "username": "proba",
            "email": "proba@proba.com",
            "password1": "validpassword",
            "password2": "validpassword",
        }
        self.client.post("/registration/", data=data)
        self.client.post(
            "/login/", data={"username": "proba", "password": "validpassword"}
        )
        category = {"name": "catname", "description": "catdesc"}
        self.client.post("/addCategory/", data=category)
        sub = {}
        result = self.client.post("/addsubscription/", data=sub)
        self.assertEqual(result.status_code, 302)
        self.assertEqual(Subscription.objects.count(), 0)
