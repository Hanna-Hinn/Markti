import requests



def convertCurrency(result, currencyType):
    

    url = "https://api.freecurrencyapi.com/v1/latest?apikey=vbZI4A4fAm9wrUZkQkuf8S6z69ivphZfHsee2pkm"

    resp = requests.get(url)

    # {"data":{"AUD":1.492317,"BGN":1.798568,"BRL":4.889407,"CAD":1.346753,"CHF":0.895526,"CNY":6.952607,"CZK":21.71843,"DKK":6.84781,"EUR":0.919681,"GBP":0.798421,"HKD":7.838458,"HRK":6.929336,"HUF":339.610377,"IDR":14800.522647,"ILS":3.662404,"INR":82.267085,"ISK":138.790153,"JPY":136.050272,"KRW":1335.752157,"MXN":17.448125,"MYR":4.497506,"NOK":10.596432,"NZD":1.601913,"PHP":56.083085,"PLN":4.144564,"RON":4.543305,"RUB":79.750131,"SEK":10.348076,"SGD":1.336287,"THB":33.77004,"TRY":19.684725,"USD":1,"ZAR":19.011935}}


    # place the data in a dictionary
    data = resp.json()

    # check if the currency type is valid
    if currencyType not in data["data"] or currencyType == "USD":
        currencyType = "USD"
        print ("Invalid currency type, defaulting to USD")
        return result

    for product in result:
        product.product_price = round(product.product_price * data["data"][currencyType], 2)

       

    return result
