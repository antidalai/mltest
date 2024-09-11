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


patStartTime = time.time()

def percentChange(startPoint, currentPoint):
    try:
        x = ((currentPoint - startPoint) / abs(startPoint)) * 100 #   Calculate the percent change between the start and current
        if x == 0.0:
            return 0.0000000001
        else:
            return x
    except:
        return 0.00000001
# This function creates kind of an average change between 10 points
# Also sets a future range of 10 points
# Creates and stores patterns in percent change between 10 points
# Also adds in how well the patterns do inside of the performance array by looking 10 steps ahead. 
def patternStorage():

    x = len(avgLine) - 60
    y = 31

    while y < x:
        pattern = []
        p1 = percentChange(avgLine[y-30], avgLine[y-29])
        p2 = percentChange(avgLine[y-30], avgLine[y-28])
        p3 = percentChange(avgLine[y-30], avgLine[y-27])
        p4 = percentChange(avgLine[y-30], avgLine[y-26])
        p5 = percentChange(avgLine[y-30], avgLine[y-25])
        p6 = percentChange(avgLine[y-30], avgLine[y-24])
        p7 = percentChange(avgLine[y-30], avgLine[y-23])
        p8 = percentChange(avgLine[y-30], avgLine[y-22])
        p9 = percentChange(avgLine[y-30], avgLine[y-21])
        p10 = percentChange(avgLine[y-30], avgLine[y-20])

        p11 = percentChange(avgLine[y-30], avgLine[y-19])
        p12 = percentChange(avgLine[y-30], avgLine[y-18])
        p13 = percentChange(avgLine[y-30], avgLine[y-17])
        p14 = percentChange(avgLine[y-30], avgLine[y-16])
        p15 = percentChange(avgLine[y-30], avgLine[y-15])
        p16 = percentChange(avgLine[y-30], avgLine[y-14])
        p17 = percentChange(avgLine[y-30], avgLine[y-13])
        p18 = percentChange(avgLine[y-30], avgLine[y-12])
        p19 = percentChange(avgLine[y-30], avgLine[y-11])
        p20 = percentChange(avgLine[y-30], avgLine[y-10])

        p21 = percentChange(avgLine[y-30], avgLine[y-9])
        p22 = percentChange(avgLine[y-30], avgLine[y-8])
        p23 = percentChange(avgLine[y-30], avgLine[y-7])
        p24 = percentChange(avgLine[y-30], avgLine[y-6])
        p25 = percentChange(avgLine[y-30], avgLine[y-5])
        p26 = percentChange(avgLine[y-30], avgLine[y-4])
        p27 = percentChange(avgLine[y-30], avgLine[y-3])
        p28 = percentChange(avgLine[y-30], avgLine[y-2])
        p29 = percentChange(avgLine[y-30], avgLine[y-1])
        p30 = percentChange(avgLine[y-30], avgLine[y])

        outcomeRange = avgLine[y+20:y+30]
        currentPoint = avgLine[y]
        try:
            avgOutcome = sum(outcomeRange) / len(outcomeRange)
        except Exception as e:
            print(str(e))
            avgOutcome = 0

        futureOutcome = percentChange(currentPoint, avgOutcome)
        pointsArr =[p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23, p24, p25, p26, p27, p28, p29, p30]
        pattern.extend(pointsArr)
        patternArr.append(pattern)
        performanceArr.append(futureOutcome)

        y += 1
    
    patEndTime = time.time()
    print(len(patternArr))
    print(len(performanceArr))
    print("Pattern storage took", patEndTime-patStartTime, ' seconds')

def currentPattern():
    currentPat1 = percentChange(avgLine[-31], avgLine[-30])
    currentPat2 = percentChange(avgLine[-31], avgLine[-29])
    currentPat3 = percentChange(avgLine[-31], avgLine[-28])
    currentPat4 = percentChange(avgLine[-31], avgLine[-27])
    currentPat5 = percentChange(avgLine[-31], avgLine[-26])
    currentPat6 = percentChange(avgLine[-31], avgLine[-25])
    currentPat7 = percentChange(avgLine[-31], avgLine[-24])
    currentPat8 = percentChange(avgLine[-31], avgLine[-23])
    currentPat9 = percentChange(avgLine[-31], avgLine[-22])
    currentPat10 = percentChange(avgLine[-31], avgLine[-21])

    currentPat11 = percentChange(avgLine[-31], avgLine[-20])
    currentPat12 = percentChange(avgLine[-31], avgLine[-19])
    currentPat13 = percentChange(avgLine[-31], avgLine[-18])
    currentPat14 = percentChange(avgLine[-31], avgLine[-17])
    currentPat15 = percentChange(avgLine[-31], avgLine[-16])
    currentPat16 = percentChange(avgLine[-31], avgLine[-15])
    currentPat17 = percentChange(avgLine[-31], avgLine[-14])
    currentPat18 = percentChange(avgLine[-31], avgLine[-13])
    currentPat19 = percentChange(avgLine[-31], avgLine[-12])
    currentPat20 = percentChange(avgLine[-31], avgLine[-11])

    currentPat21 = percentChange(avgLine[-31], avgLine[-10])
    currentPat22 = percentChange(avgLine[-31], avgLine[-9])
    currentPat23 = percentChange(avgLine[-31], avgLine[-8])
    currentPat24 = percentChange(avgLine[-31], avgLine[-7])
    currentPat25 = percentChange(avgLine[-31], avgLine[-6])
    currentPat26 = percentChange(avgLine[-31], avgLine[-5])
    currentPat27 = percentChange(avgLine[-31], avgLine[-4])
    currentPat28 = percentChange(avgLine[-31], avgLine[-3])
    currentPat29 = percentChange(avgLine[-31], avgLine[-2])
    currentPat30 = percentChange(avgLine[-31], avgLine[-1])
    
    listCurrentPats = [currentPat1, currentPat2, currentPat3, currentPat4, currentPat5, currentPat6, currentPat7, currentPat8, currentPat9, currentPat10, currentPat11, currentPat12, currentPat13, currentPat14, currentPat15, currentPat16, currentPat17, currentPat18, currentPat19, currentPat20, currentPat21, currentPat22, currentPat23, currentPat24, currentPat25, currentPat26, currentPat27, currentPat28, currentPat29, currentPat30]
    patForRecog.extend(listCurrentPats)

    print(patForRecog)

