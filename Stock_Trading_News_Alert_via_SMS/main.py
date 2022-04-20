import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = "YOUR STOCK API KEY HERE"   # Stock API: Sign up at https://www.alphavantage.co
NEWS_API_KEY = "YOUR NEWS API KEY HERE"     # News API: Sign up at https://newsapi.org/v2/everything

# Twilio Account ID and authentication key.
account_sid = "YOUR TWILIO ID HERE"         # SMS: Sign up at https://www.twilio.com/
auth_token = "YOUR TWILIO AUTHENTICATION CODE HERE"

# Stock parameters to get the stock data
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
}
# News parameters to get the news data
news_parameters = {
    "q": COMPANY_NAME,
    "apiKey": NEWS_API_KEY

}

# Using https://www.alphavantage.co to get yesterday and day_before_yesterday closing stock prices
response = requests.get(url="https://www.alphavantage.co/query", params=stock_parameters)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]


#  Yesterday and day before yesterday stock
stock_data = [value for key, value in data.items()]
yesterday_data = (stock_data[0]['4. close'])
day_before_yesty_data = (stock_data[1]['4. close'])

# Calculating percent change
percent_change = ((float(yesterday_data) - float(day_before_yesty_data)) / float(day_before_yesty_data)) * 100
print(percent_change)

# Setting change symbols for the stock change
stock_up_down = None
if percent_change > 0:
    stock_up_down = "🔺"
else:
    stock_up_down = "🔻"

# if stock change is greater than x, get the news and send details
if abs(percent_change) >= 5:

    # Using  https: // newsapi.org to get the first 3 news pieces for the COMPANY_NAME.
    news_request = requests.get(url="https://newsapi.org/v2/everything", params=news_parameters)
    news_request.raise_for_status()
    news_data = news_request.json()

    for news in range(3):
        headline = news_data["articles"][news]["title"]
        brief = news_data["articles"][news]["description"]

# Sending separate messages with the percentage change and each article's title and description to your phone number.
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=(f'{STOCK}: {stock_up_down} {abs(round(percent_change, 2))}%\n'
                  f'Headline: {headline}\n'
                  f'Brief: {brief}\n'),
            from_='YOUR TWILIO NUMBER HERE',
            to='YOUR VERIFIED NUMBER HERE'
        )

        print(message.sid) 
