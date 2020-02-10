#I have created this file -Jalal-pwd
from django .http import HttpResponse
# def index(request):
#     return HttpResponse('''<h1>This is Jalal's WEBSITE Portfolio from Django</h1>
#     <a href= "https://github.com/Nido89"> Link to My Github Portfolio</a>
#      <p>
#      <h2>This is Jalal's WEBSITE Portfolio from Django</h2>
#      <a href= "https://adunosolutions.eu"> Link to My Personnel Company website <a/>
#                         </p>
#                         <p>
#      <h2>This is Jalal's WEBSITE Portfolio from Django</h2>
#      <a href= "https://artmoc.com"> Link to My Print on demand store <a/>
#                         </p>
#                         <p>
#      <h2>This is Jalal's WEBSITE Portfolio from Django</h2>
#      <a href= "https://idoam.com"> Link to My directory lsiting site in php <a/>
#                         </p>
#      <a/>''')

def index(request):
    return HttpResponse("<h1>Home</h1>")

def removepunc(request):
    return HttpResponse("remove punctuations")

def capfirst(request):
    return HttpResponse("capitalize first letter")

def newlineremove(request):
    return HttpResponse("Remove new first line")

def spaceremover(request):
    return HttpResponse("Remove space")

def charcount(request):
    return HttpResponse("count characters")


def about(request):
    return HttpResponse("This is about Jalal in django python")

