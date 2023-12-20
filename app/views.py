

from django.shortcuts import render, get_object_or_404
from .models import Country, State, City

def country_list(request):
    countries = Country.objects.all()
    return render(request, 'country_list.html', {'countries': countries})

def country_detail(request, country_id):
    country = get_object_or_404(Country, pk=country_id)
    return render(request, 'country_detail.html', {'country': country})

def state_list(request, country_id):
    states = State.objects.filter(country_id=country_id)
    return render(request, 'state_list.html', {'states': states})

def state_detail(request, state_id):
    state = get_object_or_404(State, pk=state_id)
    return render(request, 'state_detail.html', {'state': state})

def city_list(request, state_id):
    cities = City.objects.filter(state_id=state_id)
    return render(request, 'city_list.html', {'cities': cities})

def city_detail(request, city_id):
    city = get_object_or_404(City, pk=city_id)
    return render(request, 'city_detail.html', {'city': city})
