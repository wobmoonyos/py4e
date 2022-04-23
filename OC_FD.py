#https://ocefpaf.github.io/python4oceanographers/blog/2014/08/18/gpx/
#https://www.gpsvisualizer.com/convert?from_profile=1&convert_format=gpx&units=us&local_input=20220410164153-09165
#https://www.usgs.gov/faqs/how-much-distance-does-degree-minute-and-second-cover-your-maps#:~:text=One%20degree%20of%20latitude%20equals,one%20second%20equals%2080%20feet.
import matplotlib.pyplot as plt
import numpy as np
import gpxpy
from sympy import fft
gpx = gpxpy.parse(open('C:/Users/14253/Desktop/py4e/OC100.gpx'))
import math


# store track data as track variable object
track = gpx.tracks[0]

# store segment data as segment object
segment = track.segments[0]

# formatting data as an array
data = []
segment_length = segment.length_3d()
for point_idx, point in enumerate(segment.points):
    data.append([point.longitude, point.latitude,
                 3.28084*point.elevation, point.time, segment.get_speed(point_idx)])

# converting array to dataframe and adding labels
from pandas import DataFrame

columns = ['Longitude', 'Latitude', 'Altitude', 'Time', 'Speed']
df = DataFrame(data, columns=columns)
df.head()
# df['Distance']= np.arange(0,74.55,74.55/85830)
df['Time']= np.arange(0,23.838,23.838/85830)
print(df)

# plt.scatter(df.loc[:,'Time'], df.loc[:,'Speed'])
df['CDiff']= abs(df.loc[:,'Altitude'].diff().cumsum())
# plt.scatter(df.loc[:,'Time'], df.loc[:,'CDiff'])


df['Longitude']=288200*df.loc[:,'Longitude']
df['Latitude']=364000*df.loc[:,'Latitude']

Sum_of_Squares = (df.loc[:,'Longitude']**2)+(df.loc[:,'Latitude']**2)
Sum_of_Squares.dtypes
RSS = (Sum_of_Squares**(1/2))
RSS_delta = abs(RSS.diff())
RSS_sum = RSS_delta.cumsum()/5280
RSS_sum = RSS_sum * 74.55/54.856989
print(RSS_sum)
print(RSS_sum.shape[0])
df['Distance']=RSS_sum

plt.scatter(df.loc[:,'Time'],df.loc[:,'Distance'])
plt.show()
#RSS = math.sqrt(Sum_of_Squares)
