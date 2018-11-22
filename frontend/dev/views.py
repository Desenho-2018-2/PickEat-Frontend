from django.shortcuts import render


def index(request):
    orders = [{'table': 2, 'id': 321, 'status': 'done'}, {'table': 3, 'id': 322, 'status': 'cook'}]
    return render(request, 'dev/index.html', {'orders': orders})

def tables(request):
    table = [1,2,3,4,5,6,7,8,9]
    return render(request, 'dev/tables.html', {"tables":table})