def patternRecognition():

    patFound = 0
    pltPatArr = []

    for everyPattern in patternArr:
        sim1 = 100.0 - abs(percentChange(everyPattern[0], patForRecog[0])) # Finds how similar the pattern for recognition is in compared to our list of patterns
        sim2 = 100.0 - abs(percentChange(everyPattern[1], patForRecog[1]))
        sim3 = 100.0 - abs(percentChange(everyPattern[2], patForRecog[2]))
        sim4 = 100.0 - abs(percentChange(everyPattern[3], patForRecog[3]))
        sim5 = 100.0 - abs(percentChange(everyPattern[4], patForRecog[4]))
        sim6 = 100.0 - abs(percentChange(everyPattern[5], patForRecog[5]))
        sim7 = 100.0 - abs(percentChange(everyPattern[6], patForRecog[6]))
        sim8 = 100.0 - abs(percentChange(everyPattern[7], patForRecog[7]))
        sim9 = 100.0 - abs(percentChange(everyPattern[8], patForRecog[8]))
        sim10 = 100.0 - abs(percentChange(everyPattern[9], patForRecog[9]))

        sim11 = 100.0 - abs(percentChange(everyPattern[10], patForRecog[10]))
        sim12 = 100.0 - abs(percentChange(everyPattern[11], patForRecog[11]))
        sim13 = 100.0 - abs(percentChange(everyPattern[12], patForRecog[12]))
        sim14 = 100.0 - abs(percentChange(everyPattern[13], patForRecog[13]))
        sim15 = 100.0 - abs(percentChange(everyPattern[14], patForRecog[14]))
        sim16 = 100.0 - abs(percentChange(everyPattern[15], patForRecog[15]))
        sim17 = 100.0 - abs(percentChange(everyPattern[16], patForRecog[16]))
        sim18 = 100.0 - abs(percentChange(everyPattern[17], patForRecog[17]))
        sim19 = 100.0 - abs(percentChange(everyPattern[18], patForRecog[18]))
        sim20 = 100.0 - abs(percentChange(everyPattern[19], patForRecog[19]))

        sim21 = 100.0 - abs(percentChange(everyPattern[20], patForRecog[20]))
        sim22 = 100.0 - abs(percentChange(everyPattern[21], patForRecog[21]))
        sim23 = 100.0 - abs(percentChange(everyPattern[22], patForRecog[22]))
        sim24 = 100.0 - abs(percentChange(everyPattern[23], patForRecog[23]))
        sim25 = 100.0 - abs(percentChange(everyPattern[24], patForRecog[24]))
        sim26 = 100.0 - abs(percentChange(everyPattern[25], patForRecog[25]))
        sim27 = 100.0 - abs(percentChange(everyPattern[26], patForRecog[26]))
        sim28 = 100.0 - abs(percentChange(everyPattern[27], patForRecog[27]))
        sim29 = 100.0 - abs(percentChange(everyPattern[28], patForRecog[28]))
        sim30 = 100.0 - abs(percentChange(everyPattern[29], patForRecog[29]))

        simLevel = (sim1+sim2+sim3+sim4+sim5+sim6+sim7+sim8+sim9+sim10+
                    sim11+sim12+sim13+sim14+sim15+sim16+sim17+sim18+sim19+sim20+
                    sim21+sim22+sim23+sim24+sim25+sim26+sim27+sim28+sim29+sim30)/30.0 # finds the average of all the similarity levels

        if simLevel > 75:
            patdex = patternArr.index(everyPattern)
            xp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,28, 29, 30]
            patFound = 1                # check for bool later
            pltPatArr.append(everyPattern)
            
    if patFound == 1:    
        fig = plt.figure(figsize=(10, 6))

        for eachPatt in pltPatArr:
            futurePoints = patternArr.index(eachPatt)
            plt.plot(xp, eachPatt) 

        plt.plot(xp, patForRecog, '#54fff7', linewidth=3)
        plt.grid(True)
        plt.title('Pattern Recognition') 
        plt.show()
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




dataLength = int(bid.shape[0]) # is how you get the size of a numpy array
print("data length is ", dataLength)
toPoint = 37000

while toPoint < dataLength:
    # defining global variables
    avgLine = (bid+ask)/2   # Finds the middle spot between bid and ask price
    avgLine = avgLine[:toPoint] # only consider the data we want to be considered
    patternArr = [] # As we run pattern finder we will store the patterns in this array
    performanceArr = [] # Stores future performance of our patterns being stored in the above array
    patForRecog = [] # pattern for recognition / current pattern type of thing


    # Calling functions
    patternStorage() 
    currentPattern()
    patternRecognition()
    totalTime = time.time() - patStartTime 
    print("Entire process took: ", totalTime)
    moveOn = input('press ENTER to continue...')
    toPoint += 1
