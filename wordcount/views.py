from django.http import HttpResponse
from django.shortcuts import render  # this tool looks for html that we want to return when triggering a function here (for example homepage)
import operator

def homepage(request): # request is obligatory because anytime someone is coming looking fro a url on a website it sends this
                       # request object - it contains what's the url they're looking for, cookies, what browser they're using and other stuff
    # return HttpResponse("Hello") # "Hello" string cannot be returned, we need to return HttpResponse object
    return render(request, 'home.html')
    # return render(request, 'home.html', {'hithere': 'this is me'}) # we can pas additional 3rd argument as dict and in template we can get value of dict
                                                                    # can't have whitespaces in dict keys, so 'hi there' is not allowed

def eggs(request):  # so now is user goes to localhost:8000/eggs, the page will return that string
    return HttpResponse('<h1>eggs<h1>') # so input can be an html, but obviously not hardcoded here, so we should use !!!templates! where we can, besides plain html, run python code as well


# this function addresses user to "count/" page and count.html
def count(request):
    # we can get value of fulltext=whatever+text+user+types :
    fulltext = request.GET['fulltext'] # this gives us back text "whatever+text+user+types"
    print(fulltext) # will show in terminal

    wordlist = fulltext.split()
    worddictionary = {}
    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1
    # sort words in descending order
    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordlist), 'sortedwords': sortedwords}) # dict itself also could be shown

def about(request):
    return render(request, 'about.html')
