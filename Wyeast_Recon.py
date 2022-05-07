import matplotlib.pyplot as plt
import numpy as np
import gpxpy
from sympy import fft
gpx = gpxpy.parse(open('C:/Users/14253/Desktop/py4e/Wyeast.gpx'))


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


df['Distance'] = np.linspace(0,58.7,12913)


slope= np.diff(df.loc[:,'Altitude'])/np.diff(5280*df.loc[:,'Distance'])
slope = np.insert(slope,0,0)
df['Slope']=slope
print(df)
plt.scatter(df.loc[:,'Distance'],df.loc[:,'Slope'])
# plt.scatter(df.loc[:,'Distance'],df.loc[:,'Altitude'])
ylim=(0,1.5)
plt.show()
