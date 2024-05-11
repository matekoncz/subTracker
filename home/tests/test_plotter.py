import django.test
from django.contrib.auth.models import User
from home.models import Category, Subscription
from home import plotter

class TestPlotter(django.test.TestCase):
    def test_plot_sub_number(self):
        data = {"username":"proba", "email":"proba@proba.com", "password1":"validpassword", "password2":"validpassword"}
        self.client.post("/registration/",data=data)
        self.client.post("/login/",data={"username":"proba","password":"validpassword"})
        category = {"name":"catname","description":"catdesc"}
        self.client.post("/addCategory/",data=category)
        sub = {"service_name":"netflix","price":10,"category":"catname"}
        self.client.post("/addsubscription/",data=sub)
        my_user = User.objects.get(username="proba")
        data = plotter.plot_categories_by_sub_sum(my_user)
        self.assertEqual(data['names'][0],"catname")
        self.assertEqual(data['sums'][0],1)

    def test_plot_money_sum(self):
        data = {"username":"proba", "email":"proba@proba.com", "password1":"validpassword", "password2":"validpassword"}
        self.client.post("/registration/",data=data)
        self.client.post("/login/",data={"username":"proba","password":"validpassword"})
        category = {"name":"catname","description":"catdesc"}
        self.client.post("/addCategory/",data=category)
        sub = {"service_name":"netflix","price":10,"category":"catname"}
        self.client.post("/addsubscription/",data=sub)
        my_user = User.objects.get(username="proba")
        data = plotter.plot_categories_by_money_spent(my_user)
        self.assertEqual(data['names'][0],"catname")
        self.assertEqual(data['sums'][0],10)

    def test_plot_bar_for_subs(self):
        data = {"username":"proba", "email":"proba@proba.com", "password1":"validpassword", "password2":"validpassword"}
        self.client.post("/registration/",data=data)
        self.client.post("/login/",data={"username":"proba","password":"validpassword"})
        category = {"name":"catname","description":"catdesc"}
        self.client.post("/addCategory/",data=category)
        sub = {"service_name":"netflix","price":10,"category":"catname"}
        self.client.post("/addsubscription/",data=sub)
        my_user = User.objects.get(username="proba")
        data = plotter.bar_for_subs(my_user)
        self.assertEqual(data['names'][0],"netflix")
        self.assertEqual(data['prices'][0],10)