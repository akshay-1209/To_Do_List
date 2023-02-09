from . import views
from django.urls import path

urlpatterns = [
    path("",views.index,name="index"),
    path("login",views.login_view,name="login"),
    path("register",views.register_view,name="register"),
    path("home",views.home_view,name="home"),
    path("home/add",views.add_view,name="add"),
    path("home/remove",views.remove_view,name="remove"),
    path("logout",views.logout_view,name="logout"),
]