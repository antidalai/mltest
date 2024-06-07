import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
import numpy as np
import os
from dateutil.parser import parse


def date_converter(date_string):
    return mdates.date2num(parse(date_string))


print("Current Directory: ", os.getcwd())

# This whole function is dedicated to displaying data
def graphRawFX():
    date,bid,ask = np.loadtxt('GBPUSD1d.txt', unpack = True, # need to add /mltest when on pc but not when on laptop
                              delimiter = ',', converters = {0: date_converter}) # This is using matplotlib.dates and stripping the string into proper date format
    fig = plt.figure(figure=(10,7)) # Essentially creates a blank canvas for drawing our plots
    ax1 = plt.subplot2grid((40, 40), (0, 0), rowspan=40, colspan=40) # Creates a sublot with certain specifications
    
    ax1.plot(date, bid) # 
    ax1.plot(date, ask)
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))

    plt.grid(True)
    plt.show()

graphRawFX()