#I have created this file -Jalal-pwd
from django .http import HttpResponse
def index(request):
    return HttpResponse("<h1>This is Jalal reporting from Django</h1>")


def about(request):
    return HttpResponse("This is about jalal in django python")

