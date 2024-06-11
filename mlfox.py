import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
import numpy as np
import os
import time
from dateutil.parser import parse



def date_converter(date_string):
    return mdates.date2num(parse(date_string))

date,bid,ask = np.loadtxt('GBPUSD1d.txt', unpack = True,  # need to add /mltest when on pc but not when on laptop
                              delimiter = ',', converters = {0: date_converter}) # This is using matplotlib.dates and stripping the string into proper date format

avgLine = (bid+ask)/2   # Finds the middle spot between bid and ask price
patternArr = [] # As we run pattern finder we will store the patterns in this array
performanceArr = [] 
patForRecog = [] # pattern for recognition / current pattern type of thing


def percentChange(startPoint, currentPoint):
    return ((currentPoint - startPoint) / abs(startPoint)) * 100 #   Calculate the percent change between the start and current


# This function creates kind of an average change between 10 points
# Also sets a future range of 10 points
# Creates and stores patterns in percent change between 10 points
def patternStorage():
    patStartTime = time.time()

    x = len(avgLine) - 30
    y = 11

    while y < x:
        pattern = []
        p1 = percentChange(avgLine[y-10], avgLine[y-9])
        p2 = percentChange(avgLine[y-10], avgLine[y-8])
        p3 = percentChange(avgLine[y-10], avgLine[y-7])
        p4 = percentChange(avgLine[y-10], avgLine[y-6])
        p5 = percentChange(avgLine[y-10], avgLine[y-5])
        p6 = percentChange(avgLine[y-10], avgLine[y-4])
        p7 = percentChange(avgLine[y-10], avgLine[y-3])
        p8 = percentChange(avgLine[y-10], avgLine[y-2])
        p9 = percentChange(avgLine[y-10], avgLine[y-1])
        p10 = percentChange(avgLine[y-10], avgLine[y])

        outcomeRange = avgLine[y+20:y+30]
        currentPoint = avgLine[y]
        try:
            avgOutcome = sum(outcomeRange) / len(outcomeRange)
        except Exception as e:
            print(str(e))
            avgOutcome = 0

        futureOutcome = percentChange(currentPoint, avgOutcome)
        pointsArr =[p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]
        pattern.extend(pointsArr)
        patternArr.append(pattern)
        performanceArr.append(futureOutcome)

        y += 1
    
    patEndTime = time.time()
    print(len(patternArr))
    print(len(performanceArr))
    print("Pattern storage took", patEndTime-patStartTime, ' seconds')

def currentPattern():
    currentPat1 = percentChange(avgLine[-11], avgLine[-10])
    currentPat2 = percentChange(avgLine[-11], avgLine[-9])
    currentPat3 = percentChange(avgLine[-11], avgLine[-8])
    currentPat4 = percentChange(avgLine[-11], avgLine[-7])
    currentPat5 = percentChange(avgLine[-11], avgLine[-6])
    currentPat6 = percentChange(avgLine[-11], avgLine[-5])
    currentPat7 = percentChange(avgLine[-11], avgLine[-4])
    currentPat8 = percentChange(avgLine[-11], avgLine[-3])
    currentPat9 = percentChange(avgLine[-11], avgLine[-2])
    currentPat10 = percentChange(avgLine[-11], avgLine[-1])

    listCurrentPats = [currentPat1, currentPat2, currentPat3, currentPat4, currentPat5, currentPat6, currentPat7, currentPat8, currentPat9, currentPat10]
    patForRecog.extend(listCurrentPats)

    print(patForRecog)



def patternRecognition():
    for myPattern in patternArr:
        sim1 = percentChange(myPattern[0], patForRecog[0])


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

#graphRawFX()
patternStorage()
currentPattern()