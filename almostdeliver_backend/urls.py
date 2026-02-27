from django.contrib import admin
from django.urls import path
from seller_pannel.views import home  # Ye line views se home function ko laati hai

urlpatterns = [
    path('admin/', admin.site.urls), # Ye admin panel ka rasta hai
    path('', home),  # Ye aapki main website (Lucknow service) ka rasta hai
]