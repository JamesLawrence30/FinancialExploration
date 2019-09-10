import requests;
import collections;
"""import json;"""

alphaVantageKey = "0ZU6NM5CMUSMR7DO"

def makeRequest(symbol):
    #create api call string below. receive time series from api
    request = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol="+symbol+"&outputsize=compact&datatype=json&apikey="+alphaVantageKey)
    #my own key used. output size compact is last 100 datapoints..full is last 20+ yrs of data
    requestBody = request.content
#    print(requestBody);
    print(requestBody[7])
    Tseries = request["Time Series (Daily)"]; #remove header from time series

    return Tseries;
	

def dailyData(listOfDays):
    dataList = []
    for day in listOfDays:
#        dataList.append(listOfDays[day])
        dataList.append(day);

    return dataList;




def main():
    request = makeRequest("MSFT"); #structure api call by passing in a ticker symbol
    #evenrually pull hidden secret api key from another file that won't go on git.
    closePrices = dailyData(request);
    print(closePrices); #print all close prices with dates
#   print(closePrices[3]); #print just on key value pair of close price and date
    
#Tell python to call main function first
if __name__ == "__main__":
    main()
