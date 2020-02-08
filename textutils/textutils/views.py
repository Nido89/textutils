#I have created this file -Jalal-pwd
from django .http import HttpResponse
def index(request):
    return HttpResponse("This is Jalal reporting from Django")


def about(request):
    return HttpResponse("This is about jalal in django python")

