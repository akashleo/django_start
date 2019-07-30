from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
     return(render(request, 'home.html'))

def count(request):
     fulltext= request.GET['fulltext']
     #print(fulltext)
     wordlist = fulltext.split();

     worddictionary = {}

     for word in wordlist:
          if word in worddictionary:
               worddictionary[word]+=1
          else:
               worddictionary[word]=1

     sortedwords =sorted(worddictionary.items(), key= operator.itemgetter(1), reverse = True)


     totalwords = len(wordlist)

     return(render(request, 'count.html' , {"fulltext":fulltext, "count":totalwords, "sortedwords":sortedwords}))

