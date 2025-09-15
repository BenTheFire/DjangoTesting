from django.http import HttpResponse


def home(request):
    return HttpResponse(""
                        "<h1>Welcome to the Basic Django Site</h1>"
                        "<p>We're working on it!</p>"
                        "")
