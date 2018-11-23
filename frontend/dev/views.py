from django.shortcuts import render


def index(request):
    orders = [{'table': 2, 'id': 321, 'status': 'done'}, {'table': 3, 'id': 322, 'status': 'cook'}]
    return render(request, 'dev/index.html', {'orders': orders})

def tables(request):
    table = [{'number': 1,'status': 'aberta'},{'number':2,'status':'aberta'},{'number':3,'status':'fechada'},{'number':4,'status':'aberta'},{'number':1,'status':'fechada'}]
    return render(request, 'dev/tables.html', {"tables":table})

def order(request):
    return render(request, 'dev/order.html')

def menu(request):
    drink = [{'name':'Marguerita', 'id': 1, 'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit'},{'name':'Ice Vanilla', 'id': 2, 'description': 'Curabitur et elit accumsan, commodo neque in'},{'name':'Blue Caribbean', 'id': 3, 'description': 'Orci varius natoque penatibus et magnis'},{'name':'Corona', 'id': 4, 'description': 'Orci varius natoque penatibus et magnis'}]
    snack = [{'name':'Porção de Carne de Sol', 'id': 1, 'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit'},{'name':'Isca de Frango', 'id': 2, 'description': 'Curabitur et elit accumsan, commodo neque in'},{'name':'Batata Frita', 'id': 3, 'description': 'Orci varius natoque penatibus et magnis'}]
    beer = [{'name':'Skoll', 'id': 1, 'description': ''},{'name':'Heineken', 'id': 2, 'description': ''},{'name':'Kaiser', 'id': 3, 'description': ''}]
    return render(request, 'dev/menu.html', {"drinks":drink,"snacks":snack,"beers":beer})

    