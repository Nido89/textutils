#I have created this file -Jalal-pwd
from django .http import HttpResponse
from django.shortcuts import render
def index(request):
    params = {'type': 'Hobby Projects', 'projects': 'coding websites'}
    return render(request,'index.html',params)

def home(request):
    return HttpResponse('''<h1>Home</h1><p><h2>This is Jalal's WEBSITE Portfolio from Django</h2>
    <a href= "https://github.com/Nido89"> Link to My Github Portfolio</a>
     <p>
     <h3>This is Jalal's WEBSITE Portfolio from Django</h3>
     <a href= "https://adunosolutions.eu"> Link to My Personnel Company website <a/>
                        </p>
                        <p>
     <h3>This is Jalal's WEBSITE Portfolio from Django</h3>
     <a href= "https://artmoc.com"> Link to My Print on demand store <a/>
                        </p>
                        <p>
     <h3>This is Jalal's WEBSITE Portfolio from Django</h3>
     <a href= "https://idoam.com"> Link to My directory lsiting site in php <a/>
                        </p>
     <a/>''')

def analyze(request):
    #get the Text
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    print(removepunc)
    print(djtext)
    if removepunc == "on":
    #analyzed = djtext
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params= {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed}
        return render(request,'analyze.html', params)
    else:

        return HttpResponse("Error")

# def capfirst(request):
#     return HttpResponse("capitalize first letter")
#
# def newlineremove(request):
#     return HttpResponse("Remove new first line")
#
# def spaceremover(request):
#     return HttpResponse("Space Remover <a href='/'> Go Back <a/>")
#
# def charcount(request):
#     return HttpResponse("count characters")
#
#
# def about(request):
#     return HttpResponse("This is about Jalal in django python")

