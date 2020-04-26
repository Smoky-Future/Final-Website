import csv
from django.contrib.staticfiles.storage import staticfiles_storage
from .models import pollution_index
from django.http import HttpResponse
from datetime import datetime

def fetch_data(request):
        count = 0
        with open(staticfiles_storage.path('DataSets/delhi_using.csv'), newline='') as File:
                    reader = csv.reader(File)
                    for row in reader:
                         if count != 0:
                              try:
                                      for x in row:
                                          if x == '' or x == ' ':
                                              x = 0


                                      pollution_index.objects.create( city = "Delhi",
                                                                      date = datetime.strptime(row[0], "%Y/%m/%d").date(),
                                                                      pm25 = int(row[1]),
                                                                      pm10 = int(row[2]),
                                                                      o3   = int(row[3]),
                                                                      no2  = int(row[4]),
                                                                      so2  = int(row[5]),
                                                                      co   = int(row[6]))
                              except:
                                   pass
                         count =  count + 1
                    # x = pollution_index.objects.filter(city = 'Mumbai')
                    # print(x)
        return HttpResponse('data succesfully added')
