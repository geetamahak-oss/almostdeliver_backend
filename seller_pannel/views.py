from django.shortcuts import render
from .models import Order # यह आपके डेटाबेस मॉडल को लाता है

def home(request):
    # डेटाबेस से सारे ऑर्डर्स निकालें
    all_orders = Order.objects.all() 
    # ऑर्डर्स को HTML पेज (index.html) पर भेजें
    return render(request, 'seller_pannel/index.html', {'orders': all_orders})