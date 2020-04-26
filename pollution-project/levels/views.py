from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import pollution_index
from .graph import plot, regression
from django.db.models import Max
import datetime

def gen_graph(request):
    cities = ['Delhi','Bangalore','Mumbai','Las-Vegas','New-York']
    delhi  = pollution_index.objects.filter(city = cities[0]).order_by('date')
    graph = plot(request,delhi)
    delhi  = delhi.all().aggregate(Max('date'))

    fields = []
    dates = []
    for i in range(2,20):
        date = delhi['date__max']+ datetime.timedelta(days=i)
        fields.append([regression(pollution_index.objects.filter(city = cities[0]),str(date) ),date])


    args = {
             'plot':graph,
             'fields':fields,
    }
    return render(request,'index.html',args)
