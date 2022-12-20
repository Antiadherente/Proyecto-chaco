from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return HttpResponse("<h1>Queonda perry</h1>");
def reloco(request):
    return render(request, "paginas/reloco.html");

