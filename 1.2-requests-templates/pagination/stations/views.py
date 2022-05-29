from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import csv



def index(request):
    return redirect(reverse('bus_stations'))


def read_csv():
    information = []

    with open('./data-398-2018-08-30.csv', encoding='utf-8') as file:
        lists = csv.reader(file)
        for element in lists:
            if element[1] != 'Name' or element[4] != 'Street' or element[6] != 'District':
                information.append({
                    'Name': element[1],
                    'Street': element[4],
                    'District': element[6]
                })

    return information



def bus_stations(request):
    information = read_csv()

    paginator = Paginator(information, 10)
    current_page = request.GET.get('page', 1)
    page = paginator.get_page(current_page)

    context = {
        'bus_stations': page.object_list,
        'page': page,
    }

    return render(request, 'stations/index.html', context)











