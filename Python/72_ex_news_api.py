import requests

key = 'bab16070e3b1484ebb8108305b9ccfdb'
def get_news(api_key, country_code='us'):
    query = input("search news please:")
    url = f'https://newsapi.org/v2/everything?q={query}&from=2024-01-07&sortBy=publishedAt&apiKey={key}'
    response = requests.get(url)
    news = response.json()
    return news

news = get_news(key)

 
 
for i in range(11):
    fn = news['articles'][i]['description']
    print(f'{fn}\n')
