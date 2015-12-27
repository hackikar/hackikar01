from django.http import HttpResponse


def index(request):
    return HttpResponse("אהלן עולם פה זה כל הרעיונות.")