from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):
    return render(request, 'home.html', {'hithere': 'This is me'})


def about(request):
    return render(request, 'about.html', {'about_message': 'This is the about message'})


def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    word_dict = dict()

    for word in wordlist:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    sorted_word_dict = sorted(word_dict.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'texto': fulltext,
                                          'count': len(wordlist),
                                          'sorted_word_dict': sorted_word_dict})
