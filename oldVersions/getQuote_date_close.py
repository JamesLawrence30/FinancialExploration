import requests;
import collections;
"""import json;"""

alphaVantageKey = "0ZU6NM5CMUSMR7DO"

def makeRequest(symbol):
    #create api call string below. receive time series from api
    Tseries = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol="+symbol+"&outputsize=compact&datatype=json&apikey="+alphaVantageKey).json()
    #output size compact is last 100, full is like 20,000+
    #my own key used. output size compact is last 100 datapoints..full is last 20+ yrs of data
    noHeader = Tseries["Time Series (Daily)"]; #remove header from time series

    return noHeader;
	

def nested_dict_iter(nested):
    for key, value in nested.iteritems():
        #If we're at inner most level of nested dict, record value...else, move down a level recursively

        if isinstance(value, collections.Mapping):  #I think this checks if we're at innermost level or not...unsure how. found function  online
            for inner_key, inner_value in nested_dict_iter(value):  #moves recursively through the nested dictionary to get down to final inner level of dict
                if(inner_key == "4. close"):  #choose which parameter I want to record
                    dictItem = "{\""+key+"\":\""+inner_value+"\"}"  #create a dictionary entry of ("date":"close price")
#                    dictItem = inner_value #create a list value of close price only
                    yield dictItem  #add this new dictionary entry to a list
        
        else:
            yield key, value  #key is the date, value is all the parameters of that date (open, close, high, low....)

    return


def main():
    request = makeRequest("MSFT"); #structure api call by passing in a ticker symbol
    #evenrually pull hidden secret api key from another file that won't go on git.
    closePrices = list(nested_dict_iter(request)); #get close price using the nested dictionary iteration function
    print(closePrices); #print all close prices with dates
#    print(closePrices[3]); #print just on key value pair of close price and date
    
#Tell python to call main function first
if __name__ == "__main__":
    main()
