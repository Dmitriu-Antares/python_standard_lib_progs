import requests
from bs4 import BeautifulSoup

base_url = "https://www.yelp.com/search?find_desc=dinner&find_loc="
loc = "New York,NY"
page = 20
while page < 201:
    url = base_url + loc + '&start=' + str(page)
    #giving a status
    sport = requests.get(url)
    #text
    s_text = sport.text
    #beaty
    sport_soup = BeautifulSoup(s_text,'html.parser')
    #find all objects
    sport_soup_obj = sport_soup.findAll('div',{'class','biz-listing-large'})
    #every single object load in file
    filepath = 'site-{loc}'.format(loc=loc)
    with open(filepath,'a') as f:
        for obj in sport_soup_obj:
            titles = obj.findAll('a',{'class','biz-name'})[0].text.encode('utf8')
            address = obj.findAll('address')[0].text.encode('utf8')
            tel = obj.findAll('span',{'class','biz-phone'})[0].text.encode('utf8')
            text='{title},{address},{tel}'.format(
                    title=titles,
                    address=address,
                    tel=tel).replace(' ','')
            f.write(text)
    page +=10
