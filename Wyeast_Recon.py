import matplotlib.pyplot as plt
import numpy as np
import gpxpy
from sympy import fft
#from pandasgui import show
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
delta_slope= np.diff(df.loc[:,'Slope'])/np.diff(5280*df.loc[:,'Distance'])
delta_slope = np.insert(delta_slope,0,0)
df['Delta_Slope']=delta_slope
print(df)

"""
plt.scatter(df.loc[:,'Distance'],df.loc[:,'Slope'],s=10)
plt.xlabel("100K Distance (Miles)",fontsize=24)
plt.ylabel("Slope Angle (ft/ft)",fontsize=24)
plt.title("Wy'east Howl Slope Angle vs. Distance",fontsize=30)
# plt.scatter(df.loc[:,'Distance'],df.loc[:,'Altitude'])
#plt.show()

plt.scatter(df.loc[:,'Distance'],df.loc[:,'Delta_Slope'],s=5)
plt.xlabel("100K Distance (Miles)",fontsize=24)
plt.ylabel("Delta_Slope",fontsize=24)
plt.title("Wy'east Howl Delta Slope Angle vs. Distance",fontsize=30)
ylim=([-.25,.25])
#plt.show()


b1_bin=[-1,-.75,-.5,-.25,0,.25,.5,.75,1]
plt.hist(df.loc[:,'Slope'],bins=50,range=[-.5,.5])
plt.title("Slope Angle Frequency by # of Data Points",fontsize=30)
plt.xlabel("Slope Bins",fontsize=24)
plt.ylabel("Frequency (# Data Points)",fontsize=24)
#plt.show()
"""

k = df[df.loc[:,'Slope']>.25]

"""
Write conversion from lat and lon to nautical miles and then to regular
lat = 69 miles per 1 degrees
lon = 69.172 miles per 1 degrees
"""

df['Tared_Lat']= df.loc[:,'Latitude']-df.loc[0,'Latitude']
df['Tared_Long']= df.loc[:,'Longitude']-df.loc[0,'Longitude']
df['Scaled_Lat']= 69*df.loc[:,'Tared_Lat']
df['Scaled_Long']=69.172*df.loc[:,'Tared_Long']

plt.scatter(df.loc[:,"Scaled_Lat"],df.loc[:,"Scaled_Long"])
plt.grid()
plt.show()
print(df)

"""
write a method to calculate turns and aggresiveness in XY
"""


"""
generate a table to hold all aid station data
"""

aid_table = DataFrame()
aid_table['Aid Station'] =['Start - Mt. Hood Meadows','#1 - Elk Meadows', '#2 - Gunsight (limited/unstaffed aid in AM)', '#3 High Prairie', "#4 Surveyor's Ridge", 'High Prairie','Gunsight 2', 'Elk Meadows 2', 'Timberline', 'Finish - Mt. Hood Meadows']
aid_table['Total Distance (mi)']=[0,8.6,14.3,21.6,31.0,39.4,46.7,52.4,57.8,62.0]
aid_table['To Next Aid (mi)']= [8.6,5.7,7.3,9.4,8.4,7.3,5.7,5.4,4.2,0]
aid_table['Crew']=['Yes','Yes','No','No','Yes','No','No','Yes','No','Yes']
aid_table['Pacer']=['No','No','No','No','No','No','No','Yes','No','No']
aid_table['Drop Bag']=['No','Yes','No','No','Yes','No','No','Yes','No','Yes']
aid_table['Toilet']=['Yes','Yes','No','No','Yes','No','No','Yes','No','Yes']
aid_table['Cutoff']=['NA','NA','NA','NA','1:00 PM','4:00 PM','6:00 PM','8:00 PM','9:30 PM','11:00 PM']


"""
fft_slope = np.fft.fft(df.loc[:,'Slope'])
print(fft_slope.real)

plt.scatter(fft_slope)
plt.show()
"""
