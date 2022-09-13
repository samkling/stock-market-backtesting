import utils as u

def main():
    u.log('Start HV Study')

    hvStudy('CELH')

    u.log('End HV Study')

def hvStudy(ticker):
    priceFile = u.openFile('HV_STOCK_DATA/'+ticker.upper()+'_DAILY_PRICES.json')
    priceData = u.getJson(priceFile)
    u.closeFile(priceFile)
    priceArray = u.getPriceArray(priceData)



    for price in priceArray:
        print(price)



main()