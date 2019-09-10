import requests;
import collections;
"""import json;"""

alphaVantageKey = "0ZU6NM5CMUSMR7DO"

def makeRequest(symbol):
    #create api call string below. receive time series from api
    request = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol="+symbol+"&outputsize=compact&datatype=json&apikey="+alphaVantageKey
    
    response = requests.get(request)
    #my own key used. output size compact is last 100 datapoints..full is last 20+ yrs of data
    
    responseBody = response.content; #remove header from time series

    return responseBody;



def updateMongo(responseBody):
    print(responseBody);
    #this needs to connect to mongodb
    #for every day in response body, add the data to collection timeSeries
    #wil then be able to filter for the close prices from each day's data
    ###each day is a "file"?? in the collection


def main():
    responseBody = makeRequest("MSFT"); #structure api call by passing in a ticker symbol
    #evenrually pull hidden secret api key from another file that won't go on git.
    updateMongo(responseBody);

#Tell python to call main function first
if __name__ == "__main__":
    main()
