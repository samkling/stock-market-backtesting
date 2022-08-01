import os
import json
from datetime import datetime

#   DAILY PRICES CONSTANTS
TIME_SERIES_DAILY = 'Time Series (Daily)'
TIME_SERIES_OPEN = '1. open'
TIME_SERIES_HIGH = '2. high'
TIME_SERIES_LOW = '3. low'
TIME_SERIES_CLOSE = '4. close'
TIME_SERIES_VOLUME = '5. volume'

#   CONSTANTS
HIGH = 'high'
LOW = 'close'
CLOSE = 'low'
OPEN = 'open'

#   MOVING AVERAGE CONSTANTS
TA_SMA = 'Technical Analysis: SMA'
SMA = 'SMA'
TA_EMA = 'Technical Analysis: EMA'
EMA = 'EMA'

def log(message):
    print(message)

def getDir():
    return os.getcwd()

def openFile(filename):
    log('Opening File: ' + filename)
    return open(getDir() + '/data/' + filename, 'r')

def closeFile(file):
    log('Closed File: ' + file.name.split('/')[-1])
    file.close()

def getJson(file):
    return json.load(file)

def getPriceArray(data):
    # [[date, {open, high, low, close}]]
    ary = []

    for day in data[TIME_SERIES_DAILY]:
        # priceDate = datetime.strptime(day, '%Y-%m-%d').date()

        ary = [[day,{
            OPEN: data[TIME_SERIES_DAILY][day][TIME_SERIES_OPEN],
            HIGH: data[TIME_SERIES_DAILY][day][TIME_SERIES_HIGH],
            LOW: data[TIME_SERIES_DAILY][day][TIME_SERIES_LOW],
            CLOSE: data[TIME_SERIES_DAILY][day][TIME_SERIES_CLOSE]
        }]] + ary
    
    return ary

def getSMAArray(data):
    log('Get SMA Array')
    ary = []

    for day in data[TA_SMA]:
        ary = [[day, data[TA_SMA][day][SMA]]] + ary
    return ary

def getEMAArray(data):    
    log('Get EMA Array')
    ary = []

    for day in data[TA_EMA]:
        ary = [[day, data[TA_EMA][day][EMA]]] + ary
    return ary

def matchArrayLength(shortAry,longAry):
    firstDate = shortAry[0][0]
    for i in range(len(longAry)):
        if longAry[0][0] == firstDate:
            break
        else:
            longAry.pop(0)
    return longAry