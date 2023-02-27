from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main_cad, name='main_cad'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('add_unit', views.add_unit, name='add_unit'),
    #path('change_status_10_6', views.change_status_10_6, name='change_status_10_6'),

    path(r'^change_status/(?P<username>\d+)/(?P<status>\d+)$', views.change_status, name='change_status'),
    path('add_member', views.add_member, name='add_member')
]