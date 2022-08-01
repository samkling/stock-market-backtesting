import utils as u


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

    print(len(sma50Array))
    print(len(ema10Array))
    print(len(priceArray))

    ema10Array = u.matchArrayLength(sma50Array, ema10Array)
    priceArray = u.matchArrayLength(sma50Array, priceArray)
    
    print(len(sma50Array))
    print(len(ema10Array))
    print(len(priceArray))

    u.log('Finished 50sma - 10ema trend analysis')







main()
