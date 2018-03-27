



contain.div.a.img["title"]



availability = 
>>>availability["itemprop"]

price = contain.findAll('span', attrs={"class": "price-sales"})
>>> product_price = price[0].text.strip()
// >>>price["data-price"]



for contain in new:
     title = contain.div.a.img["title"]
     price = contain.findAll('span', attrs={"class": "price-sales"})
     print("Title: "+title+"\n")
     print("price: "+(price[0].text.strip())+"\n")


