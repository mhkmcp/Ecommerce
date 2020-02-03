from django.urls import path
from . import views as v

app_name = 'cart'

urlpatterns = [
    path('', v.cart_home, name='home'),
    path('update', v.cart_update, name='update'),
    path('checkout', v.checkout_home, name='checkout'),
]
