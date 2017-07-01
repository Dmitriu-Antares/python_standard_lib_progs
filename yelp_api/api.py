import requests


idid='ah6E77FUNKBOAfjd1G0Maw'
key ='vawFjrbgngyg5CHUZMQW4if6GNIeTxgEDleFb5ENDRxT0zRQo0Jlb0aKmzNpJdFE'
r = requests.post("https://api.yelp.com/oauth2/token", data={'client_id': idid, 'client_secret': key})
response = r.json()
token=str(response['access_token'])

#auth = OAuth1(key,token)


def search(location):
    params ={
        'location':location
    }
    req = requests.get('https://api.yelp.com/v3/businesses/search',headers={'Authorization': 'Bearer '+token},params=params)
    answer = req.json()
    filepath='site-{loc}.txt'.format(loc=location)
    with open(filepath,'a') as f:
        for i in answer['businesses'] :
            name=i['name']
            rating=i['rating']
            location=i['location']['display_address']
            text = '{name},{rating},{location}\n'.format(
                name=name,
                rating=rating,
                location=location
            )
            f.write(text)

data = search('NY')
