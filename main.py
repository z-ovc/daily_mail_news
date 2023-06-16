import requests
from send_email import send_email

#make a request
api_key = "ee08e398f6784a11a79b9f35bd11ed20"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-05-16&sortBy=publishedAt&apiKey=ee08e398f6784a11a79b9f35bd11ed20"
request = requests.get(url)

#get a fictionary of data
content = request.json()

#access the articles
body=""
for article in content["articles"]:
    if article["title"] and article["description"] is not None:
        body = body+article["title"]+article["description"]

body = body.encode("utf-8")
send_email(body)