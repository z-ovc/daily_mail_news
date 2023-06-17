import requests
from send_email import send_email

#make a request
api_key = "ee08e398f6784a11a79b9f35bd11ed20"
topic = "tesla"
url = f"https://newsapi.org/v2/everything?q={topic}&from=2023-05-17&sortBy=publishedAt&apiKey=ee08e398f6784a11a79b9f35bd11ed20"
request = requests.get(url)

#get a fictionary of data
content = request.json()

#access the articles
body=""
for article in content["articles"]:
    if article["title"] and article["description"] is not None:
        body = "Subject: today-news\n" +body+article["title"]+article["description"]+"\n"+article["url"]+2*"\n"

body = body.encode("utf-8")
send_email(body)
