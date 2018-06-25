"""airbnb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import login, logout
from keja import views as keja_views

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', keja_views.home, name="home"),
    url(r"register_house", keja_views.register_house, name="register_house"),
    url(r"register_caretaker", keja_views.register_caretaker, name="register_caretaker"),
    url(r"accounts/", include("allauth.urls")),
    url(r"bookings", keja_views.bookings, name="bookings"),
    url(r"houses", keja_views.home, name="houses"),
    url(r"^caretakers/", keja_views.caretakers, name="caretakers"),
    url(r"^caretaker/(?P<caretaker_id>\d+)", keja_views.caretaker, name="caretaker"),
    url(r"^search/$", keja_views.search, name="search"),
    url(r"^house/(?P<house_id>\d+)", keja_views.house, name="house"),
    url(r"^like/(?P<house_id>\d+)/$", keja_views.like_house, name="like_house"),
    url(r"^add_comment/(?P<house_id>\d+)$", keja_views.add_comment, name="add_comment"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
