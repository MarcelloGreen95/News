from django.shortcuts import render


def home(request):
    context_dict = {'boldmessage': 'April 16th, 2021, 10:36am',
                    '2ndmessage':'It has now been confirmed that Jade is angry',
                    '3rdmessage': 'April 16th, 2021, 10:37am',
                    '4thmessage': 'It is official, Matt is amazing'}
    return render(request, 'home.html', context=context_dict)
