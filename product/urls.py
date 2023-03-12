from django.urls import path
from . import views
print(11)
urlpatterns = [
    path('',views.login,name="login"),
    path('register/',views.register,name="register"),
    path('home/',views.home,name="home"),
    path('logout/',views.logout,name="logout"),
    path('create_profile/',views.create_profile,name="create_profile"),

]