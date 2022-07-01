from django.urls import path
from register.views import register

urlpatterns = [
    path("", register.home, name="home"),
    path("hello/<name>", register.hello_there, name="hello_there"),
    path("register_self/<int:evento>", register.register_self, name="register_self"),
    path("register_self_done/<int:evento>", register.register_self_done, name="register_self_done"),
]
