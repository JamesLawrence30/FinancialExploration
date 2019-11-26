import requests;
import csv;


alphaVantageKey = "0ZU6NM5CMUSMR7DO"

def makeRequest(symbol):
    #create api call string below. receive time series from api
    #datatype=csv is key here to receiving the data in a format that is useful for python
    csvURL = "https://www.alphavantage.co/query?function=MACD&symbol="+symbol+"&interval=1min&datatype=csv&series_type=open&apikey="+alphaVantageKey
    
    with requests.Session() as s:
        tSeriesDownload = s.get(csvURL); #make request and receive csv file

        decoded_content = tSeriesDownload.content.decode('utf-8'); #'decode' file to use as csv in python?
        
        tSeriesDecoded = csv.reader(decoded_content.splitlines(), delimiter=','); # turn csv into usable list in python?

        tSeriesWithHeader = list(tSeriesDecoded); #full csv file is now usable in python

        tSeries = tSeriesWithHeader[1:]; #remove first line off time series with name of each csv column

    return tSeries;


def populateMongo(timeSeries):
    """
    for row in timeSeries:
        print(row)
    """
    for row in timeSeries:
        if(float(row[3]) >= 0.05):
            print(row[3]);
    ####script to some mongoDB api to send data to noSQL db en masse for safe keeping / use later in an operation
    #### this will be a .insertMany() since many time series entreis added


def main():
    timeSeries = makeRequest("MSFT"); #structure api call by passing in a ticker symbol
    #evenrually pull hidden secret api key from another file that won't go on git.

    populateMongo(timeSeries); #populate mongodb with all time series data
    ####eventually want to manipulate realtie data and execute trades based on intraday market technicals


#Tell python to call main function first
if __name__ == "__main__":
    main()
