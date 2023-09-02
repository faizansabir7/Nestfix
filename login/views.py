from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from .models import User, Service, ServiceProvider, Comment, Booking
from .utils import nearestcity
from django.views.decorators.cache import cache_control
from django.views.decorators.csrf import csrf_exempt


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def index(request):
    return render(request, "login/index.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        try:
            user = User.objects.get(username=username)
            if user.is_active == False:
                return render(request, "login/login.html", {
                    "message": "Registration successful. Please wait for admin approval."
                })
        except:
            user = authenticate(request, username=username, password=password)

        # Check if authentication successful

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
            # return render(request, "login/services.html", {
            #     "services": Service.objects.all()
            # })
        else:
            return render(request, "login/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "login/login.html")


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        phno = request.POST["tel"]
        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "login/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.phno = phno
            user.save()
        except IntegrityError:
            return render(request, "login/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "login/register.html")


def spregister(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        print('ffff')
        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        district = request.POST["district"]
        city = request.POST["city"]
        tel = request.POST["tel"]
        service = Service.objects.get(id=request.POST["service"])
        certificate = request.FILES['ccc']
        if password != confirmation:
            return render(request, "login/spregister.html", {
                "message": "Passwords must match."
            })

        # Create new user with status "pending"
        user = User.objects.create_user(username, email, password)
        user.phno = tel
        sp = ServiceProvider(user=user, service=service,
                             district=district, city=city)
        sp.save()
        user.is_active = False
        if certificate:
            user.certificate = certificate

        user.save()

        return render(request, "login/spregister.html", {
            "message": "Registration successful. Please wait for admin approval."
        })
    else:
        return render(request, "login/spregister.html", {
            "services": Service.objects.all()

        })


def services(request):
    return render(request, "login/services.html", {
        "services": Service.objects.all()
    })


def service(request, id):
    if request.method == 'POST':
        if 'city' in request.POST:
            print('city')
            city = request.POST['city']
            district = request.POST['district']
            request.session['pdistrict'] = district
            request.session['pcity'] = city
            splist = nearestcity(district, city)

            return render(request, "login/service.html", {
                "item": Service.objects.get(id=id),
                "my_list": splist
            })
        else:
            print('hello')
            return render(request, "login/service.html", {
                "item": Service.objects.get(id=id)

            })


def getsp(request, username):
    form_submitted = False
    district = request.session.get('pdistrict')
    city = request.session.get('pcity')
    if request.method == 'POST':
        sp = ServiceProvider.objects.get(
            user=User.objects.get(username=username))
        if Booking.objects.filter(user=request.user, sp=sp, complete=False).exists():
            form_submitted = True
            messages.warning(request, 'Booking is already active.')

        else:
            a = Booking(user=request.user, sp=sp, district=district, city=city)
            a.save()
            form_submitted = True
            messages.success(
                request, 'Congratulations! Your Booking is successful. Our Service Provider will contact you soon.')

    return render(request, 'login/getsp.html', {
        "item": ServiceProvider.objects.get(user=User.objects.get(username=username)),
        "comments": Comment.objects.filter(sp=ServiceProvider.objects.get(user=User.objects.get(username=username))).order_by('-created_at'),
        "form_submitted": form_submitted

    })


def orders(request):
    if request.method == "POST":

        a = Booking.objects.get(id=request.POST['hidden-field'])
        a.complete = True
        a.save()

    if request.GET.get('link'):
        complete_orders = Booking.objects.filter(
            complete=True, user=request.user)
        pending_orders = Booking.objects.filter(
            complete=False, user=request.user)
        return render(request, 'login/orders.html', {
            "complete_orders": complete_orders, "pending_orders": pending_orders,
            "sp": False

        })

    else:
        return render(request, 'login/orders.html', {
            "orders": Booking.objects.filter(sp=ServiceProvider.objects.get(user=request.user), complete=False).order_by('datetime'),
            "sp": True

        })


def comment(request, bid):
    if request.GET.get('link'):

        if Booking.objects.filter(id=bid).exists():
            booking = Booking.objects.get(id=bid)
            booking.cancel()
        complete_orders = Booking.objects.filter(
            complete=True, user=request.user)
        pending_orders = Booking.objects.filter(
            complete=False, user=request.user)
        return render(request, 'login/orders.html', {
            "complete_orders": complete_orders, "pending_orders": pending_orders,
            "sp": False

        })

    if request.method == "POST":
        booking = Booking.objects.get(id=bid)
        comment = request.POST['comment']
        rating = request.POST.get('rating')
        print(comment, rating)
        a = Comment(sp=booking.sp, comment=comment,
                    user=request.user, rate=rating)
        a.save()
        return render(request, 'login/comment.html', {
            "bid": bid,
            'message': 'Thanks for your feedback'
        })

    return render(request, 'login/comment.html', {
        "bid": bid
    })
