from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Order

# बस ये एक लाइन काफी है
admin.site.register(Order)