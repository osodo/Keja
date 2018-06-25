from django.contrib import admin
from keja.models import Caretaker, House, Review
# Register your models here.

class profileAdmin(admin.ModelAdmin):
    class Meta:
        model = Caretaker, House, Review

admin.site.register(Caretaker, profileAdmin)
admin.site.register(House, profileAdmin)
