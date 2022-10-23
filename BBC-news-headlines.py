from bs4 import BeautifulSoup
import requests

#header
headers = {'User-agent': 'Mozilla/5.0'}

# Requests the news webpage
request = requests.get('https://www.bbc.com/news', headers=headers)
html = request.content

# Create some soup
Beautysoup = BeautifulSoup(html, 'html.parser')


# Easy to read the HTML from the news site
# print(soup.prettify())

def bbc_news_headlines(keyword):
    news_list = []

    # Finds all the headers in BBC Home
    for h in Beautysoup.findAll('h3', class_='gs-c-promo-heading__title'):
        news_title = h.contents[0].lower()

        if news_title not in news_list:
            if 'bbc' not in news_title:
                news_list.append(news_title)


    no_of_news = 0
    keyword_list = []
    #userinput = input("Keywords from user") Function to determine user input
    #print("userinput")
    
    # Goes through the list and searches for the keyword
    for i, title in enumerate(news_list):
        text = ''
        if keyword.lower() in title:
            text = ' <------------ KEYWORD'
            no_of_news += 1
            keyword_list.append(title)

        print(i + 1, ':', title, text)

    # Prints the Titles of the articles that contain the keywords
    print(f'\n--------- Total mentions of "{keyword}" = {no_of_news} ---------')
    for i, title in enumerate(keyword_list):
        print(i + 1, ':', title)


bbc_news_headlines('20')
