from django.http import HttpResponse

def index(request):
    return HttpResponse("mick says hello world!")

# Create your views here.
