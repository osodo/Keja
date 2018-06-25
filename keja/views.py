from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth.decorators import login_required, permission_required
from keja.models import Caretaker, House, Review
from keja.forms import CaretakerForm, HouseForm, ReviewForm
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.utils import timezone
from django.template.context_processors import csrf
from django.core.paginator import Paginator, EmptyPage, Page
from django.contrib import auth
from django.contrib.auth.models import User
from django.db.models import Q
#from allauth.account.forms import LoginForm, SignupForm
from django.views.generic.edit import FormView
# Create your views here.


def houses(request):
    return render_to_response(template_name="home.html", context=None)

def home(request):
    house_list = House.objects.all()
    paginator = Paginator(house_list, per_page=4, allow_empty_first_page=False)
    page = request.GET.get("page")
    houses = paginator.get_page(page)
    context = {"houses":houses}
    template = "home.html"
    return render(request, template, context)

def caretakers(request):
    caretaker_list = Caretaker.objects.all()
    paginator = Paginator(caretaker_list, per_page=1, allow_empty_first_page=False)
    page = request.GET.get("page")
    caretakers = paginator.get_page(page)
    context = {"caretakers":caretakers}
    template = "caretakers.html"
    return render(request, template, context)

def house(request, house_id):
    house = House.objects.get(id=house_id)
    return render_to_response("house.html", {"house":house})

def caretaker(request, caretaker_id):
    caretaker = Caretaker.objects.get(id=caretaker_id)
    return render_to_response("caretaker.html", {"caretaker":caretaker})

def like_house(request, house_id):
    if house_id:
        house = House.objects.get(id=house_id)
        count = house.rating
        count += 1
        house.rating = count
        house.save()

    return HttpResponseRedirect("/house/%s" % house_id)

def search(request):
    template = "search.html"
    search_text = request.GET.get("search")
    results = House.objects.filter(Q(name__icontains=search_text)|Q(description__icontains=search_text))
    context = {"results":results}
    return render(request, template, context)

def register_house(request):
    if request.POST:
        form = HouseForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(redirect_to="")

    else:
        form = HouseForm()
    args = {}
    args.update(csrf(request))
    args["form"] = form
    return render_to_response("register_house.html", args)

def register_caretaker(request):
    if request.POST:
        form = CaretakerForm(request.POST)
        form.instance.user_id = request.user.id
        if form.is_valid():
            print(request.user)
            form.save()
            return HttpResponseRedirect(redirect_to="/")
    else:
        form = CaretakerForm()
    args = {}
    args.update(csrf(request))
    args["form"] = form
    return render_to_response("register_caretaker.html", args)

def add_comment(request, house_id):
    house = House.objects.get(id=house_id)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.publish_date = timezone.now()
            temp.house = house
            temp.save()
            return HttpResponseRedirect("/house/%s" % house_id)
    else:
        form = ReviewForm()
    args = {}
    args.update(csrf(request))
    args["house"] = house
    args['form'] = form
    return render_to_response("add_comment.html", args)

def bookings(request):
    return render_to_response(template_name="home.html", context=None)

"""
def search(request):
    if request.method == "GET":
        search_text = request.GET.get("search")
        try:
            houses = House.objects.filter(name__icontains=search_text)
        except House.DoesNotExist:
            houses = None
        return render(request, "search.html", {"houses":houses})
    else:
        return render(request, "search.html", {})
"""
