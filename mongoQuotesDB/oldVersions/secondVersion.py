import requests;
import collections;


alphaVantageKey = "0ZU6NM5CMUSMR7DO"

def makeRequest(symbol):
    #create api call string below. receive time series from api
    request = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol="+symbol+"&outputsize=compact&datatype=json&apikey="+alphaVantageKey
    
    response = requests.get(request)
    #my own key used. output size compact is last 100 datapoints..full is last 20+ yrs of data
    
    responseBody = response.content; #remove header from time series

    return responseBody;


def cutHeader(responseBody):
    bodyString = str(responseBody); #cast list as a string to parse through
    endHeaderPosition = bodyString.find("}"); #find end bracket of header string
    startPosition = endHeaderPosition + len(",    \"Time Series (Daily)\":   "); #add characters for "Time Series (Daily)": to position
    timeSeriesString = bodyString[startPosition:-2] #take only the time series from the body, drop all other characters from request string

    return timeSeriesString;


def populateMongo(timeSeries):
    print(timeSeries)
    ####POSSIBLY A RECURSIVE FUNCTION TO GO FROM timeseries.find("{") to timeseries.find("}")
    ######then call function recursively starting at position of timeseries.find("}") to begin looking for exact start of next entry
    #######each entry is send to an .insertOne()

    #this needs to connect to mongodb
    #for every day in response body, add the data to collection timeSeries
    #wil then be able to filter for the close prices from each day's data
    ###each day is a "file"?? in the collection


def main():
    responseBody = makeRequest("MSFT"); #structure api call by passing in a ticker symbol
    #evenrually pull hidden secret api key from another file that won't go on git.
    
    timeSeriesString = cutHeader(responseBody); #get the time series in string form from the response body

    populateMongo(timeSeriesString); #populate mongodb with all time series data as of today...
    ####eventually want to drop today and populate today's close data at midnight  after close
    ##!!!!!!!! or just use the opening price at 9:35am each day

#Tell python to call main function first
if __name__ == "__main__":
    main()
