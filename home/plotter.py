from django.shortcuts import get_object_or_404
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import os
from pathlib import Path
from django.db.models import Sum

from home.models import Category, Subscription

matplotlib.use('Agg')

def plot_categories_by_sub_sum(user):
    catname=[]
    subsum=[]
    for cat in Category.objects.filter(user=user):
        catname.append(cat.name)
        subsum.append(Subscription.objects.filter(category=get_object_or_404(Category,name=cat.name,user=user)).count())
    
    data = np.array(subsum)
    plt.pie(x=data,labels=catname)

    my_path = Path(os.path.abspath(__file__)).parent.absolute()
    plt.savefig(str(my_path)+'/static/plots/categories_by_sub_sum.png')
    plt.close()

def plot_categories_by_money_spent(user):
    catname=[]
    moneysum=[]
    for cat in Category.objects.filter(user=user):
        catname.append(cat.name)
        moneysum.append(Subscription.objects.filter(category=get_object_or_404(Category,name=cat.name,user=user)).aggregate(Sum("price"))['price__sum'])

    
    data = np.array(moneysum)

    def absolute_value(val):
        a  = np.round(val/100.*data.sum(), 0)
        return a

    plt.pie(x=data,labels=catname,autopct=absolute_value)

    my_path = Path(os.path.abspath(__file__)).parent.absolute()
    plt.savefig(str(my_path)+'/static/plots/categories_by_money_spent.png')
    plt.close()

def bar_for_subs(user):
    names = []
    prices=[]

    subnum = Subscription.objects.filter(user=user).count()

    limit = 5 if subnum > 5 else subnum
    for sub in Subscription.objects.filter(user=user).order_by('-price')[:limit]:
        names.append(sub.service_name)
        prices.append(sub.price)
    x = np.array(names)
    y = np.array(prices)


    plt.bar(x,y, color = "red")
    my_path = Path(os.path.abspath(__file__)).parent.absolute()
    plt.savefig(str(my_path)+'/static/plots/for_subs.png')
    plt.close()