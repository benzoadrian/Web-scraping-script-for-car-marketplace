from bs4 import BeautifulSoup
import requests

url = "https://www.autoscout24.nl/lst/ferrari/488/ve_pista"

result = requests.get(url)

doc = BeautifulSoup(result.text, "html.parser")

prices = doc.find_all('span',class_="SellerInfo_name__yjUE6")

arr=[]

for s in prices:
 arr.append(s.next_element)

print(arr) 





