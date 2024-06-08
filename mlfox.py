import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
import numpy as np
import os
from dateutil.parser import parse



def date_converter(date_string):
    return mdates.date2num(parse(date_string))

date,bid,ask = np.loadtxt('GBPUSD1d.txt', unpack = True,  # need to add /mltest when on pc but not when on laptop
                              delimiter = ',', converters = {0: date_converter}) # This is using matplotlib.dates and stripping the string into proper date format


def percentChange(startPoint, currentPoint):
    return ((currentPoint - startPoint) / startPoint) * 100 #   Calculate the percent change between the start and current


print("This is the bid: ", bid)

# This whole function is dedicated to displaying data
def graphRawFX():
    fig = plt.figure(figure=(10,7))  # Essentially creates a blank canvas for drawing our plots
    ax1 = plt.subplot2grid((40, 40), (0, 0), rowspan=40, colspan=40) # Creates a sublot with certain specifications
    
    ax1.plot(date, bid)  # plots the different bid prices points against the date
    ax1.plot(date, ask)  # does the same but for ask prices
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S')) # Sets the format for the xaxis

    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)   #Tilts the label on the xaxis to increase readability
    
    plt.gca().get_yaxis().get_major_formatter().set_useOffset(False)    # makes it so that the y axis displays in full without any offset



    plt.grid(True)
    plt.show()

graphRawFX()