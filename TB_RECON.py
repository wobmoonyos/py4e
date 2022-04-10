#https://ocefpaf.github.io/python4oceanographers/blog/2014/08/18/gpx/
"""
loc: only work on index
iloc: work on position
at: get scalar values. It's a very fast loc
iat: Get scalar values. It's a very fast iloc

"""
import matplotlib.pyplot as plt
import numpy as np
import gpxpy
from sympy import fft
gpx = gpxpy.parse(open('TB3AX.gpx'))


"""
print("{} track(s)".format(len(gpx.tracks)))
track = gpx.tracks[0]

print("{} segment(s)".format(len(track.segments)))
segment = track.segments[0]

print("{} point(s)".format(len(segment.points)))
"""

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

# how many "takes" are in the GPX array
num_points = df.shape[0]

# how far between each point are you stepping
dist_step = 100 / (num_points)

# Start = 0, Stop = 100, Step Size = dist_step
dist_df = DataFrame(np.arange(0, 100, dist_step))

df.insert(loc=5, column="Distance", value= dist_df)
print(df)
#

Y_ax = df.loc[:,"Altitude"]
X_ax = 5280*df.loc[:,"Distance"]

slope = np.diff(Y_ax)/np.diff(X_ax)
fftable_slope = slope
slope = DataFrame(slope)

print(slope)
# print(df.shape[0],slope.shape[0])

plt.plot(slope)
plt.show()

from sympy import fft

decimal_point = 2
transform = fft(fftable_slope, decimal_point)

print("this is a slope FFT")
plt.plot(transform)
plt.show()


#df.insert(loc=6, column="Slope", value=slope)
