import pandas as pd
from matplotlib import pyplot as plt
import plotly.graph_objects as go
import plotly.io as pio
from django.contrib.staticfiles.storage import staticfiles_storage
from django.http import HttpResponse
from django.core.files import File

from datetime import datetime

import numpy as np
import pandas as pd

def plot(request,data):
    # df = pd.read_csv(staticfiles_storage.path('DataSets/USA/reseda,-los angeles-air-quality.csv'))

    d = {"date": [],
         "pm25": [],
         "pm10": [],
         "o3": [],
         "no2": [],
         "so2": [],
         "co": []}

    # for i in df:
    #     for j in df.get(i):
    #         d[i].append(j if j != " " else 0)
    for i in data:
        d['date'] += [str(i.date)]
        d['pm25'] += [i.pm25]
        d['pm10'] += [i.pm10]
        d['o3']   += [i.o3]
        d['no2']  += [i.no2]
        d['so2']  += [i.so2]
        d['co']   += [i.co]



    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=d["date"][:100][::-1],
        y=d["o3"][:100][::-1],
        name='<b>O3</b>',  # Style name/legend entry with html tags
        connectgaps=True  # override default to connect the gaps
    ))
    fig.add_trace(go.Scatter(
        x=d["date"][:100][::-1],
        y=d["pm25"][:100][::-1],
        name='pm25',
        connectgaps=True
    ))
    fig.add_trace(go.Scatter(
        x=d["date"][:100][::-1],
        y=d["pm10"][:100][::-1],
        name='pm10',
    ))
    fig.add_trace(go.Scatter(
        x=d["date"][:100][::-1],
        y=d["no2"][:100][::-1],
        name='NO2',
        connectgaps=True
    ))
    fig.add_trace(go.Scatter(
        x=d["date"][:100][::-1],
        y=d["so2"][:100][::-1],
        name='SO2',
        connectgaps=True
    ))

    fig.add_trace(go.Scatter(
        x=d["date"][:100][::-1],
        y=d["co"][:100][::-1],
        name='CO',
        connectgaps=True
    ))

    return pio.to_html(fig,full_html=False)

def regression(data, test_dat):
    """
    :param test_dat: Url of excel sheet / database source
    :param data: date to get prediction # year/month/date format
    :return: pollution level (pm25,pm10,O3,NO2,SO2,CO)
    """

    d = {"date": [],
         "pm25": [],
         "pm10": [],
         "o3": [],
         "no2": [],
         "so2": [],
         "co": []}

    # for i in df:
    #     for j in df.get(i):
    #         d[i].append(j if j != " " else 0)
    for i in data:
        d['date'] += [str(i.date)]
        d['pm25'] += [i.pm25]
        d['pm10'] += [i.pm10]
        d['o3']   += [i.o3]
        d['no2']  += [i.no2]
        d['so2']  += [i.so2]
        d['co']   += [i.co]
    
    # -------------------------------Web_Page aka Graph-----------
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=d["date"][:100][::-1],
        y=d["o3"][:100][::-1],
        name='<b>O3</b>',  # Style name/legend entry with html tags
        connectgaps=True  # override default to connect the gaps
    ))
    fig.add_trace(go.Scatter(
        x=d["date"][:100][::-1],
        y=d["pm25"][:100][::-1],
        name='pm25',
    ))
    fig.add_trace(go.Scatter(
        x=d["date"][:100][::-1],
        y=d["pm10"][:100][::-1],
        name='pm10',
    ))
    fig.add_trace(go.Scatter(
        x=d["date"][:100][::-1],
        y=d["no2"][:100][::-1],
        name='NO2',
    ))
    fig.add_trace(go.Scatter(
        x=d["date"][:100][::-1],
        y=d["so2"][:100][::-1],
        name='SO2',
    ))

    fig.add_trace(go.Scatter(
        x=d["date"][:100][::-1],
        y=d["co"][:100][::-1],
        name='CO',
    ))
    # ---------------------------ML-----------------------------
    x = np.array(d["date"][:100][::-1])

    xt = []
    for i in range(len(x)):
        temp = str(x[i]).split("-")
        if len(temp[1]) == 1:
            temp[1] = "0" + temp[1]
        if len(temp[2]) == 1:
            temp[2] = "0" + temp[2]
        xt.append(datetime.fromisoformat('-'.join(temp)).timestamp())

    x = np.array(list(map(int, xt)))
    pm25 = np.array(list(map(int, d["pm25"][:100]))[::-1])
    pm10 = np.array(list(map(int, d["pm25"][:100]))[::-1])
    O3 = np.array(list(map(int, d["o3"][:100]))[::-1])
    NO2 = np.array(list(map(int, d["no2"][:100]))[::-1])
    SO2 = np.array(list(map(int, d["so2"][:100]))[::-1])
    CO = np.array(list(map(int, d["co"][:100]))[::-1])

    ppm25 = np.poly1d(np.polyfit(x, pm25, 3))  # p: polynomial equation 3rd param : degree of the polynomial
    ppm10 = np.poly1d(np.polyfit(x, pm10, 3))
    po3 = np.poly1d(np.polyfit(x, O3, 3))
    pno2 = np.poly1d(np.polyfit(x, NO2, 3))
    pso2 = np.poly1d(np.polyfit(x, SO2, 3))
    pco = np.poly1d(np.polyfit(x, CO, 3))

    # print(p) # Polynomial equation

    # temp = "2020/4/2".split("/")
    # if len(temp[1]) == 1:
    #     temp[1] = "0" + temp[1]
    # if len(temp[2]) == 1:
    #     temp[2] = "0" + temp[2]
    s = datetime.fromisoformat(test_dat).timestamp()

    return ppm25(s), ppm10(s), po3(s), pno2(s), pso2(s), pco(s)
