import csv

from django.core.paginator import Paginator
from django.shortcuts import render
from pagination.settings import BUS_STATION_CSV


# Create your views here.
def pagi_view(request):
    stations_list = []
    page_number = int(request.GET.get("page", 1))
    with open(BUS_STATION_CSV, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            station = {
            'Name': row['Name'],
            'Street': row['Street'],
            'District': row['District']
            }
            stations_list.append(station)
    paginator = Paginator(stations_list, 10)
    page = paginator.get_page(page_number)
    context = {
        "page": page
    }
    return render(request, 'index.html', context)
