from django.shortcuts import render


from .services import get_education_news, get_internet_news


def main(request):
    return render(request, 'main.html',
                  {
                    'data_set1': get_education_news()[0],
                    'data_set2': get_education_news()[1],
                    'data_set3': get_internet_news()
                  })
