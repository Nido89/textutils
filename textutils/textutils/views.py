#I have created this file -Jalal-pwd
from django .http import HttpResponse
from django.shortcuts import render
def index(request):
    params = {'type': 'Hobby Projects', 'projects': 'coding websites'}
    return render(request,'index.html',params)
def contact(request):
    params = {'type': 'Hobby Projects', 'projects': 'coding websites'}
    return render(request,'contact.html',params)

def home(request):
    return HttpResponse('''<h1>About Me</h1><p><h2>This is Jalal's WEBSITE Portfolio from Django</h2>
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
    djtext = request.POST.get('text', 'default')
    #check the values of checkboxes
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charactercounter = request.POST.get('charactercounter', 'off')
    # print(removepunc)
    # print(djtext)
    #Check which checkbox is on
    if removepunc == "on":
    #analyzed = djtext
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params= {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        #Analyze the Text for Punctuations in this case
        #return render(request,'analyze.html', params)
    if(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Upper Case', 'analyzed_text':
    analyzed}
            # Analyze the Text for Punctuations in this case
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed New Lines', 'analyzed_text':
            analyzed}
        # Analyze the Text for Punctuations in this case
        djtext = analyzed
        #return render(request, 'analyze.html', params)


    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index +1]==" "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed New Lines', 'analyzed_text':
            analyzed}
        # Analyze the Text for Punctuations in this case
        djtext = analyzed
        #return render(request, 'analyze.html', params)


    if (charactercounter == "on"):
        analyzed = len(djtext)
        params = {'purpose': 'Number of Characters counted', 'analyzed_text':
            analyzed}
        # Analyze the Text for Punctuations in this case
        #djtext = analyzed
        #return render(request, 'analyze.html', params)
    if(removepunc!= "on" and newlineremover!= "on" and fullcaps!="on" and extraspaceremover!= "on" and charactercounter!= "on"):
        return HttpResponse("Please select one option and Try Again")

    return render(request, 'analyze.html', params)
    #else:
    #
    #     return HttpResponse("Error")
# def capfirst(request):
#     return HttpResponse("capitalize first letter")
# def newlineremove(request):
#     return HttpResponse("Remove new first line")
# def spaceremover(request):
#     return HttpResponse("Space Remover <a href='/'> Go Back <a/>")
# def charcount(request):
#     return HttpResponse("count characters")
# def about(request):
#     return HttpResponse("This is about Jalal in django python")