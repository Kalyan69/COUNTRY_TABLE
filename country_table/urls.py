
from django.urls import path
from app import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('countries/', views.country_list, name='country_list'),
    path('countries/<int:country_id>/', views.country_detail, name='country_detail'),
    path('countries/<int:country_id>/states/', views.state_list, name='state_list'),
    path('states/<int:state_id>/', views.state_detail, name='state_detail'),
    path('states/<int:state_id>/cities/', views.city_list, name='city_list'),
    path('cities/<int:city_id>/', views.city_detail, name='city_detail'),
]
