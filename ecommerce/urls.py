from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from django.contrib import admin
from django.urls import path, include
from accounts.views import login_page, home_page, register_page, about_page, contact_page, guest_register
# from .views import about_page, contact_page

urlpatterns = [
    path('', home_page, name='home'),
    path('about/', about_page, name='about'),
    path('contact/', contact_page, name='contact'),
    path('login/', login_page, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register_page, name='register'),
    path('register/guest', guest_register, name='guest_register'),

    path('cart/', include('carts.urls', namespace='cart')),
    path('products/', include('products.urls', namespace='products')),
    path('search/', include('search.urls', namespace='search')),

    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
