from django.shortcuts import render

import requests
import feedparser


def main(request):
    news_set1 = []
    news_set2 = []
    NewsFeed = feedparser.parse("https://news.tut.by/rss/42/education.rss")
    latest_news_set1 = NewsFeed.entries[:2]
    latest_news_set2 = NewsFeed.entries[3:5]

    print(NewsFeed.entries[0]['published'])

    for item_news in latest_news_set1:
        news_set1.append({
                        'title': item_news['title'],
                        'source_link': item_news['links'][0]['href'],
                        'image_link': item_news['links'][1]['href'],
                        'tag_name': item_news['tags'][0]['term'],
                        'tag_link': item_news['tags'][0]['scheme']
                        })

    for item_news in latest_news_set2:
        news_set2.append({
                        'title': item_news['title'],
                        'source_link': item_news['links'][0]['href'],
                        'image_link': item_news['links'][1]['href'],
                        'tag_name': item_news['tags'][0]['term'],
                        'tag_link': item_news['tags'][0]['scheme']
                        })

    news_telecommunication_set1 = []
    NewsTelecomFeed = feedparser.parse("https://news.tut.by/rss/42/internet.rss")
    latest_news_set3 = NewsTelecomFeed.entries[:5]

    for item_news in latest_news_set3:
        news_telecommunication_set1.append({
                        'title': item_news['title'],
                        'source_link': item_news['links'][0]['href'],
                        'image_link': item_news['links'][1]['href'],
                        'tag_name': item_news['tags'][0]['term'],
                        'tag_link': item_news['tags'][0]['scheme']
                        })


    return render(request, 'main.html', {'data_set1': news_set1, 'data_set2': news_set2, 'data_set3': news_telecommunication_set1})
