from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.http import is_safe_url

from .forms import ContactForm, LoginForm, RegisterForm, GuestForm
from .models import Guest


def home_page(request):
    context = {
        'title': 'Home',
        'content': 'Welcome to Home Page'
    }
    return render(request, 'home_page.html', context)


def about_page(request):
    context = {
        'title': 'About',
        'content': 'Welcome to About Page'
    }
    return render(request, 'home_page.html', context)


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        'title': 'Contact',
        'content': 'Welcome to Contact Page',
        'form': contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)

    if request.method == 'POST':
        print(request.POST)
        print(request.POST.get('fullname'))
    return render(request, 'contact/view.html', context)


def guest_register(request):
    form = GuestForm(request.POST or None)
    context = {
        'form': form,
    }
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    next_post = '/cart/checkout' # shudnt be this way
    redirect_path = next_ or next_post or None
    print(redirect_path)
    if form.is_valid():
        email       = form.cleaned_data.get('email')
        new_guest = Guest.objects.create(email=email)
        print(new_guest)
        print(new_guest.email)
        request.session['guest_id'] = new_guest.id
        if is_safe_url(redirect_path, request.get_host()):
            return redirect(redirect_path)
        else:
            return redirect('/register')

    return redirect('/register')


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        'form': form,
        'title': 'Login'
    }
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    next_post = '/cart/checkout' #shudnt be this way
    redirect_path = next_ or next_post or None
    print(redirect_path)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            try:
                del request.session['guest_id']
            except:
                pass
            if is_safe_url(redirect_path, request.get_host()):
                return redirect(redirect_path)
            else:
                return redirect('/')
        else:
            print('Error!')

    return render(request, 'accounts/login.html', context)


User = get_user_model()


def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        'form': form,
        'title': 'Register'
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        new_user = User.objects.create_user(username, email, password)
        print(new_user)
    return render(request, 'accounts/register.html', context)
