import requests
from bs4 import BeautifulSoup

stockcode = "ITC"
print(stockcode)

stock_url = "https://www.google.com/finance/quote/"+str(stockcode)+":NSE"
print(stock_url)

response = requests.get(stock_url)
print(response)

soup = BeautifulSoup(response.text, 'html.parser')
# print(soup)

data_array = soup.find(class_='YMlKec fxKbKc').getText().strip()
print(type(data_array))
print(data_array[1:])