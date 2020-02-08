#I have created this file -Jalal-pwd
from django .http import HttpResponse
def index(request):
    return HttpResponse('''<h1>This is Jalal reporting from Django</h1> <a href= "https://github.com/Nido89"> Link to My Github Portfolio <a/>''')


def about(request):
    return HttpResponse("This is about Jalal in django python")

