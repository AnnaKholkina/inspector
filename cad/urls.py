from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main_cad, name='main_cad'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('add_unit', views.add_unit, name='add_unit'),
    #path('change_status_10_6', views.change_status_10_6, name='change_status_10_6'),

    path('change_status/<str:username>/<str:status>', views.change_status, name='change_status'),
    path('add_member_to_unit/<str:username>/<str:unit>', views.add_member_to_unit, name='add_member_to_unit'),
    path('delete_member_from_unit/<str:username>/<str:unit>', views.delete_member_from_unit, name='delete_member_from_unit')
]