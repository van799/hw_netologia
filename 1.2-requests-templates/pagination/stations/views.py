import csv

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    data_csv = settings.BUS_STATION_CSV
    with open(data_csv, encoding='Utf-8', newline='') as f:
        file_reader = csv.DictReader(f)
        content = list(file_reader)
        page_number = int(request.GET.get('page', 1))
        paginator = Paginator(content, 10)
        data_page = paginator.get_page(page_number)

        context = {
             'bus_stations': data_page,
             'page': data_page,
        }
    return render(request, 'stations/index.html', context)
