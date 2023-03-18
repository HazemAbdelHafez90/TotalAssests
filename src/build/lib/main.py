import requests
from bs4 import BeautifulSoup
import re


def get_gold_price_in_egypt():
    url = 'https://www.masrawy.com/gold'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    curr_gold_details = soup.find('div', class_='currGoldDtls')
    gram_price_in_egypt = 0
    if curr_gold_details is not None:
        numbers = re.findall(r'\d+\.\d+|\d+', curr_gold_details.text.strip())
        gram_price_in_egypt = float(numbers[1])
    else:
        print('Element not found.')
    return gram_price_in_egypt


def get_global_gold_price_in_usd():
    url = 'https://www.arabictrader.com/ar/commodities/gold-price/%D8%B3%D8%B9%D8%B1-%D8%A7%D9%84%D8%B0%D9%87%D8%A8'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    curr_gold_details = soup.find('div', class_='table-responsive')
    gram_price_in_usd = 0
    if curr_gold_details is not None:
        numbers = re.findall(r'\d+\.\d+|\d+', curr_gold_details.text.strip())
        gram_price_in_usd = float(numbers[3])
    else:
        print('Element not found.')
    return gram_price_in_usd


usd = float(input("Enter how many usd you have "))
gold  = float(input("Enter how many grams of gold you have "))
has_stocks = input("do you have stock shares? answer with y or n ")
stocks_assets =0
if(has_stocks =='y'):
    stocks_assets = float(input("what is your total money in stocks "))

egp  = float(input("Enter how many EGP you have "))






gold_price_in_egypt_in_egp = get_gold_price_in_egypt()
global_gold_price_in_usd = get_global_gold_price_in_usd()
usd_price_in_black_market = gold_price_in_egypt_in_egp / global_gold_price_in_usd

print(f"Gold price in Egypt: {gold_price_in_egypt_in_egp:.2f} EGP/gram")
print(f"Global gold price in USD: {global_gold_price_in_usd:.2f} USD/gram")
print(f"USD price in black market: {usd_price_in_black_market:.2f} EGP/USD")  



print(f"Your Total Assets are : {gold*gold_price_in_egypt_in_egp + usd *usd_price_in_black_market +egp +stocks_assets:.2f} EGP")  



