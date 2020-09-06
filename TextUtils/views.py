def ex1(request):
    s = '''<h2>Navigation Bar<br></h2>
                <a href="https://www.linkedin.com/">Linkedin</a><br> 
                <a href="https://www.facebook.com/">Facebook</a><br>
                <a href="https://www.flipkart.com/">Flipkart</a><br>
                <a href="https://www.hindustantimes.com">News</a><br>
                <a href="https://www.google.com/">Google</a>'''
    return HttpResponse(s)

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    params = {'name': 'pranjal', 'place': 'pune'}
    return render(request, 'index.html', params)

def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    remover = request.POST.get('remover', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    charcounter = request.POST.get('charcounter', 'off')

    if removepunc == 'on':
        punctuations = '''!"  # $%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        analyzed = " "
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'removed punctuation', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif (fullcaps == "on"):
        analyzed = " "
        for char in djtext:
            analyzed = analyzed + char.upper()
            params = {'purpose': 'changed to uppercase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif (remover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != '\r':
                analyzed = analyzed + char.upper()
        params = {'purpose': 'removed new lines', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif (spaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'removed new lines', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif charcounter == "on":
        analyzed = 0
        for char in djtext:
            analyzed = len(djtext)
        params = {'purpose': 'Character Counter', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse('error ')

def capitalizefirst(request):
    return HttpResponse("capitalizefirst")

def newlineremover(request):
    return HttpResponse("newlineremover")

def Spaceremove(request):
    return HttpResponse("Spaceremove <a href='/'>back</a>")

def charcount(request):
    return HttpResponse("charcount")