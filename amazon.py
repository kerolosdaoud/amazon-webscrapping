import requests
import bs4
page = requests.get("https://www.amazon.eg/%D9%85%D9%88%D8%A8%D8%A7%D9%8A%D9%84%D8%A7%D8%AA/b/?ie=UTF8&node=21832883031&ref_=nav_cs_mobiles")
info =page.content
soup=bs4.BeautifulSoup(info, "html.parser")

# print(info)
information=soup.find_all('div',{'class':"a-section a-spacing-none a-spacing-top-small s-title-instructions-style"})
price=soup.find_all('span',{'class':'a-price-whole'})
# company= soup.find_all('span',{'class':'a-size-base'})
# print(company)
mobile_info=[]
mobile_price=[]
for i in range(len(information)):
    mobile_info.append(information[i].text)
# print(mobile_info)

for p in range(len(price)):
    mobile_price.append(price[p].text)

# print(mobile_price)
for item in enumerate(mobile_info):
    print(item)

for price in enumerate(mobile_price):
     print(price)

# with open('C:\Users\AIO','w') as myfile:
#     wr = csv.writer((myfile))
    # wr.writerow(['mobile_info','mobile_price'])


