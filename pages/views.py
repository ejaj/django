from django.http import HttpResponse

# Create your views here.

def homePageView(request):
    return HttpResponse("<h1>Hello world ! </h1>")