from django.shortcuts import redirect
from django.template import loader
from django.http import HttpRequest, HttpResponse

from home.plotter import (
    plot_categories_by_money_spent,
    plot_categories_by_sub_sum,
    bar_for_subs,
)

# Create your views here.


def hello(request: HttpRequest):
    template = loader.get_template("homeTemplate.html")
    if request.user.is_authenticated:
        plot_categories_by_sub_sum(request.user)
        plot_categories_by_money_spent(request.user)
        bar_for_subs(request.user)
    return HttpResponse(template.render(request=request))

def redirect_to_hello(request):
    return redirect("hello")
