import csv
import matplotlib.pyplot as plt
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

miejsca = {'m1': [100, -116.79, 33.48], 'm2': [500, -148.79, -13.45]}

lons = [55.79, 78.79]
lats = [56, 55.45]
wal = [56, 55.45]

data = [Scattergeo(customdata=wal,lon=lons, lat=lats)]
moj_layout = Layout(title='Pieniądze wydane')
fig = {'data': data, 'layout': moj_layout}
offline.plot(fig)
