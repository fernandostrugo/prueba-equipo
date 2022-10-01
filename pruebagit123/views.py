from django.http import HttpResponse


def hola(request):
    return HttpResponse("<h1>ESTO ES NUEVO</h1>")
def mechi(request):
    return HttpResponse("<h1>TE AMO GORDITA ♥</h1>")