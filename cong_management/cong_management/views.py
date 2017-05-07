from django.http import HttpResponse
def homepage(request):
    return HttpResponse("<p>This is home page</p>")