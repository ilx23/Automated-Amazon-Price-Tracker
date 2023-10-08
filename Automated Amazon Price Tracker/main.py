import requests
from bs4 import BeautifulSoup
from smtplib import SMTP
EMAIL_ADDRESS = 'iliakeshavarz23@gmail.com'
EMAIL_PASSWORD = 'zxtokhqdyecyoijh'
AZ_URL = 'https://www.amazon.com/ASUS-Gaming-viewable-Monitor-VG249Q3A/dp/B0C7BFJHR7/ref=sr_1_2?crid=1DUM1PM4EGSOR&keywords=monitor&qid=1696749945&sprefix=monitor+%2Caps%2C386&sr=8-2'

### PASS ALONG SOME HEADERS IN ORDER FOR THE REQUEST TO RETURN THE ACTUAL WEBSITE HTML ###
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/118.0",
    "Accept-Language": "en-US,en;q=0.5"
}

### GET REQUEST AND GET HOLD OF THE PRODUCT PRICE AND TITLE ###
response = requests.get(AZ_URL, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')
product_title = soup.find('span', class_='product-title-word-break').getText().strip()
product_price = soup.find('span', class_='a-offscreen').getText()
price_without_currency = product_price.split('$')[1]
price_as_float = float(price_without_currency)

### SENDING ALERT EMAIL ABOUT PRICE IF IT WAS LESS THAN 90$ ###
msg_email = f'Subject: Amazon Price Alert \n\n {product_title} is now ${price_as_float}'.encode('utf-8')

if price_as_float < 100:
    with SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        connection.sendmail(EMAIL_PASSWORD, 'iliaplays7@gmail.com', msg_email)
