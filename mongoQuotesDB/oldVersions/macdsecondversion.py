import requests;
import csv;


alphaVantageKey = "0ZU6NM5CMUSMR7DO"

def makeRequest(symbol):
    #create api call string below. receive time series from api
#    request = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol="+symbol+"&outputsize=compact&datatype=json&apikey="+alphaVantageKey
    csvURL = "https://www.alphavantage.co/query?function=MACD&symbol="+symbol+"&interval=1min&datatype=csv&series_type=open&apikey="+alphaVantageKey
    
    with requests.Session() as s:
        tSeriesDownload = s.get(csvURL); #make request and receive csv file

        decoded_content = tSeriesDownload.content.decode('utf-8'); #'decode' file to use as csv in python?
        
        tSeriesDecoded = csv.reader(decoded_content.splitlines(), delimiter=','); # turn csv into usable list in python?

        tSeriesWithHeader = list(tSeriesDecoded); #full csv file is now usable in python

        tSeries = tSeriesWithHeader[1:]; #remove first line off time series with name of each csv column

    return tSeries;


def populateMongo(timeSeries):
    for row in timeSeries:
#        if(float(row[3]) >= 0.05):
            print(row[3]);

    ####POSSIBLY A RECURSIVE FUNCTION TO GO FROM timeseries.find("{") to timeseries.find("}")
    ######then call function recursively starting at position of timeseries.find("}") to begin looking for exact start of next entry
    #######each entry is send to an .insertOne()

    #this needs to connect to mongodb
    #for every day in response body, add the data to collection timeSeries
    #wil then be able to filter for the close prices from each day's data
    ###each day is a "file"?? in the collection


def main():
    timeSeries = makeRequest("MSFT"); #structure api call by passing in a ticker symbol
    #evenrually pull hidden secret api key from another file that won't go on git.
        
#    print(timeSeries)
    
    populateMongo(timeSeries); #populate mongodb with all time series data as of today...
    ####eventually want to drop today and populate today's close data at midnight  after close
    ##!!!!!!!! or just use the opening price at 9:35am each day


#Tell python to call main function first
if __name__ == "__main__":
    main()
