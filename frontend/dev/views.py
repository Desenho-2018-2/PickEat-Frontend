from django.shortcuts import render


def index(request):
    orders = [{'table': 2, 'id': 321, 'status': 'done'}, {'table': 3, 'id': 322, 'status': 'cook'}]
    return render(request, 'dev/index.html', {'orders': orders})

def tables(request):
    table = [1,2,3,4,5,6,7,8,9]
    return render(request, 'dev/tables.html', {"tables":table})

def menu(request):
    foods = [{"id":1,"name":"Banana", "value":0},{"id":2, "name":"Maçã", "value":0},{"id":3, "name":"Uva passa", "value":0},{"id":4, "name":"Molho de manga", "value":0},{"id":5, "name":"Chiclete de goiaba", "value":0},{"id":6, "name":"Casca de kiwi", "value":0},{"id":7, "name":"Coco com ovo", "value":0}]
    return render(request, 'dev/menu.html', {"foods":foods})