from django.shortcuts import render


def index(request):
    return render(request, 'dev/index.html', {})
def tables(request):
    table = [1,2,3,4,5]
    return render(request, 'dev/tables.html', {"tables":table})