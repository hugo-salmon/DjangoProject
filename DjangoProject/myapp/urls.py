from django.urls import path
from . import views

urlpatterns = [
    path('inscription/', views.register_user, name='inscription'),
        path('confirmation/', views.confirmation, name='confirmation'), 

]