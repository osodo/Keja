from __future__ import unicode_literals
from django.db import models
from PIL import Image
from time import time
from django.contrib.auth.models import User

# Create your models here.
def profile_image(instance, filename):
    return "profile_image/%s_%s" % (str(time()).replace(".", "_"), filename)
def house_photo(instance, filename):
    return "house_photo/%s_%s" % (str(time()).replace(".", "_"), filename)
def house_video(instance, filename):
    return "house_video/%s_%s" % (str(time()).replace(".", "_"), filename)

class Caretaker(models.Model):
    UNIVERSITIES = (
        ("JKUAT", 'Jommo Kenyatta University of Agriculture and technology'),
        ('UON', 'University of Nairobi'),
        ('KU', 'Kenyatta University'),
    )
    PLACE = (
        ("Juja", "Juja"),
        ("Nairobi","Nairobi"),
        ("Kahawa","Kahawa"),
    )
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING, null=False)
    name = models.CharField(max_length=100, null=False)
    profile_bio = models.TextField(null=True, blank=True)
    profile_image = models.FileField(upload_to=profile_image, null=True, blank=True)
    email_address = models.EmailField(null=True)
    phone_number = models.BigIntegerField(null=False, blank=True)
    place_from = models.TextField(help_text="Caretaker's place from", choices=PLACE, max_length=1, null=False)
    university_name = models.TextField(help_text="Around which university is the house located", choices=UNIVERSITIES, max_length=1, null=False)

    def __str__(self):
        return self.name

class House(models.Model):
    Room = (
    ("Two sharing","Two sharing"),
    ("Four sharing","Four sharing"),
    ("Hostel", "Hostel"),
    ("Bedsitter","Bedsitter"),
    ("One bedroom","One bedroom"),
    ("Two bedroom","Two bedroom"),
    ("Three bedroom","Three bedroom"),
    )
    name = models.CharField(max_length=100, null=False)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    description = models.TextField(null=False)
    room_type = models.TextField(help_text="The type of room eg Bedsitter or One bedroom", choices=Room, max_length=3, null=False)
    house_photo = models.FileField(upload_to=house_photo, null=False, blank=False)
    house_video = models.FileField(upload_to=house_video, null=True, blank=True)
    floor_number = models.IntegerField(help_text="How many floors including ground floor", null=False)
    plot_area = models.BigIntegerField(help_text="The total area of the plot", null=True)
    security_company = models.CharField(null=True, max_length=100)
    special_features = models.TextField(null=True)
    caretaker = models.ForeignKey(Caretaker, on_delete=models.DO_NOTHING, null=False)
    rating = models.IntegerField(null=True, default=0)
    def __str__(self):
        return self.name

class Review(models.Model):
    name = models.CharField(max_length=100)
    review_content = models.TextField(blank=False, null=False)
    publish_date = models.DateTimeField("Date published")
    house = models.ForeignKey(House, on_delete=models.DO_NOTHING, null=False)
