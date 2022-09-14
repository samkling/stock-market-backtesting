import utils as u
import datetime

def main():
    u.log('Start HV Study')
    tickers = ['aapl', 'adbe','aehr','amd','amgn','amzn','baba','box','celh','crm','crwd','dbx','elf','enph','etsy','fslr','googl','jd','lrcx','amat', 'mu', 'meta','msft','net','nio','nvda','run','rvlv','shop','snow','sq','team','tsla','u','udmy','wolf']
    
    for t in tickers:
        hvStudy(t)
    
    #hvStudy('CELH') #testing

    u.log('End HV Study')

def hvStudy(ticker):
    priceFile = u.openFile('HV_STOCK_DATA/'+ticker.upper()+'_DAILY_PRICES.json')
    priceData = u.getJson(priceFile)
    u.closeFile(priceFile)
    priceArray = u.getPriceArray(priceData)

    hvData = gatherHvDates(priceArray)

    u.saveHVDataToCSV(hvData, ticker)

def gatherHvDates(data):
    # highest volume ever           "HVE"
    hve = 0

    # highest volume 250 days       "HV1"
    hv1 = 0
    hv1Date = 0
    hv1Ary = []
    newHV1 = True

    # highest volume 90 day         "HVLE"
    hvle = 0
    hvleDate = 0
    hvleAry = []
    newHVLE = True

    # Highes Volume Data Array
    hvArray = [['date', 'volume','HV-X']]
    isRedDay = False

    for i in range(len(data)):
        day = data[i]
        prevDay = 0
        dayDate = u.createDate(day[0])
        dayDateStr = day[0]
        dayVolume = day[1]['volume']
        
        if hve != 0:
            prevDay = data[i-1]
            newHV1 = (dayDate-hv1Date).days >= 250
            newHVLE = (dayDate-hvleDate).days >= 90
            isRedDay = day[1]['close'] < prevDay[1]['close']
        
        if dayDateStr == '2010-11-11' and hve != 0:
            print(isRedDay)
            print(dayVolume)
            print(day[1]['close'])
            print(prevDay[1]['close'])

        if (dayVolume < 700000 or isRedDay) and hve > 0:
            pass
        elif dayVolume > hve:
            hve = dayVolume
            hv1 = dayVolume
            hvle = dayVolume
            hv1Date = dayDate
            hvleDate = dayDate
            hvArray.append([dayDateStr,dayVolume,'HVE'])
        elif (dayVolume >= hv1) or (newHV1 and (dayVolume > max(hv1Ary)) ):
            hv1 = dayVolume
            hvle = dayVolume
            hv1Date = dayDate
            hvleDate = dayDate
            hvArray.append([dayDateStr,dayVolume,'HV1'])
        elif (dayVolume >= hvle) or (newHVLE and (dayVolume > max(hvleAry)) ):
            hvle = dayVolume
            hvleDate = dayDate
            hvArray.append([dayDateStr,dayVolume,'HVLE'])
        
        # Rolling 250 days
        hv1Ary.append(dayVolume)
        if len(hv1Ary) > 250:
            hv1Ary.pop(0)
        # Rolling 90 days
        hvleAry.append(dayVolume)
        if len(hvleAry) > 90:
            hvleAry.pop(0)
    
    return hvArray


main()