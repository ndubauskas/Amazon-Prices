import requests
from bs4 import BeautifulSoup
import smtplib
my_email = "nicktestpython@gmail.com"
password = "PASSWORD"

url = "https://www.amazon.com/Apple-MX542AM-A-AirTag-Pack/dp/B0932QJ2JZ/ref=zg_bs_c_electronics_d_sccl_4/144-7195509-9994707?pd_rd_w=C8Jvm&content-id=amzn1.sym.309d45c5-3eba-4f62-9bb2-0acdcf0662e7&pf_rd_p=309d45c5-3eba-4f62-9bb2-0acdcf0662e7&pf_rd_r=1TQSRW3TP06P5CF1SEXQ&pd_rd_wg=XBYhi&pd_rd_r=a6a870eb-5d10-4587-af76-cf59ac87e892&pd_rd_i=B0932QJ2JZ&psc=1"
headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url=url,headers=headers)
# print(response.text)
soup = BeautifulSoup(response.text, "html.parser")
# print(soup.prettify())
#Look for class="a-price-whole"

# current_price = soup.find_all("span",{"class": "a-price-whole"})
current_price = soup.find_all(name= "span",class_= "a-price-whole")
price = soup.find(class_ ="a-price-whole").get_text()
price = price.replace(".","")
price_float = float(price)
print(price)

if price_float < 100.0:
    print("sending email")
    connection = smtplib.SMTP("smtp.gmail.com",port=587)
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=my_email,
        msg=f"Airtags are below $100!! They are at {price_float}".encode("utf-8")
    )
    connection.close()
    print("completed")