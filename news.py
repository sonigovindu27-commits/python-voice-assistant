import requests
from ss import key

api_address = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={key}'
json_data = requests.get(api_address).json()

def news():
    ar = []
    articles = json_data.get('articles', [])
    count = min(3, len(articles))  # avoid index error if less than 3
    for i in range(count):
        ar.append("Number " + str(i+1) + ": " + articles[i]['title'] + ".")
    return ar

#arr = news()
#print(arr)
