import utils as u

DATE_START = 'dateStart'
DATE_END = 'dateEnd'
DAYS = 'days'
UP_DAYS = 'upDays'
DOWN_DAYS = 'downDays'


def main():
    u.log('Start Market Trend Backtest')

    analyze_50_10_trend()

    u.log('Start Market Trend Backtest')


def analyze_50_10_trend():
    u.log('Starting 50sma - 10ema trend analysis')
    priceFile = u.openFile('SPY_DAILY_PRICES.json')
    sma50File = u.openFile('SPY_SMA_50.json')
    ema10File = u.openFile('SPY_EMA_10.json')

    priceData = u.getJson(priceFile)
    sma50Data = u.getJson(sma50File)
    ema10Data = u.getJson(ema10File)

    u.closeFile(priceFile)
    u.closeFile(sma50File)
    u.closeFile(ema10File)

    priceArray = u.getPriceArray(priceData)
    sma50Array = u.getSMAArray(sma50Data)
    ema10Array = u.getEMAArray(ema10Data)

    u.log(len(sma50Array))
    u.log(len(ema10Array))
    u.log(len(priceArray))

    ema10Array = u.matchArrayLength(sma50Array, ema10Array)
    priceArray = u.matchArrayLength(sma50Array, priceArray)
    
    u.log(len(sma50Array))
    u.log(len(ema10Array))
    u.log(len(priceArray))

    marketLength = len(priceArray)

    dayCount = 0
    trendCount = 0
    resultsArray = [['trend 1', { DATE_START:'', DATE_END:'', DAYS:0, UP_DAYS:0, DOWN_DAYS:0 }]]

    for i in range(marketLength):
        closingPrice = priceArray[i][1][u.CLOSE]
        vDate = priceArray[i][0]
        emaPrice = ema10Array[i][1]
        smaPrice = sma50Array[i][1]
        above_50day = closingPrice > smaPrice
        above_10day = closingPrice > emaPrice
        _10day_above_50day = emaPrice > smaPrice

        if dayCount == 0: # find start of trend
            if above_50day:
                u.log('Trend Starts')
                resultsArray[-1][0][DAYS] += 1
                resultsArray[-1][0][DATE_START] = vDate


        
        if (closingPrice > emaPrice) and (closingPrice > smaPrice):
            
        
        break






    u.log('Finished 50sma - 10ema trend analysis')







main()
