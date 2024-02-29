from django.urls import path
from . import views

urlpatterns = [
    path('inscription/', views.register_user, name='inscription'),
    path('existing_user', views.existing_user, name='existing_user'),
    path('', views.login_user, name='connexion'),
    path('base', views.base, name="base"),
    path('logout/', views.logout_view, name='logout'),
    path('flight_search/', views.flight_search, name='flight_search'),
    path('accommodation_reservation/', views.accommodation_reservation, name='accommodation_reservation')
]