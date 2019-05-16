from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    if request.method == 'POST':
        name_1 = request.POST.get('name_1')
        l_1 = len(name_1)
        name_2 = request.POST.get('name_2')
        l_2 = len(name_2)
        name_3 = request.POST.get('name_3')
        l_3 = len(name_3)
        if l_1 > l_2 and l_1 > l_3:
            result = name_1
        elif l_2 > l_1 and l_2 > l_3:
            result = name_2
        else:
            result = name_3
        return HttpResponse(result)
    return HttpResponse('It is GET request')


def index2(request):
    if request.method == 'POST':
        d = request.POST.get('date')
        year1, month1, day1 = map(int, d.split('-'))
        if day1 == 1 and month1 == 1:
            return HttpResponse(f'С новым {year1} годом')
        return HttpResponse(d)
    return HttpResponse('It is GET request')
