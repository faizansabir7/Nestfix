from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("spregister", views.spregister, name="spregister"),
    path("services", views.services, name="services"),
    path("service/<str:id>", views.service, name="service"),
    # path("splist", views.splist, name="splist"),
    path("orders", views.orders, name="orders"),
    path("getsp/<str:username>", views.getsp, name="getsp"),
    path('comment/<int:bid>', views.comment, name='comment')

    

]





