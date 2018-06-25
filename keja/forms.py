from django import forms
from keja.models import Caretaker, House, Review
from django.utils import timezone

class CaretakerForm(forms.ModelForm):
    class Meta:
        model = Caretaker
        fields = ("name", "profile_bio","profile_image","email_address","phone_number","place_from", "university_name")

class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = ("name","price","description","house_photo", "house_video","room_type","floor_number","plot_area","security_company","special_features")

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ("name","review_content")
